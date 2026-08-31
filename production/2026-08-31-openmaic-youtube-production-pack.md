# OpenMAIC YouTube 完整制作包（十五类画面版）

日期：2026-08-31  
唯一实验：[`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC)  
实验报告：https://jianailab.com/reports/openmaic-offline-classroom-export-test

## 已核验结论

- 首轮安装退出 1；调整隔离副本的构建许可后安装退出 0。
- 完整测试：7039 通过、45 失败、79 跳过。
- PPTX 导出专项：3 个文件、5 项测试，全部通过。
- Next.js 生产构建退出 0，生成 52 个静态页面。
- 直接调用项目生产函数 `buildPptxBlob`，导出 4 页、79,985 字节的可编辑中文 PPTX。
- 没有使用付费模型 API。
- 没有验证多智能体课程生成、TTS、视频生成和实时课堂，禁止把这些能力写成已实测。

## YouTube 主标题

**GitHub 第一名 OpenMAIC 实测：7039 项通过，45 项失败全部保留**

备选标题：

1. **零付费装完 OpenMAIC，我真实导出了 4 页可编辑课件**
2. **OpenMAIC 完整测试：7039 项通过，但这 45 项不能藏**
3. **清华 OpenMAIC 实测：安装、构建、PPTX 导出真实结果**

缩图固定文字：

- GitHub 第1名
- 7039通过 45失败
- 真实导出PPTX

## 开场钩子

GitHub Trending 第一名 OpenMAIC，我用零付费方法完成安装、完整测试和生产构建，最后真实导出了一套四页可编辑中文课件。7039 项测试通过，但 45 项失败一条也没有删。

## 十五类画面与时间轴

所有字幕只占一行。终端、README 和代码画面必须来自官方仓库或真实实验记录，不使用生成图冒充操作证据。

| # | 档案要求 | 时间 | 真实画面或文件 | 对应口播 | 单行字幕 |
|---|---|---:|---|---|---|
| 1 | 项目首页或原作者介绍 | 00:00–00:10 | `frame-01-trending.png`；[官方仓库首页](https://github.com/THU-MAIC/OpenMAIC) | 今天榜首是清华团队的 OpenMAIC。 | GitHub Trending 第1名 |
| 2 | 项目核心功能 | 00:10–00:23 | 官方 README Overview 与 Highlights | 它把主题或资料变成课件、测验、互动网页和项目式学习。 | 一个主题生成互动课堂 |
| 3 | 安装过程录屏 | 00:23–00:38 | `frame-02-install.png` 中首轮安装命令与退出码 | 第一次安装没有通过，命令退出 1。 | 首轮安装退出1 |
| 4 | 首次运行画面 | 00:38–00:51 | `frame-02-install.png` 修复后退出 0；`openmaic-evidence.mp4` 对应片段 | 只放行导出需要的 esbuild 后，第二次安装成功。 | 修复后安装退出0 |
| 5 | 关键操作录屏 | 00:51–01:05 | [`lib/export/use-export-pptx.ts`](https://github.com/THU-MAIC/OpenMAIC/blob/main/lib/export/use-export-pptx.ts) 中 `buildPptxBlob` | 最终成果直接调用项目自己的生产导出函数。 | 调用生产PPTX导出器 |
| 6 | 最终结果画面 | 01:05–01:20 | 打开 `jian-ai-lab-openmaic-offline-classroom.pptx`，连续翻四页 | 这不是展示图，而是一份真正可编辑的四页 PPTX。 | 真实导出4页PPTX |
| 7 | 输入和输出对比 | 01:20–01:34 | 左侧实验主题，右侧 PPTX 四页；可用 `frame-04-result.png` | 输入是一段课程主题，输出是四页结构化课件。 | 输入主题 输出可编辑课件 |
| 8 | 速度或步骤对比 | 01:34–01:48 | 四步卡片：安装、测试、构建、导出；不写速度数字 | 今天没有伪造速度对比，只记录四个可复查阶段。 | 安装→测试→构建→导出 |
| 9 | 项目目录或核心文件 | 01:48–02:00 | GitHub 目录与 `lib/export/use-export-pptx.ts` | 核心导出逻辑就在仓库的 export 路径中。 | 核心文件来自官方仓库 |
| 10 | README 关键段落 | 02:00–02:13 | README 中 Export anywhere、PPTX/HTML 说明 | 官方明确写了可以导出可编辑 PPTX 和互动 HTML。 | 官方支持PPTX与HTML导出 |
| 11 | 真实报错或翻车 | 02:13–02:28 | `frame-02-install.png`；`frame-03-tests.png` 的失败数字 | 完整测试不是全绿，45 项失败主要是并发存储超时。 | 45项失败全部保留 |
| 12 | 修复后的成功画面 | 02:28–02:42 | `frame-02-install.png` 退出 0；专项测试 5/5 | 修复安装后，今天使用的五项导出专项全部通过。 | 导出专项5项全过 |
| 13 | 用户使用场景 | 02:42–02:56 | PPTX 四页在 PowerPoint/Keynote 中打开 | 教师和培训团队可以继续修改文字、顺序和讲解重点。 | 课件可以继续编辑 |
| 14 | 作者或社区活跃情况 | 02:56–03:10 | [官方仓库 PR](https://github.com/THU-MAIC/OpenMAIC/pulls) 与 [Issues](https://github.com/THU-MAIC/OpenMAIC/issues) | 仓库仍在持续更新，问题和改动都能公开追踪。 | 项目仍在持续维护 |
| 15 | 最终结论画面 | 03:10–03:28 | `frame-04-result.png`；实验报告下载区 | 安装、构建和 PPTX 导出已经验证；模型生成和语音视频没有测试。 | 已验证导出 未验证模型生成 |

## 完整口播稿

GitHub Trending 第一名 OpenMAIC，我用零付费方法完成安装、完整测试和生产构建，最后真实导出了一套四页可编辑中文课件。7039 项测试通过，但 45 项失败一条也没有删。

OpenMAIC 来自清华大学团队。它想把一个主题或一份资料变成互动课堂，包括课件、测验、互动网页、项目式学习、白板和语音。

介绍很完整，但实验田不靠介绍下结论。今天只验证四件事：能不能安装、能不能跑完整测试、能不能完成生产构建，以及它自己的 PPTX 导出链能不能留下真实文件。

源码固定在实验记录使用的提交。首轮安装先退出 1。仓库自己的供应链检查通过，工作区包也完成编译，但 pnpm 11 发现第三方构建许可没有明确选择，因此拦截安装脚本。

这条失败没有删除。

第二轮只放行今天导出需要的 esbuild，其他第三方安装脚本继续禁用。重新安装后退出 0。全程没有填写模型密钥，也没有调用付费 API。

接着运行完整测试，一共 7163 项：7039 项通过、45 项失败、79 项跳过。主要失败来自浏览器并发存储测试的五秒超时，另有一个远程图片导出测试超时。所以这次不能写成全绿。

今天真正使用的是 PPTX 导出路径。文本内容、文本格式和背景三个专项测试文件共五项测试，全部通过。Next.js 生产构建也退出 0，生成 52 个静态页面，同时保留了两条 Edge Runtime 警告。

最后进入收成区。

实验没有另外画一张图冒充成果，而是直接调用 OpenMAIC 生产代码中的 buildPptxBlob，导出了一堂四页中文微课。文件有 79,985 字节，可以在 PowerPoint 或 Keynote 里继续编辑。

随后又解包检查 PPTX。四个幻灯片 XML 都存在，四段预设文字也都能找到，文件哈希已经写入实验报告。

因此，今天真正验证的是安装、生产构建和离线 PPTX 导出。多智能体课堂生成没有测试，因为它需要模型服务；TTS、视频生成和实时互动也没有测试。

这个结论比“项目很强”更有用：OpenMAIC 的导出链确实能留下可下载成果，但完整课程质量仍需要真实模型和人工审核继续验证。

完整命令、失败记录、PPTX、结果图和证据视频都在 Jian AI Lab。GitHub 是土地，我们是实验田。

## 单行字幕规则

- 每行最多 18 个汉字或 34 个英文字符。
- 屏幕同时只显示一行字幕。
- 测试数字保持阿拉伯数字，不写成中文数字。
- “7039通过，45失败，79跳过”不得拆散或改成“全部通过”。
- 不给未测试能力加“可用”“稳定”“完整验证”等词。

## 已有素材

- `openmaic-harvest-pack.zip`
- `jian-ai-lab-openmaic-offline-classroom.pptx`
- `frame-01-trending.png`
- `frame-02-install.png`
- `frame-03-tests.png`
- `frame-04-result.png`
- `openmaic-evidence.mp4`：21 秒、1920×1080、H.264、无声
- `openmaic-vertical-cover.png`
- 新制作横版缩图：`openmaic-youtube-thumbnail.png`

## 下载入口

- 收成包：https://chatgpt.com/api/library/files/libfile_c1d13867cad8819198a69b520dec7c1c/download
- PPTX：https://chatgpt.com/api/library/files/libfile_a117bd225cac8191a9a66acd3183c657/download
- 证据视频：https://chatgpt.com/api/library/files/libfile_ebff9ded692c8191856bad2c22b93d2b/download
- 结果图：https://chatgpt.com/api/library/files/libfile_e1680536d6e88191977d4f53e71fead9/download
- 竖版封面：https://chatgpt.com/api/library/files/libfile_3f6036cce6b0819180d85467cfb63899/download

## 用户剪辑动作

1. 按完整口播稿录音。
2. 按十五行时间轴放入真实画面，缺少的网页画面只从上表官方链接录取。
3. 把 21 秒证据视频拆入安装、测试、导出和结论四段。
4. 所有字幕保持单行。
5. 导出 1920×1080 横版主视频。
6. 用竖版封面、相同证据片段和 60 秒口播制作抖音版。
7. 发布前核对数字：7039、45、79、5、52、4、79,985。

当前没有宣称 YouTube、抖音、知乎或 B站已经发布。
