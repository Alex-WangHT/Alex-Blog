// MathJax 3 配置
// 禁用 arithmatex 后，MathJax 直接在客户端处理 $...$ 和 $$...$$
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
