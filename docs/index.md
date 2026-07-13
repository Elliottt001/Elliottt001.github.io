---
title: Knowledge Atlas
hide:
  - navigation
  - toc
---

<section class="ka-home" aria-label="Elliottt Zhang 的个人知识库首页">
  <div class="ka-ambient ka-ambient--cyan" aria-hidden="true"></div>
  <div class="ka-ambient ka-ambient--violet" aria-hidden="true"></div>
  <div class="ka-noise" aria-hidden="true"></div>

  <div class="ka-shell">
    <header class="ka-hero ka-reveal">
      <div class="ka-hero__copy">
        <p class="ka-kicker">Knowledge Atlas / Personal Knowledge OS</p>
        <h1>Note</h1>
        <p class="ka-hero__lead">记录、理解、构建</p>
        <p class="ka-hero__intro">
          这里整理了 Elliottt Zhang 在浙江大学学习期间关于人工智能、计算机系统、算法、数理基础、金融学、管理学与机器人方向的笔记与思考。
        </p>

        <form class="ka-search ka-glass" data-ka-search-form role="search">
          <label class="ka-sr-only" for="ka-home-search">搜索站内笔记</label>
          <input id="ka-home-search" type="search" placeholder="搜索 Agent、线性代数、Docker、微观经济学..." autocomplete="off">
          <button class="ka-button ka-button--primary" type="submit" data-magnetic>搜索</button>
        </form>

        <div class="ka-tags" aria-label="知识主题关键词">
          <a href="AI/agent/agent-basic-concepts/">AI Agent</a>
          <a href="CS/data/mining-massive-data/">Mining Massive Datasets</a>
          <a href="CS/algorithm/ads/">高级数据结构与算法分析</a>
          <a href="MATH/calculus/summary-of-calculus/">微积分方法</a>
          <a href="FINANCE/micro/">微观经济学</a>
          <a href="ROBOTICS/FTCTutorial/">FTC Robotics</a>
        </div>
      </div>

      <div class="ka-hero__map ka-glass ka-tilt" data-tilt aria-label="知识节点地图">
        <div class="ka-map-grid" aria-hidden="true"></div>
        <svg class="ka-map-lines" viewBox="0 0 520 420" role="img" aria-label="知识主题之间的连接">
          <path d="M92 94 C165 36 272 68 342 120 S456 230 410 318" />
          <path d="M92 94 C150 184 230 194 294 256 S360 348 410 318" />
          <path d="M204 336 C228 270 238 210 342 120" />
          <path d="M72 266 C158 220 196 318 294 256" />
        </svg>
        <a class="ka-node ka-node--ai" href="AI/agent/agent-basic-concepts/">Agent</a>
        <a class="ka-node ka-node--math" href="MATH/linear-algebra/summary-of-LA/">Math</a>
        <a class="ka-node ka-node--cs" href="CS/system/priciples/">System</a>
        <a class="ka-node ka-node--data" href="CS/data/mining-massive-data/">Data</a>
        <a class="ka-node ka-node--econ" href="FINANCE/micro/">Econ</a>
        <a class="ka-node ka-node--robot" href="ROBOTICS/FTCTutorial/">Robot</a>
        <div class="ka-orbit" aria-hidden="true"></div>
      </div>
    </header>

    <section class="ka-section ka-reveal" aria-labelledby="ka-focus-title">
      <div class="ka-section__head">
        <p class="ka-eyebrow">Current Focus</p>
        <h2 id="ka-focus-title">最近关注</h2>
      </div>
      <div class="ka-focus-grid">
        <article class="ka-card ka-glass ka-tilt" data-tilt>
          <div class="ka-card__meta">AI / Agent</div>
          <h3>智能体与检索增强</h3>
          <p>从智能体基础概念、RAG 到多智能体框架，逐步整理可组合的 Agent 系统认知。</p>
          <div class="ka-card__count">3 篇代表笔记</div>
          <ul>
            <li><a href="AI/agent/agent-basic-concepts/">智能体基本概念汇总</a></li>
            <li><a href="AI/agent/rag/">检索增强生成</a></li>
            <li><a href="AI/agent/multi-agent/">多智能体</a></li>
          </ul>
        </article>
        <article class="ka-card ka-glass ka-tilt" data-tilt>
          <div class="ka-card__meta">CS / Systems</div>
          <h3>开发工具与系统基础</h3>
          <p>覆盖 Shell、Docker、Git、WSL 与计算机组成原理，是日常开发和底层理解的操作台。</p>
          <div class="ka-card__count">6+ 篇持续更新</div>
          <ul>
            <li><a href="CS/tools/shell/">shell</a></li>
            <li><a href="CS/tools/docker/">Docker</a></li>
            <li><a href="CS/system/priciples/instructions/">汇编语言指令概述</a></li>
          </ul>
        </article>
        <article class="ka-card ka-glass ka-tilt" data-tilt>
          <div class="ka-card__meta">Math / Finance</div>
          <h3>数理方法与经济学模型</h3>
          <p>把微积分、线性代数、物理、电微宏观经济学放在同一张方法论地图里相互参照。</p>
          <div class="ka-card__count">10+ 篇课程笔记</div>
          <ul>
            <li><a href="MATH/calculus/summary-of-calculus/">微积分方法总结</a></li>
            <li><a href="MATH/linear-algebra/summary-of-LA/">线性代数方法总结</a></li>
            <li><a href="FINANCE/micro/price-theory/">价格理论</a></li>
          </ul>
        </article>
      </div>
    </section>

    <section class="ka-section ka-reveal" aria-labelledby="ka-featured-title">
      <div class="ka-section__head">
        <p class="ka-eyebrow">Featured Notes</p>
        <h2 id="ka-featured-title">精选笔记</h2>
      </div>
      <div class="ka-featured">
        <article class="ka-featured-main ka-glass ka-tilt" data-tilt>
          <span class="ka-pill">主推荐 / AI</span>
          <h3>Hello-Agents 教程核心概念与专业术语清单</h3>
          <p>
            一篇结构很完整的 Agent 总览，覆盖智能体发展、LLM 基础、经典范式、记忆检索、
            上下文工程、通信协议、Agentic RL 与自动化研究场景。
          </p>
          <dl class="ka-note-meta">
            <div><dt>阅读时间</dt><dd>约 45 分钟</dd></div>
            <div><dt>更新时间</dt><dd>2026-07-12</dd></div>
          </dl>
          <a class="ka-button ka-button--primary" href="AI/agent/agent-basic-concepts/" data-magnetic>进入笔记</a>
        </article>
        <div class="ka-note-grid">
          <article class="ka-note-card ka-glass ka-tilt" data-tilt>
            <span>开发工具</span>
            <h3>shell</h3>
            <p>终端、文件流、脚本、gcc 与常用命令的长篇工具笔记。</p>
            <footer><b>约 55 分钟</b><time>2026-07-09</time></footer>
            <a href="CS/tools/shell/">阅读</a>
          </article>
          <article class="ka-note-card ka-glass ka-tilt" data-tilt>
            <span>数学</span>
            <h3>微积分方法总结</h3>
            <p>极限、导数、中值定理、泰勒、不定积分与定积分的系统梳理。</p>
            <footer><b>约 30 分钟</b><time>2026-07-11</time></footer>
            <a href="MATH/calculus/summary-of-calculus/">阅读</a>
          </article>
          <article class="ka-note-card ka-glass ka-tilt" data-tilt>
            <span>Python</span>
            <h3>面向对象编程</h3>
            <p>围绕类、对象、封装、继承、多态和实践范式展开。</p>
            <footer><b>约 36 分钟</b><time>2026-07-09</time></footer>
            <a href="CS/pl/Python/py-oop/">阅读</a>
          </article>
          <article class="ka-note-card ka-glass ka-tilt" data-tilt>
            <span>物理</span>
            <h3>电磁学</h3>
            <p>从静电场到电磁波，包含公式、图示和课程复习框架。</p>
            <footer><b>约 34 分钟</b><time>2026-07-09</time></footer>
            <a href="MATH/physics/electricity/">阅读</a>
          </article>
          <article class="ka-note-card ka-glass ka-tilt" data-tilt>
            <span>算法</span>
            <h3>AVL 树和 Splay 树</h3>
            <p>高级数据结构课程中关于平衡树的核心概念与操作整理。</p>
            <footer><b>约 12 分钟</b><time>2026-07-09</time></footer>
            <a href="CS/algorithm/ads/avl-tree_splay-tree/">阅读</a>
          </article>
          <article class="ka-note-card ka-glass ka-tilt" data-tilt>
            <span>商科</span>
            <h3>不完全竞争市场</h3>
            <p>垄断、寡头、垄断竞争及市场结构对比分析。</p>
            <footer><b>约 11 分钟</b><time>2026-07-09</time></footer>
            <a href="FINANCE/micro/imperfectly-competitive-market/">阅读</a>
          </article>
        </div>
      </div>
    </section>

    <section class="ka-section ka-reveal" aria-labelledby="ka-paths-title">
      <div class="ka-section__head">
        <p class="ka-eyebrow">Reading Paths</p>
        <h2 id="ka-paths-title">阅读路径</h2>
      </div>
      <div class="ka-paths">
        <article class="ka-path ka-glass ka-tilt" data-tilt>
          <h3>构建 Agent 系统</h3>
          <ol>
            <li><a href="AI/basic/ML/">Machine Learning</a></li>
            <li><a href="AI/basic/DL/">Deep Learning</a></li>
            <li><a href="AI/agent/agent-basic-concepts/">智能体基本概念汇总</a></li>
            <li><a href="AI/agent/rag/">检索增强生成</a></li>
            <li><a href="AI/agent/multi-agent/">多智能体</a></li>
          </ol>
        </article>
        <article class="ka-path ka-glass ka-tilt" data-tilt>
          <h3>计算机基础到工程效率</h3>
          <ol>
            <li><a href="CS/system/priciples/chap1/">计算机系统概述</a></li>
            <li><a href="CS/system/priciples/instructions/">汇编语言指令概述</a></li>
            <li><a href="CS/tools/git-github/">Git & GitHub</a></li>
            <li><a href="CS/tools/shell/">shell</a></li>
            <li><a href="CS/tools/docker/">Docker</a></li>
          </ol>
        </article>
        <article class="ka-path ka-glass ka-tilt" data-tilt>
          <h3>数理模型与经济学</h3>
          <ol>
            <li><a href="MATH/calculus/knowledge-frame-of-calculus/">微积分知识框架</a></li>
            <li><a href="MATH/linear-algebra/knowledge-frame-of-LA/">线性代数知识框架</a></li>
            <li><a href="FINANCE/micro/price-theory/">价格理论</a></li>
            <li><a href="FINANCE/micro/theory-of-elasticity/">弹性理论</a></li>
            <li><a href="FINANCE/macro/gdp/">GDP 的含义与衡量</a></li>
          </ol>
        </article>
      </div>
    </section>

    <section class="ka-section ka-reveal" aria-labelledby="ka-index-title">
      <div class="ka-section__head ka-section__head--split">
        <div>
          <p class="ka-eyebrow">Notebook Index</p>
          <h2 id="ka-index-title">完整笔记索引</h2>
        </div>
        <label class="ka-index-search ka-glass">
          <span class="ka-sr-only">筛选完整笔记索引</span>
          <input type="search" data-ka-index-search placeholder="筛选主题、标题或关键词">
        </label>
      </div>
      <div class="ka-index ka-glass" data-ka-index aria-live="polite"></div>
    </section>

    <section class="ka-section ka-reveal" aria-labelledby="ka-updates-title">
      <div class="ka-section__head">
        <p class="ka-eyebrow">Recently Updated</p>
        <h2 id="ka-updates-title">最近更新</h2>
      </div>
      <div class="ka-timeline ka-glass">
        <a href="FINANCE/" class="ka-update"><time>2026-07-13</time><span>商科</span><b>分类封面更新</b></a>
        <a href="BOOK/" class="ka-update"><time>2026-07-13</time><span>阅读</span><b>阅读封面更新</b></a>
        <a href="WORK/" class="ka-update"><time>2026-07-13</time><span>工作</span><b>工作笔记封面更新</b></a>
        <a href="ROBOTICS/" class="ka-update"><time>2026-07-13</time><span>硬件</span><b>机器人分类封面更新</b></a>
        <a href="PROJECT/intellideploy/retrieval-recall/" class="ka-update"><time>2026-07-08</time><span>项目</span><b>检索与召回</b></a>
        <a href="AI/agent/rag/" class="ka-update"><time>2026-07-08</time><span>AI</span><b>检索增强生成</b></a>
        <a href="CS/data/db/review/" class="ka-update"><time>2026-06-23</time><span>数据库</span><b>复习笔记</b></a>
      </div>
    </section>
  </div>
