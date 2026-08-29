# 剑的 AI 实验室 · GitHub Radar

每天从 GitHub Trending 与 X 发现正在升温的开源项目，逐个核验官方仓库，再写成中文用户能看懂、能上手、能判断成本的介绍。

**我们不搬运榜单，不用 Star 数代替判断。** 每条收录至少回答五个问题：它解决什么、适合谁、怎么开始、实际怎么用、需要付出什么成本。

[剑的 AI 实验室](https://jianailab.com) · [项目库](https://jianailab.com/library) · [竞技场](https://jianailab.com/community) · [English](README_EN.md)

## 今日发现 · 2026-08-29

| 项目 | 一句话看懂 | 今日信号 |
| --- | --- | --- |
| [CDM](https://github.com/KAIST-Visual-AI-Group/CDM) | 让离散扩散模型在采样时更快地朝着高奖励结果走。 | X Radar Top #1 |
| [Anthropic Skills](https://github.com/anthropics/skills) | 把写作、设计、编程和文档工作变成可安装的 Agent 能力。 | X Radar Top #3 · Best Skills 安装量 |
| [Superpowers](https://github.com/obra/superpowers) | 把编程 Agent 的需求、计划、实现和验证串成可重复工作流。 | X Radar Top #3 |
| [GLM-5.3-Flash From Scratch](https://github.com/vukrosic/glm-5.3-flash-from-scratch) | 用 2,573 万参数从零训练一个可运行的教学模型。 | X Radar Top #4 |
| [pi-subagents](https://github.com/tintinweb/pi-subagents) | 给 Pi 装上可并行、可暂停接管、可恢复的子 Agent。 | X Radar Top #5 |
| [video-use](https://github.com/browser-use/video-use) | 把一句剪辑要求交给编程 Agent，直接从素材生成视频。 | X Radar Top #6 |
| [AI-Trader](https://github.com/HKUDS/AI-Trader) | 让 AI Agent 从市场研究走到交易执行。今天唯一完整实验候选，尚未启动。 | X Radar Top #7 |
| [OpenClaw](https://github.com/openclaw/openclaw) | 把 AI 助手从聊天框搬到操作系统和日常工作里。 | X Radar Top #8 |
| [早耳 hayamimi](https://github.com/oboroge0/hayamimi) | 不用 GPU 和云服务，也能把实时多语种语音变成字幕。 | X Radar Top #14 |
| [AI Resume Analyzer](https://github.com/adrianhajdin/ai-resume-analyzer) | 把简历对着职位要求打分，并给出修改方向。 | X Radar Top #15 |

完整中文介绍、安装路径和来源见 [2026-08-29 日报](daily/2026-08-29.md)。结构化数据见 [`data/projects.json`](data/projects.json)。今日十项均已发现并核验，尚未启动完整实验；AI-Trader 是今天唯一排定的实验对象。

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
