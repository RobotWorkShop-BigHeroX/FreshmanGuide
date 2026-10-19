import os
import subprocess
import sys

def test_2026_build():
    base = "docs/2026/freshman"
    md_file = os.path.join(base, "新生指南.md")
    tex_file = os.path.join(base, "新生指南.tex")
    gen_script = os.path.join(base, "generate_tex.py")
    pdf_file = os.path.join(base, "湖南大学Robot工作坊2026新生指南.pdf")
  
    assert os.path.exists(md_file), "SSOT 新生指南.md 缺失"
    assert os.path.exists(tex_file), "新生指南.tex 缺失"
    assert os.path.exists(gen_script), "generate_tex.py 缺失"
    assert os.path.exists(pdf_file), "正式发行版 PDF 缺失"
  
    # 验证资产
    assets_dir = os.path.join(base, "assets")
    for img in ["RobotWorkShop.jpg", "robocup_subgroups.png", "main_competitions.png"]:
        assert os.path.exists(os.path.join(assets_dir, img)), f"缺少排版必需资产: {img}"
      
    # 验证生成脚本能否正常执行并生成 tex (使用脚本文件名避免在指定 cwd 时路径重复拼接)
    res = subprocess.run([sys.executable, os.path.basename(gen_script)], cwd=base, capture_output=True, text=True)
    assert res.returncode == 0, f"generate_tex.py 执行失败: {res.stderr}"
    assert os.path.exists(tex_file), "generate_tex.py 未能刷新新生指南.tex"
  
    # 验证生成的 tex 引用了正确的 assets 相对路径
    with open(tex_file, "r", encoding="utf-8") as f:
        tex_content = f.read()
    assert "assets/RobotWorkShop.jpg" in tex_content, "tex 缺少正确的 Logo 路径引用"
    assert "assets/robocup_subgroups.png" in tex_content, "tex 缺少正确的分组架构图引用"
    assert "assets/main_competitions.png" in tex_content, "tex 缺少正确的赛事全景图引用"
  
    print("Test passed: 2026 engineering workspace and generation pipeline valid.")

if __name__ == "__main__":
    test_2026_build()