</section>

<style>
/* Home-only Material layout override: let the atlas occupy the full page. */
body.ka-home-page .md-sidebar--primary,
body.ka-home-page .md-sidebar--secondary,
body.ka-home-page .md-content__button,
body.ka-home-page .md-source-file,
body.ka-home-page .md-typeset .md-source-file,
body.ka-home-page .md-typeset > .md-source-file,
body.ka-home-page .md-typeset > p:has(.twemoji),
body.ka-home-page .md-typeset > div[style*="margin-top"],
body:has(.ka-home) .md-sidebar--primary,
body:has(.ka-home) .md-sidebar--secondary,
body:has(.ka-home) .md-content__button,
body:has(.ka-home) .md-source-file,
body:has(.ka-home) .md-typeset .md-source-file,
body:has(.ka-home) .md-typeset > .md-source-file,
body:has(.ka-home) .md-typeset > p:has(.twemoji),
body:has(.ka-home) .md-typeset > div[style*="margin-top"] {
  display: none !important;
}

body.ka-home-page .md-main__inner,
body:has(.ka-home) .md-main__inner {
  max-width: none;
  margin: 0;
}

body.ka-home-page .md-content,
body.ka-home-page .md-content__inner,
body:has(.ka-home) .md-content,
body:has(.ka-home) .md-content__inner {
  margin: 0;
  padding: 0;
}

