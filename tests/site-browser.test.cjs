// Exercise the real renderer, including its assistive MathML, rather than mock it.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { spawn } = require('node:child_process');
const { once } = require('node:events');
const { chromium } = require('playwright');

const root = path.resolve(__dirname, '..');
const site = path.join(root, 'site');
const mathjax = path.dirname(require.resolve('mathjax/package.json'));
const port = process.env.TEST_PORT || '18765';
const origin = `http://127.0.0.1:${port}`;
function files(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry =>
    entry.isDirectory() ? files(path.join(dir, entry.name)) : [path.join(dir, entry.name)]);
}

(async () => {
  const server = spawn(process.env.PYTHON || 'python3', ['-u', '-m', 'http.server', port,
    '--bind', '127.0.0.1', '--directory', site], { stdio: ['ignore', 'pipe', 'ignore'] });
  let browser;
  try {
    await Promise.race([once(server.stdout, 'data'), once(server, 'exit').then(() => {
      throw new Error(`Cannot start the test server on port ${port}`);
    })]);
    browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({ viewport: { width: 390, height: 844 } });
    await context.route('**/*', async route => {
      const url = new URL(route.request().url());
      if (url.origin === origin) return route.continue();
      // Use the same pinned MathJax distribution offline; CDN availability is a
      // separate operational concern and must not make CI nondeterministic.
      const prefix = '/mathjax@3.2.2/';
      if (url.hostname === 'unpkg.com' && url.pathname.startsWith(prefix)) {
        const file = path.resolve(mathjax, url.pathname.slice(prefix.length));
        assert(file.startsWith(mathjax + path.sep));
        return route.fulfill({ path: file });
      }
      return route.abort();
    });
    await context.addInitScript(() => localStorage.setItem('/.__consent', JSON.stringify({ github: false, analytics: false })));
    const page = await context.newPage();
    await page.goto(origin);
    await page.locator('#home-search').fill('微积分');
    await page.locator('.nh-search button').click();
    await page.waitForFunction(() => document.querySelectorAll('.md-search-result__item').length > 0);
    assert.equal(await page.locator('.md-search__input').inputValue(), '微积分');
    await page.close();

    const mathPages = files(site).filter(file => file.endsWith('.html') &&
      /<(?:span|div)\b[^>]*\bclass=(?:"arithmatex"|arithmatex)(?=[ >])/.test(fs.readFileSync(file, 'utf8')));
    assert(mathPages.length > 0, 'The site must include math pages in this check');
    const failures = [];
    let index = 0;
    await Promise.all(Array.from({ length: 3 }, async () => {
      const page = await context.newPage();
      while (index < mathPages.length) {
        const file = mathPages[index++];
        const relative = path.relative(site, file).split(path.sep).join('/');
        try {
          await page.goto(origin + '/' + encodeURI(relative));
          await page.waitForFunction(() => window.MathJax?.startup?.document, { timeout: 20000 });
          await page.evaluate(() => MathJax.startup.promise);
          const result = await page.evaluate(() => {
            const article = document.querySelector('article.md-content__inner');
            return {
              formulas: article.querySelectorAll('.arithmatex').length,
              rendered: article.querySelectorAll('.arithmatex > mjx-container').length,
              nested: article.querySelectorAll('mjx-assistive-mml mjx-container').length,
              errors: Array.from(article.querySelectorAll('[data-mjx-error], mjx-merror')).map(e => e.outerHTML),
              width: document.documentElement.scrollWidth,
            };
          });
          assert.equal(result.rendered, result.formulas, `${relative}: an expression did not render`);
          assert.equal(result.nested, 0, `${relative}: assistive MathML was typeset twice`);
          assert.deepEqual(result.errors, [], `${relative}: MathJax rejected an expression`);
          assert(result.width <= 393, `${relative}: page overflowed on mobile`);
        } catch (error) { failures.push(`${relative}: ${error.message}`); }
      }
      await page.close();
    }));
    assert.deepEqual(failures, [], failures.join("\n"));
    const resources = await context.newPage();
    await resources.goto(origin + '/CS/tools/markdown-advanced/');
    const audio = await resources.evaluate(() => new Promise(resolve => {
      const audio = document.querySelector('audio');
      audio.onloadedmetadata = () => resolve(audio.duration);
      audio.onerror = () => resolve(0);
      audio.load();
    }));
    assert(audio > 0, 'The original example audio must remain playable');
    for (const image of files(path.join(site, 'MATH/calculus/res/images/supplements'))) {
      await resources.goto(origin + '/' + path.relative(site, image).split(path.sep).join('/'));
      assert.equal(await resources.locator('svg').count(), 1, `${image}: image did not load`);
      const clipped = await resources.evaluate(() => {
        const width = document.querySelector('svg').viewBox.baseVal.width;
        return Array.from(document.querySelectorAll('text')).filter(e => {
          const box = e.getBBox();
          return box.x + box.width > width - 8;
        }).map(e => e.textContent);
      });
      assert.deepEqual(clipped, [], `${image}: labels extend beyond the image`);
    }
    assert.deepEqual(failures, [], failures.join('\n'));
    console.log(`Browser checks passed: ${mathPages.length} math pages, search, original audio and all supplement images.`);
  } finally {
    await browser?.close();
    server.kill();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
