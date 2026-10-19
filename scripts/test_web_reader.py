import os

def test_web_reader():
    html_path = "index.html"
    assert os.path.exists(html_path), "index.html missing"
  
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
  
    # 1. 验证版本锁定
    assert "marked@15.0.7" in html or "marked.min.js" in html, "Marked.js 缺少或未指定精确版本"
    assert "dompurify@3.2.4" in html or "purify.min.js" in html, "DOMPurify 缺少或未指定精确版本"
    assert "highlight.js@11.9.0" in html or "highlight.min.js" in html, "Highlight.js 缺少或未指定精确版本"
  
    # 2. 验证安全性：DOMPurify 清洗
    assert "DOMPurify.sanitize" in html, "未在渲染管道中强制执行 DOMPurify.sanitize 清洗"
  
    # 3. 验证协议检测与本地服务器友好提示
    assert "location.protocol" in html or "file:" in html, "缺少针对本地 file:// 协议的自适应检测"
    assert "http.server" in html or "python -m http.server" in html, "缺少针对本地服务器调试的指引提示"
  
    # 4. 验证相对图片重定向逻辑
    assert "markdownPath" in html, "缺少基于当前文档路径的资源解析上下文"
    assert "resolveAssetUrl" in html or "resolveRelativeUrl" in html or "rewritePath" in html or "normalizePath" in html, "缺少 Markdown 内相对资源重定位逻辑"
  
    # 5. 验证工具栏与多版本交互
    assert "pdfPath" in html, "缺少 PDF 下载交互绑定"
    assert "catalog.json" in html, "缺少从 catalog.json 动态加载元数据的数据驱动逻辑"
  
    print("Test passed: index.html meets frontend architecture and security rules.")

if __name__ == "__main__":
    test_web_reader()
