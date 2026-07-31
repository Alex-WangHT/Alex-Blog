// MathJax 3 配置：仅支持 $...$ 和 $$...$$
// 禁用默认的 \(...\) 和 \[...\] 分隔符
window.MathJax = {
  tex: {
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: true,
    processEnvironments: false
  },
  options: {
    // 禁用菜单中的 MathJax 右键菜单（可选）
    renderActions: {
      addMenu: []
    }
  }
};
