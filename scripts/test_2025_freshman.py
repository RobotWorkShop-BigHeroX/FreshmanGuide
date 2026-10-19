import os

def test_2025_freshman():
    base = "docs/2025/freshman"
    md_file = os.path.join(base, "2025新生指南.md")
    pdf_file = os.path.join(base, "ROBOT工作坊2025新生的第一份指南.pdf")
  
    assert os.path.exists(md_file), "2025新生指南.md 缺失"
    assert os.path.exists(pdf_file), "2025新生指南 PDF 缺失"
    assert os.path.getsize(pdf_file) > 500000, "2025新生指南 PDF 字节大小异常"
  
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "历史原件转录" in content or "转录版本" in content, "Markdown 应显式声明为历史原件转录版"
    print("Test passed: 2025 freshman guide archive valid.")

if __name__ == "__main__":
    test_2025_freshman()
