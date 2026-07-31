// MathJax 3 配置
// pymdownx.arithmatex (generic: true) 将 $...$ 输出为 \(...\)，$$...$$ 输出为 \[...\]
// 因此 MathJax 必须同时支持这两种分隔符
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
  }
};
