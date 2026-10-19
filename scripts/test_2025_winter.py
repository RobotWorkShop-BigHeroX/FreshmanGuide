import os
import subprocess
import sys
import zipfile

def test_2025_winter():
    base = "docs/2025/winter-camp"
    md_file = os.path.join(base, "2025寒假训练营.md")
    pdf_file = os.path.join(base, "2025寒假训练营.pdf")
    zip_file = os.path.join(base, "2025寒假训练营培训附件.zip")
  
    assert os.path.exists(md_file), "2025寒假训练营.md 缺失"
    assert os.path.exists(pdf_file), "2025寒假训练营 PDF 缺失"
  
    # 验证本地若存在附件压缩包，格式必须合法且受 .gitignore 保护
    if os.path.exists(zip_file):
        assert zipfile.is_zipfile(zip_file), "附件压缩包格式非法"
        res = subprocess.run(["git", "status", "--porcelain", zip_file], capture_output=True, text=True)
        assert "??" not in res.stdout, "ZIP 附件必须受 .gitignore 保护，不能处于未忽略状态"
  
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "冬训计划" in content or "训练营" in content, "Markdown 正文缺少核心通知标题"
    assert "知识产权与使用说明" in content or "授权声明" in content, "Markdown 必须包含清晰的培训资料知识产权与授权声明"
    print("Test passed: 2025 winter camp archive valid.")

if __name__ == "__main__":
    test_2025_winter()