body.ka-home-page .md-content__inner::before,
body:has(.ka-home) .md-content__inner::before {
  display: none;
}

body.ka-home-page .md-typeset,
body:has(.ka-home) .md-typeset {
  width: 100%;
  max-width: none;
}

/* Knowledge Atlas home page. Everything is scoped under .ka-home. */
.md-typeset .ka-home {
  --ka-bg: #050814;
  --ka-panel: rgba(13, 20, 38, 0.58);
  --ka-panel-strong: rgba(17, 27, 52, 0.72);
  --ka-text: #edf7ff;
  --ka-muted: #9eb1c8;
  --ka-soft: #6f829d;
  --ka-cyan: #00f0ff;
  --ka-violet: #8a2be2;
  --ka-mint: #64ffda;
  --ka-border: rgba(255, 255, 255, 0.12);
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: min(100vw, 100%);
  margin: -1.2rem auto 0;
  padding: clamp(2rem, 4vw, 4.2rem) clamp(1rem, 4vw, 2rem) 4rem;
  color: var(--ka-text);
  background:
    linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px),
    radial-gradient(circle at 20% 10%, rgba(0, 240, 255, 0.12), transparent 34rem),
    radial-gradient(circle at 80% 0%, rgba(138, 43, 226, 0.12), transparent 32rem),
    linear-gradient(135deg, #040713 0%, #07111f 45%, #090718 100%);
  background-size: 48px 48px, 48px 48px, auto, auto, auto;
  border-radius: 0 0 28px 28px;
}

.md-typeset .ka-home *,
.md-typeset .ka-home *::before,
.md-typeset .ka-home *::after {
  box-sizing: border-box;
}

.md-typeset .ka-home a {
  color: inherit;
  text-decoration: none;
}

.md-typeset .ka-home a::after {
  display: none;
}

.ka-shell {
  position: relative;
  z-index: 1;
  width: min(1180px, 100%);
  margin: 0 auto;
}

.ka-ambient {
  position: absolute;
  z-index: -2;
  width: 34rem;
  height: 34rem;
  border-radius: 999px;
  filter: blur(120px);
  opacity: 0.24;
  transform: translate3d(0, 0, 0);
  will-change: transform, opacity;
  pointer-events: none;
}

.ka-ambient--cyan {
  top: 2rem;
  left: -8rem;
  background: #00f0ff;
  animation: ka-breathe-cyan 18s ease-in-out infinite alternate;
}

.ka-ambient--violet {
  right: -10rem;
  top: 24rem;
  background: #8a2be2;
  animation: ka-breathe-violet 22s ease-in-out infinite alternate;
}

.ka-noise {
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: 0.18;
  pointer-events: none;
  background-image:
    radial-gradient(circle at 18% 24%, rgba(255,255,255,0.28) 0 1px, transparent 1.5px),
    radial-gradient(circle at 76% 42%, rgba(0,240,255,0.24) 0 1px, transparent 1.5px),
    radial-gradient(circle at 56% 76%, rgba(138,43,226,0.22) 0 1px, transparent 1.5px);
  background-size: 180px 180px, 240px 240px, 220px 220px;
}

@keyframes ka-breathe-cyan {
  from { transform: translate3d(0, 0, 0) scale(0.92); opacity: 0.18; }
  to { transform: translate3d(9rem, 5rem, 0) scale(1.08); opacity: 0.28; }
}

@keyframes ka-breathe-violet {
  from { transform: translate3d(0, 0, 0) scale(1); opacity: 0.16; }
  to { transform: translate3d(-7rem, -4rem, 0) scale(1.12); opacity: 0.26; }
}

