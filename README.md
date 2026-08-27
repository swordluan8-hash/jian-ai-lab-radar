# 剑的 AI 实验室 · GitHub Radar

每天从 GitHub Trending 与 X 发现正在升温的开源项目，逐个核验官方仓库，再写成中文用户能看懂、能上手、能判断成本的介绍。

**我们不搬运榜单，不用 Star 数代替判断。** 每条收录至少回答五个问题：它解决什么、适合谁、怎么开始、实际怎么用、需要付出什么成本。

[剑的 AI 实验室](https://jianailab.com) · [项目库](https://jianailab.com/library) · [竞技场](https://jianailab.com/community) · [English](README_EN.md)

## 今日发现 · 2026-08-27

| 项目 | 一句话看懂 | 今日信号 |
| --- | --- | --- |
| [Archify](https://github.com/tt-a1i/archify) | 让 Codex、Claude Code 或 Cursor 把代码库变成可核验、可交互、可导出的专业架构图。 | GitHub Trending 全球今日榜第 1 |
| [Open Notebook](https://github.com/lfnovo/open-notebook) | 把 PDF、视频、网页和笔记整理成可本地运行的私人 AI 研究助手。 | 约 37.7k Stars |
| [No AI Slop](https://github.com/petergyang/no-ai-slop) | 检查并清理 20 多类常见 AI 写作套路。 | 约 6.1k Stars |
| [OpenSEO](https://github.com/every-app/open-seo) | 自托管关键词研究、排名跟踪、SEO 审计和竞品分析。 | 约 13.6k Stars |
| [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 给编程 Agent 接入多模型网关，额度或服务故障时自动换线路。 | 约 56.5k Stars |
| [AI Job Search](https://github.com/MadsLorentzen/ai-job-search) | 用本地 Claude Code 流程评估岗位、定制简历并准备面试。 | 约 36.9k Stars |
| [Strix](https://github.com/usestrix/strix) | 让 AI Agent 对获授权应用做安全测试并交付漏洞证据。 | 约 58.7k Stars |
| [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) | 把 500 多个图像、视频与口型同步模型放进统一工作台。 | 约 27.2k Stars |
| [Freecut](https://github.com/Moh4696/freecut) | 让 Codex 或 Claude Code 参与剪辑、字幕、转场与动画叠加。 | 本地 Whisper 免费转写路线 |
| [Pentest AI](https://github.com/0xSteph/pentest-ai) | 每个 AI 发现的漏洞都要复测，并附可重放的证据包。 | 约 1.6k Stars |
| [Agent Orchestrator](https://github.com/Untrivial-ai/agent-orchestrator) | 在一张 Agent IDE 里调度编程 Agent、CI 修复、冲突与审查。 | 约 10k Stars |

完整中文介绍、安装路径和来源见 [2026-08-27 日报](daily/2026-08-27.md)。结构化数据见 [`data/projects.json`](data/projects.json)。

## 收录标准

1. 仓库必须公开、存在且没有失效或被误导性重命名。
2. 先查 GitHub Trending 与 X，再回到官方 README 核验事实。
3. 检查是否重复收录，并记录核验日期、Star 快照、语言和许可证。
4. 中文介绍必须包含价值、能力、最短上手、使用例子、成本或门槛。
5. Trending 只代表当前热度，不代表永久质量；所有变化数据都标注日期。
6. 安全测试项目只记录官方用途与授权边界，不夸大能力。

## 每日更新承诺

- 每天检查 GitHub Trending 的 Today 与 This week。
- 每天到 X 查找作者、开发者与可信介绍者的原始传播内容。
- 目标每天核验 10 个新项目；质量不足时明确记录，不拿无效项目凑数。
- 同步更新本仓库、[剑的 AI 实验室项目库](https://jianailab.com/library)和[竞技场](https://jianailab.com/community)。
- 给每个项目保留 GitHub、作者与发现来源链接，把读者送回原作者。

## 提交项目

开发者可以使用 [Project submission](../../issues/new?template=project-submission.yml) 提交公开 GitHub 仓库。提交不等于自动收录，我们会核验仓库、README、许可、维护状态和中文用户的实际价值。

## 数据复用

`data/projects.json` 遵循 [`schema/project.schema.json`](schema/project.schema.json)。运行以下命令检查数据完整性：

```bash
npm test
```

项目采用 [MIT License](LICENSE)。项目名称、商标与仓库内容归各自作者所有；本仓库保留并展示原始链接与来源。
