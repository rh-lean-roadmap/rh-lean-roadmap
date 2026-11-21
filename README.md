# rh-lean-roadmap

A short guide for human readers to the Lean proof of the Riemann hypothesis and of the generalized Riemann hypothesis for Dirichlet *L*-functions, announced by Levent Alpöge on 20 November 2026.

The proof exists only as a Lean 4 archive: 175,187 files, 17.4 million lines, no comments. It has been checked by machine (see [Sutherland's report](https://math.mit.edu/~drew/grh/)), but no human has read it through. This repository tries to make its shape visible.

| | |
|---|---|
| [`paper/roadmap.pdf`](paper/roadmap.pdf) | Seven pages, in English. The top of the argument in five steps, each tied to declarations in the archive, followed by the published foundations and a list of what we did not understand. |
| [`web/index.html`](web/index.html) | A story version for readers with no mathematics, in Chinese and English. Download it and open it in a browser. |
| [`video/east-of-the-line.mp4`](video/east-of-the-line.mp4) | An 80-second vertical video (Chinese, text only, original background music) for social media, with two cover images. |
| [`lean/Roadmap.lean`](lean/Roadmap.lean) | A small Lean file. It adds no mathematics: it restates the top of the proof using the archive's own theorems and proves, inside the archive, that three inputs (`Green`, `VWin`, `HypsAlt …`) imply Mathlib's `RiemannHypothesis`. |

## What this is and is not

- It is an exposition. It is not a new proof, and it does not shorten the proof: every line of the archive is still needed.
- The mathematical explanations are our reading of the code and of Alpöge's [remark](https://alpo.ge/remark.pdf). They may be wrong in detail; the Lean code is authoritative.
- The archive itself is **not** included. It carries no licence, so we do not redistribute it; the instructions below download it from its author.
- One person came up with the idea, set the direction and made the calls; the text and code were written and cross-checked by several AI models, including Anthropic's Claude. Alpöge works at Anthropic. This repository is not affiliated with him or with Anthropic.

## Checking `Roadmap.lean`

`Roadmap.lean` is compiled inside the archive, so you need the archive, Lean 4.33.1 (installed automatically by [elan](https://github.com/leanprover/elan) from `lean-toolchain`) and the Mathlib cache.

```bash
# 1. Download the 14 parts from the author's site and check them.
for i in $(seq -w 1 14); do curl -fLO "https://alpo.ge/lean.tar.gz.part$i"; done
sha256sum -c rh-lean-roadmap/lean/SHA256SUMS
cat lean.tar.gz.part* | sha256sum
# expected: 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc
# (the same archive Sutherland checked)

# 2. Unpack (creates ./lean) and add the roadmap file to the archive's Supplements library.
cat lean.tar.gz.part* | tar xz
cp rh-lean-roadmap/lean/Roadmap.lean lean/src/Supplements/Roadmap.lean

# 3. Fetch the prebuilt Mathlib and build only what the roadmap imports.
cd lean
lake exe cache get
lake build +Supplements.Roadmap
```

`lake build +Supplements.Roadmap` compiles only the import closure of the file, about 26,000 build jobs (the 17,276 archive files it reaches, plus Mathlib, which the cache provides prebuilt). In our test this took about 2 h 20 min with 24 build threads and about 160 GB of disk for build output; check your free space first. The last lines of output print the three inputs and `#print axioms Roadmap.rh_of_three_inputs`, which should list only `propext`, `Classical.choice` and `Quot.sound`.

This checks the *reduction*. That the three inputs hold is proved elsewhere in the archive; for that, rely on the full build and kernel checks in [Sutherland's report](https://math.mit.edu/~drew/grh/), or build the whole archive yourself (about 1.7 TB of build output).

## Verification status

As of Sutherland's report (page last updated 2026-11-20 22:05 UTC): all 175,187 modules compile; the five main theorems use only the three standard axioms; `leanchecker` replays every module; nanoda and con-leche accept the full export; lean4lean accepts every module. Replay of the export by Lean's default and paranoid kernels and an end-to-end `lake comparator` run were still running. Check the report for the current state.

## Sources

- L. Alpöge, remark and Lean archive: <https://alpo.ge/remark.pdf>, <https://alpo.ge/lean.tar.gz.part01> … `part14`
- A. V. Sutherland, verification report: <https://math.mit.edu/~drew/grh/>
- T. Tao, blog post of 20 November 2026: <https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/>

## Licence

Text, web page and video (`paper/`, `web/`, `video/`, this README): [CC BY 4.0](LICENSE). Lean file (`lean/`): [Apache-2.0](lean/LICENSE). The Alpöge archive is not part of this repository and is not covered by these licences.

---

## 中文简介

2026 年 11 月 20 日，Levent Alpöge 公布了和 Claude 一起完成的黎曼猜想与狄利克雷 GRH 的 Lean 证明。证明只有 Lean 代码这一种形式，共 17.5 万个文件、1740 万行，没有注释。机器检查已经通过，但还没有人读完。本仓库是一份导读：

- `paper/roadmap.pdf`：7 页英文导读，比较严谨，把证明顶层的五步和档案里的具体声明一一对上；
- `web/index.html`：中英双语的讲故事版，不需要数学背景，下载后用浏览器打开；
- `video/east-of-the-line.mp4`：80 秒竖屏短视频（纯文字介绍、原创背景音乐），附两张封面；
- `lean/Roadmap.lean`：一个小 Lean 文件，不加新数学，只用档案自己的定理串出“三个输入 ⇒ 黎曼猜想”，可在档案内编译检查。

这是导读，不是新证明，也没有把证明变短。档案本身没有许可证，本仓库不转载，只给出从作者网站下载和校验的方法。本仓库由一个人提出想法、定方向、做取舍，文字和代码由多个 AI 模型（其中包括 Anthropic 的 Claude）写成并交叉核对；Alpöge 在 Anthropic 工作；本仓库与他和 Anthropic 都没有隶属关系。
