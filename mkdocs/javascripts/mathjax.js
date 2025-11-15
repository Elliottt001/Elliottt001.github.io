window.MathJax = {
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
  
  document$.subscribe(() => { 
    MathJax.startup.output.clearCache()
    MathJax.typesetClear()
    MathJax.texReset()
    MathJax.typesetPromise()
  })