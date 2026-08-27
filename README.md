# 剑的 AI 实验室 · GitHub Radar

每天从 GitHub Trending、X 和 Agent Skills 排行中发现正在升温的开源项目，逐个回到官方仓库核验，再写成中文用户能看懂、能上手、能判断成本的介绍。

我们不搬运榜单，也不用 Star 数代替判断。每条收录至少回答五个问题：它解决什么、适合谁、怎么开始、实际怎么用、需要付出什么成本。

[剑的 AI 实验室](https://jianailab.com) · [项目库](https://jianailab.com/library) · [竞技场](https://jianailab.com/community) · [English](./README_EN.md)

## 今日发现 · 2026-08-28

| 项目 | 一句话看懂 | 今日信号 |
|---|---|---|
| [God's Eye View](https://jianailab.com/projects/gods-eye-view) | 把公开空间信号放进可交互的写实 3D 地球。 | GitHub Trending Today |
| [Nitter](https://jianailab.com/projects/nitter) | 轻量 X 替代前端；仓库已归档并暂停。 | Trending · 风险记录 |
| [Awesome GPT Image 2](https://jianailab.com/projects/awesome-gpt-image-2) | 530+ 案例、20+ 模板与可安装风格 Skill。 | GitHub Trending Today |
| [Go Modern Guidelines](https://jianailab.com/projects/go-modern-guidelines) | 让编码 Agent 按 go.mod 采用兼容的现代 Go 写法。 | GitHub Trending Today |
| [Claude Plugins Official](https://jianailab.com/projects/claude-plugins-official) | Anthropic 官方 Claude Code 插件目录。 | GitHub Trending Today |
| [Ponytail](https://jianailab.com/projects/ponytail) | 约束编码 Agent 少写代码、少造抽象。 | GitHub Trending Today |
| [AI Engineering from Scratch](https://jianailab.com/projects/ai-engineering-from-scratch) | 20 阶段、511 节构建优先 AI 工程课程。 | GitHub Trending Today |
| [Garden Skills](https://jianailab.com/projects/garden-skills) | 面向多种编码 Agent 的现成 Skills 合集。 | GitHub Trending Today |
| [Claude-Mem](https://jianailab.com/projects/claude-mem) | 自动保存和召回 Agent 的跨会话上下文。 | GitHub Trending Today |
| [GoogleTest](https://jianailab.com/projects/googletest) | 成熟的 C++ 测试与 Mock 基础设施。 | GitHub Trending Today |
| [Best Skills](https://jianailab.com/projects/best-skills) | 用跨生态安装量、增长和讨论生成每日 Skill 排行。 | 社区推荐 · 每日榜单 |

完整核验资料、作者账号和实验室公开联系见 [2026-08-28 日报](./daily/2026-08-28.md)。结构化数据见 [data/projects.json](./data/projects.json)。

## 三源雷达

1. **GitHub Trending**：发现突然升温的新仓库。
2. **X Radar**：寻找作者原帖、传播路径与真实讨论。
3. **Best Skills**：观察近期真正被安装的 Agent Skill。

任何榜单都只负责发现。最终是否值得用，仍要回到 README、许可证、维护状态、权限、成本和真实实验。

## 收录标准

- 仓库必须公开、存在且没有失效或被误导性重命名。
- 先查发现信号，再回到官方 README 核验事实。
- 检查是否重复收录，并记录核验日期、Star 快照、语言和许可证。
- 中文介绍必须包含价值、能力、最短上手、使用例子、成本或门槛。
- Trending、安装量和讨论热度都不等于永久质量或安全认证。
- 安全测试项目只记录官方用途与授权边界，不夸大能力。

## 每日更新承诺

- 每天检查 GitHub Trending 的 Today 与 This week。
- 每天使用 X Radar 查找作者、开发者与可信介绍者的原始传播内容。
- 每天检查 Best Skills 等公开 Skill 数据源，补充安装趋势。
- 目标每天核验 10 个不重复的新项目，并选 1 个进入完整实测。
- 同步更新本仓库、剑的 AI 实验室项目库和竞技场。
- 给每个项目保留 GitHub、作者、原帖与实验室公开回复链接。

## 提交项目

开发者可以使用 [Project submission](https://github.com/swordluan8-hash/jian-ai-lab-radar/issues/new?template=project-submission.yml) 提交公开 GitHub 仓库。提交不等于自动收录，我们会核验仓库、README、许可、维护状态和中文用户的实际价值。

## 数据复用

[data/projects.json](./data/projects.json) 遵循 [schema/project.schema.json](./schema/project.schema.json)。运行以下命令检查数据完整性：

```bash
npm test
```

项目采用 MIT License。项目名称、商标与仓库内容归各自作者所有；本仓库保留并展示原始链接与来源。
