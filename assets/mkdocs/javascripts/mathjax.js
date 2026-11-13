window.MathJax = {
    startup: {
      ready() {
        MathJax.startup.defaultReady();
        // Subscribe only after the engine and its initial typesetting are ready.
        MathJax.startup.promise.then(() => {
          if (typeof document$ === "undefined") return;
          document$.subscribe(() => {
            const content = document.querySelector(".md-content");
            if (!content || !content.querySelector(".arithmatex") ||
                content.querySelector("mjx-container")) return;
            MathJax.typesetClear();
            MathJax.texReset();
            MathJax.typesetPromise([content]).catch((error) => {
              console.error("MathJax typesetting failed:", error);
            });
          });
        });
      }
    },
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      packages: {'[+]': ['boldsymbol', 'ams', 'mathtools']},
      macros: {
        // 粗体向量（boldsymbol 的简写）
        bm: ["\\boldsymbol{#1}", 1],
        // 罗马字体（用于单位，如 \rm{kg}）
        rm: ["\\mathrm{#1}", 1],
        // 定义闭合积分符号为运算符
        oiint: "\\mathop{\\unicode{x222F}}\\nolimits",
        oint: "\\mathop{\\unicode{x222E}}\\nolimits",
        iiint: "\\mathop{\\unicode{x222D}}\\nolimits",
        iint: "\\mathop{\\unicode{x222C}}\\nolimits"
      }
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    },
    loader: {
      load: ['[tex]/boldsymbol', '[tex]/ams', '[tex]/mathtools']
    },
    svg: {
      fontCache: 'global'
    }
  };

  // The homepage has no formulas: load the engine only where it is needed.
  (() => {
    const loadMathJax = () => {
      if (!document.querySelector(".arithmatex") ||
          document.querySelector("script[data-mathjax-loader]")) return;
      const script = document.createElement("script");
      script.src = "https://unpkg.com/mathjax@3.2.2/es5/tex-mml-chtml.js";
      script.async = true;
      script.dataset.mathjaxLoader = "";
      document.head.appendChild(script);
    };

    if (typeof document$ !== "undefined") {
      document$.subscribe(loadMathJax);
    } else if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", loadMathJax, { once: true });
    } else {
      loadMathJax();
    }
  })();
