# 湖南大学 Robot 工作坊新生指南与培训资料库

收录湖南大学现代工程训练中心 Robot 工作坊 2025 级与 2026 级招新指南、2025 寒假精英训练营技术文档与发行文件。

## 在线阅读地址

静态阅读页面部署于 GitHub Pages：
https://robotworkshop-bigherox.github.io/FreshmanGuide/

数据源由根目录下的 `catalog.json` 进行统一配置。

## 文档与发行版本

| 分类 | 标题 | 发布标签 | 官方文件 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| 2026 招新指南 | 2026 级 Robot 工作坊新生指南 | v2026-freshman | docs/2026/freshman/湖南大学Robot工作坊2026新生指南.pdf (2.6 MB) | 包含具身智能与双足人形机器人方向内容，正文由 Markdown 源码与 XeLaTeX 排版工程编译生成 |
| 2025 招新指南 | 2025 级 Robot 工作坊新生指南 | v2025-freshman | docs/2025/freshman/ROBOT工作坊2025新生的第一份指南.pdf (664 KB) | 历史原件归档，包含传统机器人竞赛规则、编程语言入门与基础考核说明 |
| 2025 寒假训练营 | 2025 寒假精英培训计划与材料 | v2025-winter | docs/2025/winter-camp/2025寒假训练营.pdf (310 KB) / [Release 附件包](https://github.com/RobotWorkShop-BigHeroX/FreshmanGuide/releases/tag/v2025-winter) | 第五届冬训计划通知细则。配套工程材料 2025寒假训练营培训附件.zip (58.5 MB) 作为资产发布于 GitHub Releases，不直接放入 Git 跟踪 |

## 本地运行与测试

### 1. 本地启动 HTTP 阅读服务
```bash
python -m http.server 8000
```
在浏览器中打开 http://localhost:8000/ 即可浏览阅读站。

### 2. 运行自动化测试套件
```bash
python scripts/run_checks.py
```

## 目录结构

```text
FreshmanGuide/
├── .github/workflows/
│   └── deploy-pages.yml         # GitHub Pages 自动化部署工作流
├── docs/
│   ├── 2025/
│   │   ├── freshman/            # 2025 级新生指南历史档案与原件 PDF
│   │   └── winter-camp/         # 2025 寒假精英训练营细则与通知 PDF
│   └── 2026/
│       └── freshman/            # 2026 级新生指南工程 (Markdown、XeLaTeX 源码与资源)
│           ├── assets/          # 徽标与架构图文件
│           ├── generate_tex.py  # LaTeX 刷新脚本
│           ├── 新生指南.md       # 事实来源 Markdown
│           ├── 新生指南.tex      # 排版源码
│           └── 湖南大学Robot工作坊2026新生指南.pdf # 发行版 PDF
├── scripts/                     # 验证测试脚本
│   ├── run_checks.py            # 统一执行入口
│   ├── test_2025_freshman.py    # 2025 指南完整性检查
│   ├── test_2025_winter.py      # 2025 训练营检查
│   ├── test_2026_build.py       # 2026 编译检查
│   ├── test_deployment_config.py# 部署配置检查
│   ├── test_web_reader.py       # 前端阅读站安全检查
│   └── validate_catalog.py      # catalog.json 验证
├── catalog.json                 # 全局数据清单
├── index.html                   # 静态阅读页面
├── pyproject.toml / uv.lock     # Python 工具依赖管理配置
├── README.md                    # 本文档
└── LICENSE                      # MIT 授权文件
```

## 知识产权与使用说明

1. 仓库内代码、排版脚本、自动化测试脚本与指南正文遵循 MIT 许可协议。
2. 寒假训练营中的 SolidWorks 机器人模型、立创EDA 教学演示板工程、讲义文档及视频由湖南大学 Robot 工作坊成员编写制作，版权归工坊所有，仅供校内社团及机器人爱好者学术交流与培训使用，禁止商业用途；引用的元器件数据手册（Datasheet）与芯片参考封装版权归各半导体原厂商所有。
3. 大文件附件发布说明：2025 寒假训练营相关的配套材料压缩包 `2025寒假训练营培训附件.zip` 体积约为 58.5 MB（包含 SolidWorks 三维模型、立创EDA 工程文件、学习文档与教学视频）。为了避免大体积二进制文件导致 Git 版本库历史严重膨胀，该压缩包受 `.gitignore` 过滤规则保护，不直接纳入 Git 版本库跟踪，发布为 GitHub Release 独立资产。查阅下载请访问 [GitHub Release v2025-winter 发行页面](https://github.com/RobotWorkShop-BigHeroX/FreshmanGuide/releases/tag/v2025-winter) 或直接下载 [2025寒假训练营培训附件.zip](https://github.com/RobotWorkShop-BigHeroX/FreshmanGuide/releases/download/v2025-winter/2025%E5%AF%92%E5%81%87%E8%AE%AD%E7%BB%83%E8%90%A5%E5%9F%B9%E8%AE%AD%E9%99%84%E4%BB%B6.zip)。
