# 剑的 AI 实验室 · GitHub Radar

每天从 GitHub Trending 与 X 发现正在升温的开源项目，逐个核验官方仓库，再写成中文用户能看懂、能上手、能判断成本的介绍。

**我们不搬运榜单，不用 Star 数代替判断。** 每条收录至少回答五个问题：它解决什么、适合谁、怎么开始、实际怎么用、需要付出什么成本。

[剑的 AI 实验室](https://jianailab.com) · [项目库](https://jianailab.com/library) · [竞技场](https://jianailab.com/community) · [English](README_EN.md)

## 今日发现 · 2026-08-30

| 项目 | 一句话看懂 | 今日信号 |
| --- | --- | --- |
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | 把模型、工具、会话、权限和沙箱组织成插件式 Agent 框架。 | X @Smartpigai 原帖 · 官方维护者 DeepSeek AI |
| [nanochat](https://github.com/karpathy/nanochat) | 用依赖精简的完整流水线训练和运行 ChatGPT 克隆。 | X @karpathy 原帖 · 官方维护者 Andrej Karpathy |
| [LangGraph](https://github.com/langchain-ai/langgraph) | 用状态图编排可恢复、有记忆的 Agent 应用。 | X @Smartpigai 原帖 · 官方维护者 LangChain AI |
| [Baoyu Skills](https://github.com/JimLiu/baoyu-skills) | 把翻译、文章、图片和幻灯片变成可安装技能。 | X @dotey 原帖 · 官方维护者 JimLiu |
| [Guizang PPT Skill](https://github.com/op7418/guizang-ppt-skill) | 把文章变成带配图、封面和演讲者模式的网页幻灯片。 | X @op7418 原帖 · 官方维护者 op7418 |
| [OpenSquilla](https://github.com/opensquilla/opensquilla) | 用本地路由和持久记忆把 Agent 任务分给合适模型。 | X @xiaohu 原帖 · 官方维护者 opensquilla |
| [LJG Skills](https://github.com/lijigang/ljg-skills) | 把文章、论文、卡片和阅读整理成中文技能集。 | X @lijigang 原帖 · 官方维护者 lijigang |
| [Claude-to-IM-skill](https://github.com/op7418/Claude-to-IM-skill) | 把 Claude Code 或 Codex 接入 Telegram、Discord 和飞书。 | X @op7418 原帖 · 官方维护者 op7418 |
| [swyxio Skills](https://github.com/swyxio/skills) | 把技术材料、读者变化和视觉制作组织成内容工作流。 | X @swyx 原帖 · 官方维护者 swyxio |
| [llm-jq](https://github.com/simonw/llm-jq) | 用自然语言生成 jq 查询处理 JSON。 | X @simonw 原帖 · 官方维护者 Simon Willison |

完整核验、来源归因和剔除记录见 [2026-08-30 日报](daily/2026-08-30.md)。结构化数据见 [data/projects.json](data/projects.json)。本批次均为已发现、已核验项目，尚未完成完整实验。

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
