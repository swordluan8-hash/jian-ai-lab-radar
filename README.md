# 剑的 AI 实验室 · GitHub Radar

每天从 GitHub Trending、X 和 Agent Skills 排行中发现正在升温的开源项目，逐个回到官方仓库核验，再写成中文用户能看懂、能上手、能判断成本的介绍。

我们不搬运榜单，也不用 Star 数代替判断。每条收录至少回答五个问题：它解决什么、适合谁、怎么开始、实际怎么用、需要付出什么成本。

[剑的 AI 实验室](https://jianailab.com) · [项目库](https://jianailab.com/library) · [竞技场](https://jianailab.com/community) · [English](./README_EN.md)

## 今日发现 · 2026-08-29

| 项目 | 一句话看懂 | 今日信号 |
|---|---|---|
| [GitNexus](https://jianailab.com/projects/gitnexus) | 把整座代码库变成浏览器里的关系图，再用 Graph RAG Agent 追踪调用链。 | GitHub Trending Today #5 |
| [Cursor Plugins](https://jianailab.com/projects/cursor-plugins) | 让 Cursor 直接调用邮件、网盘、日历、GitHub、浏览器和审查等官方插件。 | GitHub Trending Today #8 |
| [OpenLogi](https://jianailab.com/projects/openlogi) | 本地配置罗技设备的按键、DPI 和 SmartShift，不要账号，也不要遥测。 | X discovery |
| [OpenHuman](https://jianailab.com/projects/openhuman) | 把个人记忆、深度研究和多 Agent 工作流装进一个本地优先的 AI 工作台。 | X discovery |
| [FreeLLMAPI](https://jianailab.com/projects/freellmapi) | 把多家免费模型层接到一个 OpenAI 兼容接口，并自动回退。 | GitHub Trending Today #13 |
| [Music Assistant](https://jianailab.com/projects/music-assistant) | 把流媒体、本地曲库和多品牌联网音箱放进同一套播放系统。 | X discovery |
| [Awesome Agent Skills](https://jianailab.com/projects/awesome-agent-skills) | 从一千多个跨客户端 Skills 里按用途找现成能力。 | GitHub Trending This week |
| [agents-radar](https://jianailab.com/projects/agents-radar) | 每天汇总十类 AI 信号，生成双语日报、网页、RSS 和 MCP。 | X discovery |
| [OpenBot](https://jianailab.com/projects/openbot) | 给每个 AI 同事独立浏览器、文件和工具，并记录每一步动作。 | X discovery |
| [Screenshot to Code](https://jianailab.com/projects/screenshot-to-code) | 上传截图、网页或录屏，生成可继续编辑的 HTML、React 或 Vue。 | GitHub Trending Today #7 |

今天唯一完整实验是 [Scientific Agent Skills](https://jianailab.com/projects/scientific-agent-skills)，完整核验资料、实验结果与限制见 [2026-08-29 日报](./daily/2026-08-29.md)。结构化数据见 [data/projects.json](./data/projects.json)。

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
