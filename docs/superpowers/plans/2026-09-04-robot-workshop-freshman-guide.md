# 《2026 Robot工作坊新生指南》落地上线实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 撰写并输出完整、高质量、接地气且融合 2026 最新具身智能技术栈与老指南温度的《2026 Robot工作坊新生指南》(`新生指南.md`)。

**Architecture:** 严格遵照批准的方案 A 及设计规范文档，分为【前言】、【一、工坊业务与竞赛全景】、【二、技能树与学长秘籍】、【三、学习安排与考核选拔】、【四、AI时代兵器库与极客社区】及【尾声：学长的大实话与工坊价值观】六大模块逐步实施。

**Tech Stack:** Markdown, Git, Mermaid, Python (PyMuPDF / docx 用于材料比对与校验), uv 现代包管理范式。

## Global Constraints
- 必须完全体现 2026 年最新赛况变化：RoboCup 全面转向人形机器人比赛，分为感知与定位、策略与决策、运动与控制、通信与系统 4 组，明确硬件与调试组已取消。
- 必须融入 `比赛` 目录中一手实战与排障案例（视觉挑战场地喷布反光排障、乒乓球 JAKA 机械臂奇异点避让与裁判盒闭环反馈、轮式格斗 OpenCV 识台与 AprilTag 标签测距）。
- 语言风格保持接地气、讲大实话、学长学姐带路、保姆级避坑指北。
- 完整保留“在工坊能收获什么”、“保研与绩点真相”、“最看重的品质（责任心第一）”等灵魂问答。

---

### Task 1: 编写【前言】与【第一章 1.1 核心领航赛事（RoboCup人形与世界人形机器人运动会）】

**Files:**
- Modify: `f:/Robot2026zhaoxin/新生指南.md`
- Reference: `f:/Robot2026zhaoxin/RoboCup技能要求.txt`, `f:/Robot2026zhaoxin/ROBOT工作坊新生的第一份指南.txt`

- [ ] **Step 1: 撰写前言部分**
  包含开篇警句（“学习的敌人是自己的满足……”）、传帮带文化、2026届答疑学长学姐名录模板（按专业方向和技术特长划分占位）、工坊元老与导师介绍。
- [ ] **Step 2: 撰写 1.1 核心领航赛事**
  置顶详细拆解 **RoboCup 机器人世界杯（人形赛项）**，介绍 4 大核心研发组职责、技术栈要求（强调硬件与调试组已取消），以及**世界人形机器人运动会**的前沿竞技。
- [ ] **Step 3: 格式校验与字数排版检查**
- [ ] **Step 4: 提交当前阶段变更至 Git**
  ```powershell
  git add 新生指南.md; git commit -m "feat: add preface and core embodied AI competitions"
  ```

---

### Task 2: 编写【第一章 1.2 主力骨干赛事 & 1.3 训练营矩阵】

**Files:**
- Modify: `f:/Robot2026zhaoxin/新生指南.md`
- Reference: `f:/Robot2026zhaoxin/比赛/`, `f:/Robot2026zhaoxin/ROBOT工作坊2026赛项清单.txt`, `f:/Robot2026zhaoxin/2025寒假训练营.txt`

- [ ] **Step 1: 撰写 1.2 主力骨干赛事**
  - **中国机器人大赛专项赛**：武术擂台-视觉挑战（附场地喷布反光排障案例）、武术擂台-轮式格斗（树莓派+Luby双控）、智能清洁机器人（ARM+单片机底盘、5自由度机械臂与逆解、Cartographer SLAM）、武术擂台-仿人格斗。
  - **中国高校智能机器人创意大赛**：四足机器人小型组（桌面双狗协同搬运）、四足机器人大型组（工业巡检救援越障）、智能机器人对抗赛（轮式自主攻防）。
  - **常规主力与拓展赛项**：乒乓球机器人（JAKA机械臂、LK电机、UDP裁判盒通信与闭环击球微调）、电赛与格斗赛建议。
- [ ] **Step 2: 撰写 1.3 训练营矩阵**
  - 校企训练营：达摩院 VLA 机械臂、中科云谷人形机器人、Datawhale/火山引擎 OpenClaw 百校用虾、抖音 AI 黑客松数据与成果。
  - 寒假精英训练营：4 周周计划追踪机制、统一软硬件基础考核 + 进阶技术自主选学答辩。