.ka-hero {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(320px, 0.78fr);
  gap: clamp(1.2rem, 4vw, 3rem);
  align-items: center;
  min-height: min(720px, calc(100vh - 7rem));
  padding-bottom: clamp(2rem, 5vw, 4rem);
}

.ka-kicker,
.ka-eyebrow,
.ka-card__meta,
.ka-pill {
  margin: 0 0 0.6rem;
  color: var(--ka-mint);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0;
  text-transform: uppercase;
}

.md-typeset .ka-hero h1 {
  margin: 0;
  color: var(--ka-text);
  font-size: clamp(3.2rem, 9vw, 6.8rem);
  line-height: 0.88;
  letter-spacing: 0;
  text-shadow: 0 0 32px rgba(0, 240, 255, 0.18);
}

.ka-hero__lead {
  margin: 1.2rem 0 0;
  color: #ffffff;
  font-size: clamp(1.45rem, 4vw, 2.35rem);
  font-weight: 700;
  line-height: 1.25;
}

.ka-hero__intro {
  max-width: 42rem;
  margin: 1rem 0 1.4rem;
  color: var(--ka-muted);
  font-size: 0.95rem;
  line-height: 1.85;
}

.ka-glass {
  position: relative;
  background: var(--ka-panel);
  border: 1px solid transparent;
  border-radius: 18px;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.08),
    inset 0 -24px 60px rgba(0, 240, 255, 0.025),
    0 18px 70px rgba(0, 0, 0, 0.28);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
}

.ka-glass::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 0;
  padding: 1px;
  border-radius: inherit;
  background:
    radial-gradient(circle at var(--glow-x, 50%) var(--glow-y, 0%), rgba(0, 240, 255, 0.58), transparent 22%),
    linear-gradient(135deg, rgba(255,255,255,0.28), rgba(0,240,255,0.18), rgba(138,43,226,0.22), rgba(255,255,255,0.06));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.ka-glass > * {
  position: relative;
  z-index: 1;
}

.ka-tilt {
  --tilt-x: 0deg;
  --tilt-y: 0deg;
  --lift: 0px;
  transform: perspective(900px) rotateX(var(--tilt-x)) rotateY(var(--tilt-y)) translate3d(0, var(--lift), 0);
  transform-style: preserve-3d;
  transition: transform 180ms ease, background-color 180ms ease, box-shadow 180ms ease;
  will-change: transform;
}

.ka-tilt::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 0;
  border-radius: inherit;
  opacity: 0;
  background: radial-gradient(circle at var(--glow-x, 50%) var(--glow-y, 50%), rgba(0, 240, 255, 0.14), transparent 34%);
  transition: opacity 180ms ease;
  pointer-events: none;
}

.ka-tilt:hover {
  --lift: -4px;
  background: rgba(18, 30, 58, 0.66);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.11),
    0 22px 80px rgba(0, 0, 0, 0.34),
    0 0 38px rgba(0, 240, 255, 0.08);
}

.ka-tilt:hover::after {
  opacity: 1;
}

.ka-search {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  max-width: 42rem;
  padding: 0.45rem;
  border-radius: 16px;
}

.ka-search input,
.ka-index-search input {
  width: 100%;
  min-width: 0;
  color: var(--ka-text);
  background: transparent;
  border: 0;
  outline: 0;
  font: inherit;
}

.ka-search input {
  padding: 0.6rem 0.7rem;
}

.ka-search input::placeholder,
.ka-index-search input::placeholder {
  color: rgba(237, 247, 255, 0.52);
}

.ka-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.2rem;
  padding: 0.56rem 1rem;
  color: #03111a;
  font-weight: 800;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  background: linear-gradient(135deg, var(--ka-cyan), var(--ka-mint));
  box-shadow: 0 0 28px rgba(0, 240, 255, 0.18);
  transition: transform 180ms ease, box-shadow 180ms ease, filter 180ms ease;
}

.ka-button:hover,
.ka-button:focus-visible {
  color: #03111a;
  filter: saturate(1.12);
  box-shadow: 0 0 34px rgba(0, 240, 255, 0.28);
}

.ka-button:focus-visible,
.ka-home a:focus-visible,
.ka-home button:focus-visible,
.ka-home input:focus-visible,
.ka-home summary:focus-visible {
  outline: 2px solid var(--ka-cyan);
  outline-offset: 3px;
}

.ka-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  max-width: 46rem;
  margin-top: 1rem;
}

.ka-tags a {
  padding: 0.38rem 0.7rem;
  color: #dffaff;
  font-size: 0.72rem;
  border: 1px solid rgba(0, 240, 255, 0.22);
  border-radius: 999px;
  background: rgba(0, 240, 255, 0.07);
  transition: border-color 180ms ease, background-color 180ms ease, transform 180ms ease;
}

.ka-tags a:hover,
.ka-tags a:focus-visible {
  border-color: rgba(100, 255, 218, 0.58);
  background: rgba(0, 240, 255, 0.13);
  transform: translateY(-2px);
}

.ka-hero__map {
  min-height: 420px;
  overflow: hidden;
  border-radius: 22px;
}

