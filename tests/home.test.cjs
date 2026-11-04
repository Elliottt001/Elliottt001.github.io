// Run with: node tests/home.test.cjs
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const path = require("node:path");
const read = (name) => fs.readFileSync(path.join(__dirname, "../assets/mkdocs/javascripts", name), "utf8");

async function checkMathStartup() {
  let hasMath = false;
  let isTypeset = false;
  let loader = null;
  let subscriptions = [];
  const calls = [];
  const content = { querySelector: (selector) => selector === "mjx-container" ? isTypeset : hasMath };
  const document = {
    querySelector: (selector) => selector === ".arithmatex" ? hasMath :
      selector === ".md-content" ? content : loader,
    createElement: () => ({ dataset: {} }),
    head: { appendChild: (script) => { loader = script; } },
  };
  const context = { document, console, window: {}, document$: {
    subscribe: (callback) => { subscriptions.push(callback); callback(); },
  } };
  vm.createContext(context);
  vm.runInContext(read("mathjax.js"), context);
  assert.equal(loader, null, "Pages without formulas must not load MathJax");
  hasMath = true;
  subscriptions.forEach((callback) => callback());
  assert.match(loader.src, /mathjax@3/);
  const firstLoader = loader;
  subscriptions.forEach((callback) => callback());
  assert.equal(loader, firstLoader, "Navigation must not load a second engine");

  let ready;
  const math = context.window.MathJax;
  context.MathJax = math;
  math.startup.defaultReady = () => calls.push("defaultReady");
  math.startup.promise = new Promise((resolve) => { ready = resolve; });
  math.typesetClear = () => calls.push("clear");
  math.texReset = () => calls.push("reset");
  math.typesetPromise = () => { calls.push("typeset"); return Promise.resolve(); };
  math.startup.ready();
  assert.deepEqual(calls, ["defaultReady"], "Do not typeset before startup resolves");
  ready();
  await math.startup.promise;
  assert.deepEqual(calls, ["defaultReady", "clear", "reset", "typeset"]);
  isTypeset = true;
  subscriptions.forEach((callback) => callback());
  assert.equal(calls.length, 4, "Do not typeset already rendered math or its assistive MathML");
  hasMath = false;
  subscriptions.forEach((callback) => callback());
  assert.equal(calls.length, 4, "Returning home must not typeset empty content");
}

function checkSearch() {
  const calls = [];
  const toggle = { checked: false, dispatchEvent: (event) => calls.push(event.type) };
  const search = { value: "stale query", dispatchEvent: (event) => calls.push(event.type), focus: () => calls.push("focus") };
  const input = { value: "  Agent  " };
  const form = { querySelector: () => input };
  const document = { querySelector: (selector) => selector === "[data-home-search]" ? form :
    selector === ".md-search__input" ? search : toggle };
  const context = { document, Event: class { constructor(type) { this.type = type; } },
    document$: { subscribe: (callback) => { callback(); callback(); } } };
  vm.runInNewContext(read("home.js"), context);
  form.onsubmit({ preventDefault() {} });
  assert.equal(toggle.checked, true);
  assert.equal(search.value, "Agent");
  assert.deepEqual(calls, ["change", "input", "focus"]);
  input.value = " ";
  form.onsubmit({ preventDefault() {} });
  assert.equal(search.value, "", "An empty search must clear the previous query");
}

checkMathStartup().then(() => {
  checkSearch();
  console.log("Home search and delayed MathJax startup checks passed.");
}).catch((error) => { console.error(error); process.exitCode = 1; });
