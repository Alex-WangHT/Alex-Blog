// MathJax 3 配置
// 支持 arithmatex generic 输出的 \( \) 和 \[ \]
// 以及 math/tex script 标签（由 fenced code block 生成）
window.MathJax = {
  tex: {
    inlineMath: [
      ['$', '$'],
      ['\\(', '\\)']
    ],
    displayMath: [
      ['$$', '$$'],
      ['\\[', '\\]']
    ],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    renderActions: {
      addMenu: []
    }
  },
  startup: {
    pageReady() {
      // 将 arithmatex 遗留的 math/tex script 标签转换为 MathJax 3 格式
      document.querySelectorAll('script[type^="math/tex"]').forEach(script => {
        script.type = script.type.replace('math/tex', 'text/tex');
      });
      return MathJax.startup.defaultPageReady();
    }
  }
};
