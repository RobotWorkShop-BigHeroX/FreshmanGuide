# 湖南大学 Robot 工作坊招新与培训知识门户 (FreshmanGuide)

> **Hunan University Robot Workshop Freshman Guide & Training Portal**  
> 湖南大学现代工程训练中心 Robot 工作坊官方知识门户 · 凝聚热血与热爱 · 传承极客工程精神

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/Online%20Portal-GitHub%20Pages-blue.svg)](https://robotworkshop-bigherox.github.io/FreshmanGuide/)

---

## 🌐 在线阅读与门户访问

本项目提供纯静态 SPA 在线阅读门户，支持全文检索、响应式排版、右侧目录大纲跳转与各版本原件下载：

- **官方在线门户**：[https://robotworkshop-bigherox.github.io/FreshmanGuide/](https://robotworkshop-bigherox.github.io/FreshmanGuide/)
- **数据驱动配置**：全局清单由根目录 [`catalog.json`](catalog.json) 统筹驱动。

---

## 📚 知识归档矩阵

本仓库对湖南大学 Robot 工作坊历年招新指南、竞赛经验与冬训材料进行系统化归档与长青维护：

| 年份 / 分类 | 文档标题 | 发布标签 | 官方原件 / 资产 | 说明 |
| :--- | :--- | :--- | :--- | :--- |
| **2026 招新指南** | 2026 级 Robot 工作坊新生指南 | `v2026-freshman` | [官方发行版 PDF](docs/2026/freshman/湖南大学Robot工作坊2026新生指南.pdf) (2.6 MB) | 唯一内容源驱动，涵盖具身智能与双足人形机器人前沿业务 |
| **2025 招新指南** | 2025 级 Robot 工作坊新生指南 | `v2025-freshman` | [官方原件 PDF](docs/2025/freshman/ROBOT工作坊2025新生的第一份指南.pdf) (664 KB) | 历史原件归档，涵盖传统竞赛体系、编程入门与基础考核 |
| **2025 寒假冬训** | 2025 寒假精英培训计划与材料 | `v2025-winter` | [官方通知 PDF](docs/2025/winter-camp/2025寒假训练营.pdf) (310 KB) / [Release附件包](https://github.com/RobotWorkShop-BigHeroX/FreshmanGuide/releases/tag/v2025-winter) | 第五届冬训计划通知细则，配套 SolidWorks 与立创EDA 实战包 |

---

## 🚀 本地调试与快速启动

本项目前端采用原生 HTML5、现代 CSS 与纯 JavaScript 构建，遵循浏览器安全规范：

### 1. 本地启动 HTTP 阅读服务器
```bash
# 在仓库根目录启动轻量级 HTTP 服务
python -m http.server 8000
```
在浏览器中打开：[http://localhost:8000/](http://localhost:8000/) 即可流畅浏览与调试。

### 2. 运行全量前置回归检验
```bash
# 运行统一自动化测试套件
python scripts/run_checks.py
```

---

## 📁 仓库目录结构

```text
FreshmanGuide/
├── .github/workflows/
│   └── deploy-pages.yml         # GitHub Pages 自动化前置验证与部署工作流
├── docs/
│   ├── 2025/
│   │   ├── freshman/            # 2025 级新生招新历史档案与原件 PDF
│   │   └── winter-camp/         # 2025 寒假精英训练营细则与官方通知 PDF
│   └── 2026/
│       └── freshman/            # 2026 级新生指南核心工程 (SSOT Markdown + XeLaTeX 源码 + 资产)
│           ├── assets/          # 徽标与架构图表 (RobotWorkShop.jpg, png)
│           ├── generate_tex.py  # LaTeX 刷新构建脚本
│           ├── 新生指南.md       # 唯一事实来源 (SSOT)
│           ├── 新生指南.tex      # ClassicThesis 优雅排版源码
│           └── 湖南大学Robot工作坊2026新生指南.pdf # 最终发行版 PDF
├── scripts/                     # 生产回归测试脚本套件 (CI 前置门禁)
│   ├── run_checks.py            # 统一测试执行入口
│   ├── test_2025_freshman.py    # 2025 归档完整性检验
│   ├── test_2025_winter.py      # 2025 训练营与附件过滤检验
│   ├── test_2026_build.py       # 2026 编译生成全链检验
│   ├── test_deployment_config.py# 工作流与文档合规检验
│   ├── test_web_reader.py       # 前端架构与安全注入检验
│   └── validate_catalog.py      # catalog.json 元数据格式检验
├── catalog.json                 # 全局数据驱动清单
├── index.html                   # 原生科技极客风格 SPA 在线阅读站
├── pyproject.toml / uv.lock     # Python 依赖管理配置
├── README.md                    # 本文档
└── LICENSE                      # MIT 开源协议
```

---

## 🤝 编著者与贡献者

- **2026 编著者**：李鸿 (`2868014836@qq.com`)
- **原著与历史贡献者**：江涛、李书淇、乔淼 等原著作者 $\cdot$ 工坊历届队员与指导团队
- **出品机构**：湖南大学现代工程训练中心 Robot 工作坊

---

## 📄 知识产权与使用授权

1. **开源授权**：本仓库的代码、排版脚本、自动化测试套件以及原创指南正文依据 [MIT License](LICENSE) 协议开源。
2. **教学培训资料说明**：寒假精英训练营中的 SolidWorks 机器人模型、立创EDA 教学演示板工程、讲义文档及视频由湖南大学 Robot 工作坊往届成员编写制作，版权归工坊所有，仅供校内学生社团及机器人爱好者学术交流与实践培训使用，禁止任何未经授权的商业用途；所附带的元器件公开技术数据手册（Datasheet）及芯片参考封装版权归各半导体原厂商所有。
