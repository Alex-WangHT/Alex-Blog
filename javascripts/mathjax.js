// MathJax 3 配置
// 支持 arithmatex generic 输出的 \( \) 和 \[ \]
// 兼容 arithmatex fenced code block 遗留的 math/tex 脚本标签
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

// 轮询转换 math/tex → text/tex，直到 MathJax 可用
(function checkAndConvert() {
  var scripts = document.querySelectorAll('script[type^="math/tex"]');
  if (scripts.length > 0 && typeof MathJax !== 'undefined' && MathJax.typesetPromise) {
    scripts.forEach(function(script) {
      script.type = script.type.replace('math/tex', 'text/tex');
    });
    MathJax.typesetPromise();
    return;
  }
  // 继续轮询，最多 50 次（5 秒）
  if ((checkAndConvert.retry = (checkAndConvert.retry || 0) + 1) < 50) {
    setTimeout(checkAndConvert, 100);
  }
})();