- [ ] **Step 3: 格式校验与链接检查**
- [ ] **Step 4: 提交当前阶段变更至 Git**
  ```powershell
  git add 新生指南.md; git commit -m "feat: add main competitions and training camps"
  ```

---

### Task 3: 编写【第二章 技能树与学长秘籍（2026 AI时代新解）】

**Files:**
- Modify: `f:/Robot2026zhaoxin/新生指南.md`
- Reference: `f:/Robot2026zhaoxin/资料.md`, `f:/Robot2026zhaoxin/ROBOT工作坊新生的第一份指南.txt`

- [ ] **Step 1: 撰写 2.1 基础技能**
  - 软件：C语言（工科基石、11月闭卷机考唯一科目、学到指针前，翁恺/黑马课推荐）、Python（高效胶水与AI调用）、Java（大实话版说明）。
  - 硬件：SolidWorks（3D机械建模打样）、立创EDA（PCB电路设计与板卡自制）。
- [ ] **Step 2: 撰写 2.2 进阶技术栈**
  - 嵌入式：51底层逻辑 ➔ STM32（江协科技/铁头山羊）。
  - Linux/Ubuntu：双系统/虚拟机避坑指南、常用指令速查心法（结合AI使用）。
  - ROS/ROS2：鱼香ROS一键安装、ROS2 Humble通信机制、Nav2导航、SMACC2状态机与BehaviorTree行为树。
  - CV（计算机视觉）：OpenCV实战定位（HSV分割、AprilTag识别、形态学处理），作为感知“螺丝刀”。
  - AI与具身智能：Datawhale 学习地图（Agent智能体、LLM应用、Vibe coding理念、强化学习蘑菇书）、VLA大模型体验、Isaac Sim / MuJoCo动力学仿真。
- [ ] **Step 3: 检查所有学习链接与推荐教程的有效性与可读性**
- [ ] **Step 4: 提交当前阶段变更至 Git**
  ```powershell
  git add 新生指南.md; git commit -m "feat: add skills tree and learning resources"
  ```

---

### Task 4: 编写【第三章 学习安排与选拔规则】与【第四章 AI时代兵器库与极客社区】

**Files:**
- Modify: `f:/Robot2026zhaoxin/新生指南.md`

- [ ] **Step 1: 撰写第三章 学习安排与选拔规则**
  - 10-11月：打牢C语言基础，11月下旬线下闭卷机考（重基本功与自学态度，高通过率，不为卡人）。
  - 12月：期末大过天，停训专心备战期末考试。
  - 1-2月：寒假精英营四周周计划打分；统一基础软硬件二选一考核 + 进阶技术自主答辩。
  - 春季开学后：队伍遴选与管理层（综合部、技术部、宣传部）换届面试与资源倾斜规则。
- [ ] **Step 2: 撰写第四章 AI时代兵器库与极客社区**
  - 编程软件（Power By AI）：VSCode+Copilot、Cursor、Claude、Antigravity IDE/2.0 等。指导新手善用 Skills、Subagents、Hooks 提效，强调“懂逻辑，拒抄袭”。
  - 现代环境配置：放弃又大又慢的 Anaconda，主推现代极速 Python 管理工具 `uv`（附国内镜像加速配置）与 Node.js/npm。
  - 极客社区：GitHub、Linux.do、V2EX、Hacker News、博客园。
- [ ] **Step 3: 格式与章节衔接检查**
- [ ] **Step 4: 提交当前阶段变更至 Git**
  ```powershell
  git add 新生指南.md; git commit -m "feat: add schedule selection and modern dev tools"
  ```

---

### Task 5: 编写【尾声：学长的大实话与工坊价值观】并执行全篇总装校验

**Files:**
- Modify: `f:/Robot2026zhaoxin/新生指南.md`

- [ ] **Step 1: 撰写尾声大实话与价值观部分**
  - 在工坊保底能得到什么？
  - 在工坊有追求还能得到什么？
  - 竞赛项目与保研的残酷真相（绩点是底线/门票，竞赛是上限与面试底气）。
  - 关于入选队员后与我们最看重的品质（责任心、靠谱、团队精神高于一切，杜绝弃赛与投机倒把）。
- [ ] **Step 2: 全篇 Markdown 格式、排版、层次与文字打磨**
- [ ] **Step 3: 运行校验检查文档字数、完整度与所有引用文件一致性**
- [ ] **Step 4: 提交最终完整指南至 Git**
  ```powershell
  git add 新生指南.md; git commit -m "feat: complete 2026 robot workshop freshman guide"
  ```
