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
    ready() {
      // 在 MathJax 渲染前，将 arithmatex 遗留的 math/tex 脚本转换为 MathJax 3 格式
      document.querySelectorAll('script[type^="math/tex"]').forEach(script => {
        script.type = script.type.replace('math/tex', 'text/tex');
      });
      MathJax.startup.defaultReady();
    }
  }
};
