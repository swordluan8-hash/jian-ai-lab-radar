# 剑的 AI 实验室 · GitHub Radar

每天从 GitHub Trending 与 X 发现正在升温的开源项目，逐个核验官方仓库，再写成中文用户能看懂、能上手、能判断成本的介绍。

**我们不搬运榜单，不用 Star 数代替判断。** 每条收录至少回答五个问题：它解决什么、适合谁、怎么开始、实际怎么用、需要付出什么成本。

[剑的 AI 实验室](https://jianailab.com) · [项目库](https://jianailab.com/library) · [竞技场](https://jianailab.com/community) · [English](README_EN.md)

## 今日发现 · 2026-08-31

今天收录 10 个赚钱方向项目；Best Skill Radar 经用户明确决定本日免除。当天只执行一个真实实验：[OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)。

| 项目 | 一句话看懂 | 今日状态 |
| --- | --- | --- |
| [TikTok Aura Farming](https://github.com/theneurallab/tiktok-aura-farming) | 复现 TikTok Aura Farming 视频制作代码。 | 已收录，未实验 |
| [Sorftime Seller Agent](https://github.com/DannylydST/sorftime-seller-agent) | 为六个平台提供选品和市场研究。 | 已收录，未实验 |
| [Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills) | 为 Amazon 卖家提供关键词、竞品和 Listing 审核 Skills。 | 已收录，未实验 |
| [Amazon Catalog CLI](https://github.com/BWB03/amazon-catalog-cli) | 让 Agent 查询 Amazon Category Listing Reports。 | 已收录，未实验 |
| [Lingxing MCP](https://github.com/zach22-1999/lingxing-mcp) | 只读接入领星 ERP 的经营数据。 | 已收录，未实验 |
| [TikTok Viral Factory](https://github.com/Vanszs/tiktok-viral-factory) | 多 Agent 制作 TikTok Shop 联盟视频，依赖外部媒体服务。 | 已收录，未实验 |
| [Pexo Skills](https://github.com/pexoai/pexo-skills) | 图片、音频与视频内容生产 Skills。 | 已收录，未实验 |
| [Atlas Marketing Studio](https://github.com/AtlasCloudAI/atlas-marketing-studio) | 自托管电商 AI 视频广告工作台。 | 已收录，未实验 |
| [Video Ad Generator](https://github.com/creatify-ai/video-ad-generator) | 从商品链接生成视频广告创意框架。 | 已收录，未实验 |
| [Ad Creative Evaluator](https://github.com/creatify-ai/ad-creative-evaluator) | 用八维规则和专家视角评估广告创意。 | 已收录，未实验 |

### 今日唯一实验

[OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)：首轮安装失败后修复；完整测试 7039 通过、45 失败、79 跳过；生产构建通过；真实导出 4 页、79,985 字节可编辑中文 PPTX。多智能体生成、TTS、视频和实时课堂没有测试。

- [2026-08-31 完整日报](daily/2026-08-31.md)
- [OpenMAIC YouTube 十五类画面制作包](production/2026-08-31-openmaic-youtube-production-pack.md)
- [结构化项目数据](data/projects.json)

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
