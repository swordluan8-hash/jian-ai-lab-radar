# OpenMAIC 逐平台发布包 v2

日期：2026-08-31  
唯一主实验：[`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC)  
完整报告：https://jianailab.com/reports/openmaic-offline-classroom-export-test  
实验田：https://jianailab.com/experiments/openmaic-offline-classroom-export-test

## 统一事实口径

- GitHub Trending 全球 Today 第 1 名，实验对象固定为 OpenMAIC。
- 首轮安装退出 1；调整隔离副本构建许可后，第二轮退出 0。
- 完整测试：7039 项通过、45 项失败、79 项跳过。
- PPTX 导出专项：3 个文件、5 项测试全部通过。
- Next.js 生产构建退出 0，共生成 52 个静态页面。
- 直接调用项目生产函数 `buildPptxBlob`，导出 4 页、79,985 字节的可编辑中文 PPTX。
- 全程没有使用付费模型 API。
- 没有验证多智能体课程生成、TTS、视频生成和实时课堂；任何平台都不得把这些能力写成“已实测”。

## 发布顺序与审核门

正式顺序固定为：**X → DEV → 小红书 → Instagram → TikTok**。

本文件是逐平台审核稿。未经用户逐个平台确认，不把“稿件已准备”写成“已经发布”。YouTube、知乎、B站、抖音由用户录音、剪辑和发布。

---

## 1. X 串文（7 条）

### 1/7

GitHub Trending 第 1 名 OpenMAIC，我做了完整离线实测。

结果不是一句“很强”：

7039 项通过  
45 项失败  
79 项跳过  
生产构建成功  
真实导出 4 页可编辑中文 PPTX

失败记录全部保留。

报告：https://jianailab.com/reports/openmaic-offline-classroom-export-test

### 2/7

OpenMAIC 来自清华团队，目标是把主题或资料转成互动课堂：课件、测验、网页、白板、语音和项目式学习。

今天不验证宣传页，而是只测四件事：

安装、完整测试、生产构建、PPTX 导出。

### 3/7

第一次安装退出 1。

原因是 pnpm 11 检测到第三方构建脚本没有明确许可，安装链被拦截。

这条失败没有删除。第二轮只放行导出路径需要的 esbuild，其他第三方安装脚本继续禁用，重新安装退出 0。

### 4/7

完整测试不是全绿：

7039 passed  
45 failed  
79 skipped

主要失败来自浏览器并发存储测试的 5 秒超时，另有远程图片导出超时。

所以不能把结论写成“全部通过”。

### 5/7

今天真正使用的是 PPTX 导出路径。

文本内容、文本格式、背景 3 个专项测试文件，共 5 项测试全部通过。

Next.js 生产构建退出 0，生成 52 个静态页面。

### 6/7

最后直接调用 OpenMAIC 生产代码里的 `buildPptxBlob`。

导出结果：

4 页中文微课  
79,985 字节  
可在 PowerPoint / Keynote 继续编辑  
文件结构和预设文字已解包核验

下载：https://jianailab.com/experiments/openmaic/openmaic-harvest-pack.zip

### 7/7

结论：

已验证：安装、生产构建、离线 PPTX 导出。  
未验证：多智能体课程生成、TTS、视频生成、实时课堂。

OpenMAIC 的导出链能留下真实成果，但完整课程质量仍需真实模型和人工审核。

GitHub 是土地，我们是实验田。

---

## 2. DEV 英文长文

### Title

OpenMAIC Offline Test: 7,039 Passed, 45 Failed, and a Real Editable PPTX

### Body

OpenMAIC reached the top of GitHub Trending, so I tested it as today's single main experiment instead of writing a feature summary.

The scope was deliberately narrow and reproducible:

1. install the pinned source,
2. run the full test suite,
3. run a production build,
4. call the project's own PPTX export path,
5. keep every failure and limitation in the record.

The first installation exited with code 1. The workspace compiled, but pnpm 11 stopped third-party build scripts that had not been explicitly approved. I kept that failure. In a second isolated run, I allowed only the esbuild step required by the export path; the installation then exited with code 0.

The complete test run produced:

- 7,039 passed
- 45 failed
- 79 skipped

The failures were not hidden. Most came from five-second timeouts in concurrent browser-storage tests, with another timeout in a remote-image export test. Therefore, this is not a “fully green” result.

The focused PPTX export checks were stronger: three files and five tests all passed. The Next.js production build also exited with code 0 and generated 52 static pages.

For the harvest artifact, I called OpenMAIC's production `buildPptxBlob` function directly. It produced a four-slide, 79,985-byte editable Chinese PPTX. I then unpacked the file and verified that all four slide XML files and the expected preset text were present.

No paid model API was used.

What this experiment verified:

- installation after a documented permission adjustment,
- production build,
- focused PPTX export,
- a real downloadable and editable output file.

What it did not verify:

- multi-agent course generation,
- TTS,
- video generation,
- real-time classroom interaction,
- end-to-end course quality using a live model.

Full report: https://jianailab.com/reports/openmaic-offline-classroom-export-test

Harvest package: https://jianailab.com/experiments/openmaic/openmaic-harvest-pack.zip

Repository: https://github.com/THU-MAIC/OpenMAIC

---

## 3. 小红书

### 标题

GitHub 第1名 OpenMAIC 实测：7039通过，45失败也保留

### 正文

今天只做一个主实验：OpenMAIC。

不是转发项目介绍，而是完整走安装、测试、生产构建和成果导出。

真实结果：

✅ 第二轮安装成功  
✅ 7039 项测试通过  
⚠️ 45 项失败  
⏭️ 79 项跳过  
✅ 生产构建成功，52 个静态页面  
✅ PPTX 导出专项 5 项全过  
✅ 真实导出 4 页可编辑中文课件

首轮安装其实失败了，退出码是 1。修正隔离副本的构建许可后，第二轮才成功。这条失败没有删。

最后不是放一张效果图，而是直接调用项目自己的生产导出函数，拿到 79,985 字节的 PPTX，并解包核验 4 页结构。

边界也写清楚：今天没有测试多智能体课程生成、TTS、视频生成和实时课堂。

完整报告和成果包都在 Jian AI Lab。

#OpenMAIC #GitHubTrending #AI工具 #开源项目 #AI课件 #实测

### 图片顺序

1. 横版/竖版封面：GitHub 第1名
2. Trending 排名证据
3. 首轮安装退出 1
4. 修复后安装退出 0
5. 7039/45/79 测试结果
6. 5 项导出专项全部通过
7. 四页 PPTX 结果
8. 已验证 / 未验证边界卡

---

## 4. Instagram

### Caption

OpenMAIC was #1 on GitHub Trending, so I ran a real offline test.

Results:

✅ Installation succeeded after a documented permission fix  
✅ 7,039 tests passed  
⚠️ 45 failed  
⏭️ 79 skipped  
✅ Production build completed with 52 static pages  
✅ 5/5 focused PPTX export tests passed  
✅ A real 4-slide, editable Chinese PPTX was generated

The first install failed with exit code 1, and that failure remains in the report.

No paid model API was used. Multi-agent course generation, TTS, video generation, and real-time classroom features were not tested.

Full report: jianailab.com/reports/openmaic-offline-classroom-export-test

#OpenMAIC #GitHubTrending #OpenSource #AItools #EdTech #BuildInPublic

### Carousel

封面 → 排名 → 安装失败 → 安装成功 → 完整测试 → 构建成功 → PPTX 四页 → 结论边界。

---

## 5. TikTok 60 秒竖版稿

### 口播

GitHub Trending 第一名 OpenMAIC，我没有只看介绍，直接跑了完整离线实验。

第一次安装退出 1，因为 pnpm 拦住了没有明确许可的第三方构建脚本。修正隔离副本许可后，第二次安装退出 0。

完整测试结果：7039 项通过，45 项失败，79 项跳过。失败主要是浏览器并发存储测试超时，所以不能写成全部通过。

生产构建成功，生成 52 个静态页面。PPTX 导出专项 5 项全部通过。

最后我直接调用项目自己的生产导出函数，真实生成了 4 页、79,985 字节的可编辑中文 PPTX。

今天已经验证安装、构建和离线导出；没有验证多智能体生成、语音、视频和实时课堂。

完整报告和成果包都在 Jian AI Lab。

### 竖版镜头

0–4 秒：封面“GitHub 第1名”  
4–10 秒：项目首页与 Trending  
10–17 秒：首轮安装退出 1  
17–23 秒：修复后退出 0  
23–33 秒：7039 / 45 / 79  
33–40 秒：构建 52 个静态页面  
40–50 秒：连续翻四页 PPTX  
50–56 秒：已验证 / 未验证  
56–60 秒：报告和下载入口

---

## 6. 用户发布平台

### YouTube

标题：**GitHub 第一名 OpenMAIC 实测：7039 项通过，45 项失败全部保留**

完整十五类画面、3 分 28 秒口播和单行字幕规则：

https://github.com/swordluan8-hash/jian-ai-lab-radar/blob/main/production/2026-08-31-openmaic-youtube-production-pack.md

### 知乎

标题：**OpenMAIC 离线实测报告：7039 项通过、45 项失败，PPTX 导出链真实可用**

正文使用完整中文长文：

https://github.com/swordluan8-hash/jian-ai-lab-radar/blob/main/production/2026-08-31-openmaic-long-article-zh.md

### B站

标题：**清华 OpenMAIC 完整实测：安装翻车、7039 项通过、真实导出 PPTX**

简介：保留测试数字、报告链接、成果包链接和未验证边界。主视频复用 YouTube 横版剪辑。

### 抖音

标题：**GitHub 第一名 OpenMAIC，45 项失败我也留下了**

使用上方 TikTok 60 秒口播与竖版镜头；字幕保持单行。

---

## 素材下载

- 完整收成包：https://chatgpt.com/api/library/files/libfile_c1d13867cad8819198a69b520dec7c1c/download
- 四页可编辑 PPTX：https://chatgpt.com/api/library/files/libfile_a117bd225cac8191a9a66acd3183c657/download
- 21 秒证据视频：https://chatgpt.com/api/library/files/libfile_ebff9ded692c8191856bad2c22b93d2b/download
- 实验结果图：https://chatgpt.com/api/library/files/libfile_e1680536d6e88191977d4f53e71fead9/download
- 竖版封面：https://chatgpt.com/api/library/files/libfile_3f6036cce6b0819180d85467cfb63899/download

## 当前真实状态

- 上述平台稿件已完成。
- X、DEV、小红书、Instagram、TikTok 尚未发布，等待逐平台审核。
- OpenMAIC 团队邀请尚未发送。
- YouTube、知乎、B站、抖音尚未发布；需要用户录音、剪辑和上传。
