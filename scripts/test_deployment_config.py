import os

def test_deployment_config():
    yml_path = ".github/workflows/deploy-pages.yml"
    assert os.path.exists(yml_path), "deploy-pages.yml missing"
  
    with open(yml_path, "r", encoding="utf-8") as f:
        yml = f.read()
  
    # 验证权限最小化声明
    assert "contents: read" in yml, "deploy-pages.yml missing 'contents: read'"
    assert "pages: write" in yml, "deploy-pages.yml missing 'pages: write'"
    assert "id-token: write" in yml, "deploy-pages.yml missing 'id-token: write'"
  
    # 验证 CI 前置门禁
    assert "run_checks.py" in yml, "deploy-pages.yml must invoke python scripts/run_checks.py before deployment"
  
    # 验证 README.md
    assert os.path.exists("README.md"), "README.md missing"
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    assert "Robot" in readme, "README.md missing Robot Workshop title"
    assert "http.server" in readme or "本地调试" in readme or "快速启动" in readme, "README.md missing local server instructions"
  
    # 验证 LICENSE
    assert os.path.exists("LICENSE"), "LICENSE missing"
  
    print("Test passed: deployment configuration and project documentation valid.")

if __name__ == "__main__":
    test_deployment_config()
