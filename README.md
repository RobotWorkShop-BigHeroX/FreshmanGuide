# 湖南大学 Robot 工作坊 2026 新生指南

> **Hunan University Robot Workshop 2026 Freshman Guidebook**  
> 凝聚热血与热爱 · 面向 2026 级新成员的极客入门指南与知识图谱

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 项目简介

本项目是**湖南大学 Robot 工作坊**面向 2026 级招新与新成员培养打造的官方新生指南手册。

手册旨在帮助对机器人竞赛与工程实践感兴趣的新同学快速建立系统的认知脉络，涵盖工坊发展脉络、核心竞赛矩阵、技术学习递进路线以及日常科研协作准则，消除零基础顾虑，树立严谨靠谱的极客工程素养。

---

## 📂 仓库文件清单

仓库经过深度精简与规范化整理，保留核心源码与单一正式发行文件：

| 文件名 | 格式 / 类型 | 说明 |
| :--- | :--- | :--- |
| **`湖南大学Robot工作坊2026新生指南.pdf`** | 最终发行版 PDF | 排版优雅的正式发布版手册（基于 ClassicThesis 风格排版） |
| **`新生指南.md`** | Markdown 源码 | 完整的轻量级文本，支持在线阅读与全文检索 |
| **`新生指南.tex`** | XeLaTeX 源码 | 高质量排版源码，含定制宏包配置、版面几何与色彩方案 |
| **`generate_tex.py`** | Python 构建脚本 | 自动化构建/更新 LaTeX 源码的生成脚本 |
| **`pyproject.toml` / `uv.lock`** | Python 工程配置 | 基于 [uv](https://github.com/astral-sh/uv) 现代化包管理器管理 |
| **`image/` & `RobotWorkShop.jpg`** | 架构图与工坊徽标 | 包含 RoboCup 人形赛项四大核心研发组架构图与主力赛事全景图 |
| **`README.md`** | 仓库说明 | 本文档，包含项目导航与本地构建指南 |
| **`LICENSE`** | 开源协议 | [MIT License](LICENSE) 授权许可 |
| **`.gitignore`** | Git 配置文件 | 忽略 LaTeX 编译中间缓存、Python 字节码与系统临时文件 |

---

## 🛠️ 本地编译与构建指南

若需对手册进行内容修改并重新编译生成 PDF，请按以下步骤操作：

### 1. 环境依赖
- **Python 包管理**：推荐安装 [uv](https://github.com/astral-sh/uv)。
- **LaTeX 编译引擎**：推荐安装 [TeX Live](https://www.tug.org/texlive/) 或 [MacTeX](https://www.tug.org/mactex/)。
- **排版引擎**：`XeLaTeX`。
- **系统字体**：
  - 中文字体：`SimSun`（宋体）、`SimHei`（黑体）、`KaiTi`（楷体）。
  - 西文字体：`Palatino Linotype`、`Arial`、`Consolas`。

### 2. 重新生成并编译 PDF
在项目根目录下打开终端，执行以下命令：

```bash
# 1. 使用 uv 运行 Python 脚本生成/更新 LaTeX 源码
uv run python generate_tex.py

# 2. 使用 XeLaTeX 编译生成 PDF（建议编译两次以确保目录与页码跳转正确更新）
xelatex -interaction=nonstopmode 新生指南.tex
xelatex -interaction=nonstopmode 新生指南.tex
```

---

## 🤝 编著者与贡献者

- **编著者**：李鸿 (`2868014836@qq.com`)
- **贡献者**：江涛、李书淇、乔淼 等原著作者 $\cdot$ 工坊历届队员与指导团队
- **出品方**：湖南大学现代工程训练中心 Robot 工作坊
- **指导精神**：知行合一 · 追求极致 · 传承热爱

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。