.ka-map-grid {
  position: absolute;
  inset: 0;
  z-index: 0;
  background:
    linear-gradient(rgba(0,240,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(138,43,226,0.06) 1px, transparent 1px);
  background-size: 34px 34px;
  mask-image: radial-gradient(circle at 50% 46%, #000, transparent 74%);
  pointer-events: none;
}

.ka-map-lines {
  display: none;
}

.ka-map-lines path {
  stroke-dasharray: 9 12;
  animation: ka-dash 18s linear infinite;
}

@keyframes ka-dash {
  to { stroke-dashoffset: -180; }
}

.ka-node {
  position: absolute;
  z-index: 3;
  display: grid;
  place-items: center;
  width: 5rem;
  height: 5rem;
  top: var(--node-y);
  left: var(--node-x);
  color: #f7fdff;
  font-size: 0.74rem;
  font-weight: 800;
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 999px;
  background:
    radial-gradient(circle at 35% 25%, rgba(255,255,255,0.22), transparent 26%),
    linear-gradient(135deg, rgba(0,240,255,0.2), rgba(138,43,226,0.2));
  box-shadow: 0 0 34px rgba(0,240,255,0.16);
  transform: translate(-50%, -50%);
  transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
}

.ka-node:hover,
.ka-node:focus-visible {
  transform: translate(-50%, calc(-50% - 4px)) scale(1.03);
  border-color: rgba(100,255,218,0.68);
  box-shadow: 0 0 42px rgba(0,240,255,0.24);
}

.ka-node--ai { --node-x: 31%; --node-y: 24%; }
.ka-node--math { --node-x: 68%; --node-y: 31%; }
.ka-node--cs { --node-x: 52%; --node-y: 51%; }
.ka-node--data { --node-x: 30%; --node-y: 64%; }
.ka-node--econ { --node-x: 66%; --node-y: 73%; }
.ka-node--robot { --node-x: 34%; --node-y: 83%; }

.ka-orbit {
  position: absolute;
  inset: 21% 14% 17% 14%;
  z-index: 1;
  border: 1px solid rgba(138,43,226,0.22);
  border-radius: 50%;
  transform: rotate(-12deg);
  animation: ka-orbit 28s linear infinite;
  pointer-events: none;
}

@keyframes ka-orbit {
  to { transform: rotate(348deg); }
}

.ka-section {
  margin-top: clamp(2rem, 6vw, 4.5rem);
}

.ka-section__head {
  margin-bottom: 1rem;
}

.ka-section__head--split {
  display: flex;
  gap: 1rem;
  align-items: end;
  justify-content: space-between;
}

.md-typeset .ka-section h2 {
  margin: 0;
  color: var(--ka-text);
  font-size: clamp(1.55rem, 3vw, 2.3rem);
  line-height: 1.2;
}

.ka-focus-grid,
.ka-paths {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

.ka-card,
.ka-path,
.ka-timeline,
.ka-index {
  padding: 1rem;
}

.md-typeset .ka-card h3,
.md-typeset .ka-path h3,
.md-typeset .ka-note-card h3,
.md-typeset .ka-featured-main h3 {
  margin: 0.2rem 0 0.55rem;
  color: #f7fbff;
  font-size: 1.08rem;
  line-height: 1.3;
}

.ka-card p,
.ka-featured-main p,
.ka-note-card p {
  margin: 0 0 0.8rem;
  color: var(--ka-muted);
  line-height: 1.7;
}

.ka-card__count {
  display: inline-flex;
  margin-bottom: 0.5rem;
  padding: 0.18rem 0.55rem;
  color: #b9faff;
  font-size: 0.68rem;
  border-radius: 999px;
  background: rgba(0,240,255,0.08);
}

.ka-card ul {
  margin: 0;
  padding-left: 1rem;
}

.ka-card li {
  margin: 0.35rem 0;
  color: var(--ka-muted);
}

.ka-card a,
.ka-path a,
.ka-note-card a,
.ka-update {
  color: #dffaff;
  transition: color 160ms ease, opacity 160ms ease;
}

.ka-card a:hover,
.ka-path a:hover,
.ka-note-card a:hover,
.ka-update:hover {
  color: var(--ka-mint);
}

.ka-featured {
  display: grid;
  grid-template-columns: minmax(300px, 0.78fr) minmax(0, 1.22fr);
  gap: 1rem;
}

.ka-featured-main {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height: 100%;
  padding: 1.2rem;
  background:
    radial-gradient(circle at 12% 0%, rgba(0,240,255,0.14), transparent 42%),
    rgba(13, 20, 38, 0.62);
}

.ka-featured-main .ka-button {
  margin-top: auto;
}

.ka-note-meta {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.8rem;
  width: 100%;
  margin: 0.4rem 0 1.2rem;
}

.ka-note-meta div {
  padding: 0.65rem;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  background: rgba(255,255,255,0.035);
}

.ka-note-meta dt {
  color: var(--ka-soft);
  font-size: 0.66rem;
}

.ka-note-meta dd {
  margin: 0.1rem 0 0;
  color: var(--ka-text);
  font-weight: 800;
}

.ka-note-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.ka-note-card {
  display: flex;
  flex-direction: column;
  min-height: 13rem;
  padding: 1rem;
}

.ka-note-card span {
  color: var(--ka-mint);
  font-size: 0.68rem;
  font-weight: 800;
}

.ka-note-card footer {
  display: flex;
  gap: 0.6rem;
  justify-content: space-between;
  margin-top: auto;
  color: var(--ka-soft);
  font-size: 0.68rem;
}

.ka-note-card > a {
  align-self: flex-start;
  margin-top: 0.55rem;
  font-weight: 800;
}

.ka-path ol {
  margin: 0.6rem 0 0;
  padding: 0;
  list-style: none;
  counter-reset: path;
}

.ka-path li {
  position: relative;
  min-height: 2.1rem;
  margin: 0;
  padding: 0 0 0.95rem 2rem;
  color: var(--ka-muted);
  counter-increment: path;
}

.ka-path li::before {
  content: counter(path);
  position: absolute;
  left: 0;
  top: 0;
  display: grid;
  place-items: center;
  width: 1.25rem;
  height: 1.25rem;
  color: #03111a;
  font-size: 0.62rem;
  font-weight: 900;
  border-radius: 999px;
  background: var(--ka-cyan);
  box-shadow: 0 0 18px rgba(0,240,255,0.28);
}

.ka-path li::after {
  content: "";
  position: absolute;
  left: 0.6rem;
  top: 1.35rem;
  bottom: 0.08rem;
  width: 1px;
  background: linear-gradient(var(--ka-cyan), rgba(138,43,226,0.12));
}

.ka-path li:last-child {
  padding-bottom: 0;
}

.ka-path li:last-child::after {
  display: none;
}

.ka-index-search {
  width: min(24rem, 100%);
  padding: 0.55rem 0.75rem;
  border-radius: 999px;
}

.ka-index {
  display: grid;
  gap: 0.7rem;
}

.ka-index details {
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  background: rgba(255,255,255,0.03);
  overflow: hidden;
}

.ka-index summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.8rem;
  padding: 0.78rem 0.9rem;
  color: var(--ka-text);
  font-weight: 850;
  cursor: pointer;
  list-style: none;
}

.ka-index summary::-webkit-details-marker {
  display: none;
}

.ka-index summary span {
  color: var(--ka-soft);
  font-size: 0.66rem;
  font-weight: 800;
}

.ka-index ul {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.45rem 0.75rem;
  margin: 0;
  padding: 0 0.9rem 0.9rem;
  list-style: none;
}

.ka-index li a {
  display: block;
  min-height: 100%;
  padding: 0.6rem 0.7rem;
  border: 1px solid rgba(255,255,255,0.07);
  border-radius: 12px;
  background: rgba(5,8,20,0.28);
  transition: border-color 160ms ease, background-color 160ms ease, transform 160ms ease;
}

.ka-index li a:hover,
.ka-index li a:focus-visible {
  color: var(--ka-text);
  border-color: rgba(0,240,255,0.28);
  background: rgba(0,240,255,0.07);
  transform: translateY(-2px);
}

.ka-index li b {
  display: block;
  color: #f4fbff;
  font-size: 0.78rem;
}

.ka-index li small {
  display: block;
  margin-top: 0.18rem;
  color: var(--ka-soft);
  font-size: 0.62rem;
}

.ka-empty {
  margin: 0;
  color: var(--ka-muted);
}

.ka-timeline {
  display: grid;
  gap: 0.2rem;
}

.ka-update {
  position: relative;
  display: grid;
  grid-template-columns: 7rem 5.5rem 1fr;
  gap: 0.8rem;
  align-items: center;
  padding: 0.72rem 0.5rem 0.72rem 1.25rem;
  border-radius: 12px;
}

.ka-update::before {
  content: "";
  position: absolute;
  left: 0.38rem;
  top: 50%;
  width: 0.42rem;
  height: 0.42rem;
  border-radius: 50%;
  background: var(--ka-cyan);
  box-shadow: 0 0 14px rgba(0,240,255,0.6);
  transform: translateY(-50%);
}

.ka-update:hover {
  background: rgba(0,240,255,0.06);
}

.ka-update time,
.ka-update span {
  color: var(--ka-soft);
  font-size: 0.66rem;
  font-weight: 800;
}

.ka-update b {
  color: var(--ka-text);
  font-size: 0.78rem;
}

.ka-reveal {
  opacity: 0;
  transform: translateY(22px);
}

.ka-reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 620ms ease, transform 620ms ease;
  transition-delay: var(--reveal-delay, 0ms);
}

.ka-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

@supports not ((backdrop-filter: blur(12px)) or (-webkit-backdrop-filter: blur(12px))) {
  .ka-glass {
    background: rgba(12, 20, 39, 0.9);
  }
}

@media (max-width: 960px) {
  .md-typeset .ka-home {
    padding-top: 2rem;
  }

  .ka-hero,
  .ka-featured {
    grid-template-columns: 1fr;
  }

  .ka-hero {
    min-height: 0;
  }

  .ka-hero__map {
    min-height: 340px;
  }

  .ka-focus-grid,
  .ka-paths {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 720px) {
  .md-typeset .ka-home {
    margin-top: -0.6rem;
    padding-inline: 0.75rem;
  }

  .ka-ambient {
    width: 18rem;
    height: 18rem;
    opacity: 0.14;
    filter: blur(90px);
  }

  .ka-search,
  .ka-section__head--split,
  .ka-note-meta,
  .ka-update {
    grid-template-columns: 1fr;
  }

  .ka-search,
  .ka-section__head--split {
    display: grid;
    align-items: stretch;
  }

  .ka-note-grid,
  .ka-index ul {
    grid-template-columns: 1fr;
  }

  .ka-hero__map {
    min-height: 280px;
  }

  .ka-node {
    width: 4.1rem;
    height: 4.1rem;
    font-size: 0.66rem;
  }

  .ka-update {
    gap: 0.2rem;
    padding-left: 1.1rem;
  }
}

@media (hover: none), (pointer: coarse) {
  .ka-tilt {
    transform: none !important;
    transition: background-color 180ms ease, box-shadow 180ms ease;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ka-ambient,
  .ka-map-lines path,
  .ka-orbit {
    animation: none !important;
  }

  .ka-reveal,
  .ka-reveal.is-visible,
  .ka-tilt,
  .ka-button,
  .ka-tags a,
  .ka-index li a {
    opacity: 1;
    transform: none !important;
    transition: none !important;
  }
}
</style>

<script>
(() => {
  const noteGroups = [
    {
      title: "人工智能",
      notes: [
        ["人工智能封面", "AI/", "AI / overview"],
        ["Artificial Neural Network", "AI/basic/ANN/", "AI basic"],
        ["Machine Learning", "AI/basic/ML/", "AI basic"],
        ["Deep Learning", "AI/basic/DL/", "AI basic"],
        ["Turing", "AI/basic/Turing/", "AI basic"],
        ["智能体基本概念汇总", "AI/agent/agent-basic-concepts/", "Agent complete"],
        ["检索增强生成", "AI/agent/rag/", "RAG"],
        ["多智能体", "AI/agent/multi-agent/", "Multi-agent"]
      ]
    },
    {
      title: "开发工具与工程实践",
      notes: [
        ["开发封面", "CS/", "CS overview"],
        ["项目组织", "CS/develop/project/", "engineering"],
        ["Git 规范", "CS/develop/git/", "engineering"],
        ["编程风格", "CS/develop/programming/", "engineering"],
        ["shell", "CS/tools/shell/", "tools complete"],
        ["Git & GitHub", "CS/tools/git-github/", "tools"],
        ["Docker", "CS/tools/docker/", "tools"],
        ["Markdown 基础", "CS/tools/markdown-basics/", "markdown"],
        ["Markdown 进阶", "CS/tools/markdown-advanced/", "markdown"],
        ["Markdown 与 Obsidian", "CS/tools/markdown-obsidian/", "markdown"],
        ["LaTeX", "CS/tools/LaTeX/", "tools"],
        ["WSL 备忘录", "CS/tools/linux/wsl-record/", "linux"],
        ["Windows 配置", "CS/tools/windows/win-note/", "windows"]
      ]
    },
    {
      title: "编程语言",
      notes: [
        ["Python 学习笔记", "CS/pl/Python/", "python"],
        ["Python 基础语法", "CS/pl/Python/py-basic-grammar/", "python"],
        ["Python 数据容器", "CS/pl/Python/py-sequence/", "python"],
        ["Python 面向对象编程", "CS/pl/Python/py-oop/", "python complete"],
        ["Python 文件基础", "CS/pl/Python/file-basic/", "python"],
        ["Python 文件进阶", "CS/pl/Python/file-advance/", "python"],
        ["Python 标准库积累", "CS/pl/Python/modules/", "python"],
        ["网络数据采集", "CS/pl/Python/web-scraping/", "python"],
        ["C 数据类型", "CS/pl/C/01-data-types/", "C"],
        ["C 运算符和表达式", "CS/pl/C/02-operators/", "C"],
        ["C 函数", "CS/pl/C/04-functions/", "C"],
        ["C 动态内存与链表", "CS/pl/C/08-dynamic-memory/", "C complete"]
      ]
    },
    {
      title: "算法、数据与系统",
      notes: [
        ["算法分析", "CS/algorithm/fds/chap2/", "FDS"],
        ["Tree", "CS/algorithm/fds/chap4/", "FDS"],
        ["Graph", "CS/algorithm/fds/graph/", "FDS"],
        ["AVL 树和 Splay 树", "CS/algorithm/ads/avl-tree_splay-tree/", "ADS"],
        ["倒排表", "CS/algorithm/ads/inverted_file_index/", "ADS"],
        ["动态规划", "CS/algorithm/ads/dynamic_programming/", "ADS"],
        ["Map Reduce and Spark", "CS/data/mining-massive-data/mapreduce-and-spark/", "data"],
        ["Frequent Itemsets Mining", "CS/data/mining-massive-data/frequent-itemsets-mining/", "data"],
        ["Locality Sensitive Hashing", "CS/data/mining-massive-data/lsh/", "data"],
        ["数据库复习笔记", "CS/data/db/review/", "database"],
        ["SQL 总结", "CS/data/db/sql-summary/", "database"],
        ["计算机系统概述", "CS/system/priciples/chap1/", "system"],
        ["汇编语言指令概述", "CS/system/priciples/instructions/", "system"],
        ["数的表示", "CS/system/priciples/number_representation/", "system"],
        ["数字逻辑设计 Chapter 2", "CS/system/digital-design/chap2/", "digital design"]
      ]
    },
    {
      title: "数理基础",
      notes: [
        ["数理封面", "MATH/", "math overview"],
        ["微积分知识框架", "MATH/calculus/knowledge-frame-of-calculus/", "calculus"],
        ["微积分方法总结", "MATH/calculus/summary-of-calculus/", "calculus complete"],
        ["级数", "MATH/calculus/series-sdk/", "calculus"],
        ["多元函数微分学", "MATH/calculus/differential-calculus-of-multivariate-function/", "calculus"],
        ["矢量代数与空间解析几何", "MATH/calculus/vector-algebra/", "calculus"],
        ["线性代数知识框架", "MATH/linear-algebra/knowledge-frame-of-LA/", "linear algebra"],
        ["线性代数方法总结", "MATH/linear-algebra/summary-of-LA/", "linear algebra"],
        ["命题逻辑和证明", "MATH/discrete/chap-1/", "discrete math"],
        ["动力学", "MATH/physics/dynamics-motion/", "physics"],
        ["电磁学", "MATH/physics/electricity/", "physics complete"],
        ["电磁学公式物理量总结", "MATH/physics/electricity-summary/", "physics"]
      ]
    },
    {
      title: "商科、项目与机器人",
      notes: [
        ["商科封面", "FINANCE/", "finance overview"],
        ["价格理论", "FINANCE/micro/price-theory/", "microeconomics"],
        ["弹性理论", "FINANCE/micro/theory-of-elasticity/", "microeconomics"],
        ["消费者行为理论", "FINANCE/micro/consumer-behavior-theory/", "microeconomics"],
        ["生产和成本理论", "FINANCE/micro/production-and-cost-theory/", "microeconomics"],
        ["不完全竞争市场", "FINANCE/micro/imperfectly-competitive-market/", "microeconomics"],
        ["GDP 的含义与衡量", "FINANCE/macro/gdp/", "macroeconomics"],
        ["货币市场", "FINANCE/macro/currency/", "macroeconomics"],
        ["检索与召回", "PROJECT/intellideploy/retrieval-recall/", "project"],
        ["FTC 程序入门", "ROBOTICS/FTCTutorial/1.1程序入门/", "robotics"],
        ["FTC 遥测系统使用指南", "ROBOTICS/FTCTutorial/2.2FTC遥测系统使用指南/", "robotics"],
        ["PedroPathing", "ROBOTICS/FTCTutorial/PedroPathing/", "robotics"],
        ["PID", "ROBOTICS/FTCTutorial/PID/", "robotics"]
      ]
    }
  ];

  const state = {
    cleanup: null
  };

  const motionAllowed = () =>
    window.matchMedia("(prefers-reduced-motion: no-preference)").matches &&
    window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  const renderIndex = (root, query = "") => {
    const term = query.trim().toLowerCase();
    const groups = noteGroups
      .map((group) => {
        const notes = group.notes.filter(([title, , tags]) => {
          const haystack = `${group.title} ${title} ${tags}`.toLowerCase();
          return !term || haystack.includes(term);
        });
        return { title: group.title, notes };
      })
      .filter((group) => group.notes.length);

    if (!groups.length) {
      root.innerHTML = '<p class="ka-empty">没有匹配的笔记。</p>';
      return;
    }

    root.innerHTML = groups.map((group, groupIndex) => `
      <details ${groupIndex < 2 || term ? "open" : ""}>
        <summary>${group.title}<span>${group.notes.length} 篇</span></summary>
        <ul>
          ${group.notes.map(([title, href, tags]) => `
            <li><a href="${href}"><b>${title}</b><small>${tags}</small></a></li>
          `).join("")}
        </ul>
      </details>
    `).join("");
  };

  const initHome = () => {
    const home = document.querySelector(".ka-home");
    document.body.classList.toggle("ka-home-page", Boolean(home));
    if (!home) {
      if (state.cleanup) state.cleanup();
      return;
    }

    if (state.cleanup) state.cleanup();

    const cleanupTasks = [];
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    const indexRoot = home.querySelector("[data-ka-index]");
    const indexSearch = home.querySelector("[data-ka-index-search]");
    if (indexRoot) {
      renderIndex(indexRoot);
      if (indexSearch) {
        const onInput = () => renderIndex(indexRoot, indexSearch.value);
        indexSearch.addEventListener("input", onInput);
        cleanupTasks.push(() => indexSearch.removeEventListener("input", onInput));
      }
    }

    const searchForm = home.querySelector("[data-ka-search-form]");
    if (searchForm) {
      const onSubmit = (event) => {
        event.preventDefault();
        const field = searchForm.querySelector("input");
        const query = field ? field.value.trim() : "";
        const toggle = document.querySelector("[data-md-toggle='search']");
        if (toggle) toggle.checked = true;
        window.setTimeout(() => {
          const mdSearch = document.querySelector(".md-search__input");
          if (!mdSearch) return;
          mdSearch.focus();
          if (query) {
            mdSearch.value = query;
            mdSearch.dispatchEvent(new Event("input", { bubbles: true }));
          }
        }, 40);
      };
      searchForm.addEventListener("submit", onSubmit);
      cleanupTasks.push(() => searchForm.removeEventListener("submit", onSubmit));
    }

    const revealItems = Array.from(home.querySelectorAll(".ka-reveal, .ka-card, .ka-note-card, .ka-path"));
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealItems.forEach((el) => el.classList.add("is-visible"));
    } else {
      revealItems.forEach((el, index) => {
        el.style.setProperty("--reveal-delay", `${Math.min(index % 6, 5) * 55}ms`);
      });
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
      revealItems.forEach((el) => observer.observe(el));
      cleanupTasks.push(() => observer.disconnect());
    }

    if (motionAllowed()) {
      const tiltCards = Array.from(home.querySelectorAll("[data-tilt]"));
      tiltCards.forEach((card) => {
        let raf = 0;
        let next = null;

        const applyTilt = () => {
          if (!next) return;
          const rect = card.getBoundingClientRect();
          const px = (next.x - rect.left) / rect.width;
          const py = (next.y - rect.top) / rect.height;
          const rotateY = (px - 0.5) * 8;
          const rotateX = (0.5 - py) * 8;
          card.style.setProperty("--tilt-x", `${rotateX.toFixed(2)}deg`);
          card.style.setProperty("--tilt-y", `${rotateY.toFixed(2)}deg`);
          card.style.setProperty("--glow-x", `${(px * 100).toFixed(1)}%`);
          card.style.setProperty("--glow-y", `${(py * 100).toFixed(1)}%`);
          raf = 0;
        };

        const onMove = (event) => {
          next = { x: event.clientX, y: event.clientY };
          if (!raf) raf = window.requestAnimationFrame(applyTilt);
        };

        const onLeave = () => {
          if (raf) window.cancelAnimationFrame(raf);
          raf = 0;
          next = null;
          card.style.setProperty("--tilt-x", "0deg");
          card.style.setProperty("--tilt-y", "0deg");
          card.style.setProperty("--glow-x", "50%");
          card.style.setProperty("--glow-y", "0%");
        };

        card.addEventListener("mousemove", onMove);
        card.addEventListener("mouseleave", onLeave);
        cleanupTasks.push(() => {
          card.removeEventListener("mousemove", onMove);
          card.removeEventListener("mouseleave", onLeave);
          if (raf) window.cancelAnimationFrame(raf);
        });
      });

      const magneticButtons = Array.from(home.querySelectorAll("[data-magnetic]"));
      magneticButtons.forEach((button) => {
        let raf = 0;
        let point = null;

        const applyMagnet = () => {
          if (!point) return;
          const rect = button.getBoundingClientRect();
          const dx = point.x - (rect.left + rect.width / 2);
          const dy = point.y - (rect.top + rect.height / 2);
          const x = Math.max(-8, Math.min(8, dx * 0.16));
          const y = Math.max(-6, Math.min(6, dy * 0.18));
          button.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, 0) scale(1.025)`;
          raf = 0;
        };

        const onMove = (event) => {
          point = { x: event.clientX, y: event.clientY };
          if (!raf) raf = window.requestAnimationFrame(applyMagnet);
        };

        const onLeave = () => {
          if (raf) window.cancelAnimationFrame(raf);
          raf = 0;
          point = null;
          button.style.transform = "";
        };

        button.addEventListener("mousemove", onMove);
        button.addEventListener("mouseleave", onLeave);
        button.addEventListener("blur", onLeave);
        cleanupTasks.push(() => {
          button.removeEventListener("mousemove", onMove);
          button.removeEventListener("mouseleave", onLeave);
          button.removeEventListener("blur", onLeave);
          if (raf) window.cancelAnimationFrame(raf);
        });
      });
    }

    state.cleanup = () => {
      cleanupTasks.splice(0).forEach((task) => task());
      state.cleanup = null;
    };
  };

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(initHome);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initHome, { once: true });
  } else {
    initHome();
  }
})();
</script>
