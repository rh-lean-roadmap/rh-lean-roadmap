# rh-lean-roadmap

Homepage: <https://rh-lean-roadmap.github.io/rh-lean-roadmap/> · Zenodo, version v44: [doi:10.5281/zenodo.24562451](https://doi.org/10.5281/zenodo.24562451)

A guide for human readers to the Lean proof of the Riemann hypothesis and of the generalized Riemann hypothesis for Dirichlet *L*-functions, announced by Levent Alpöge on 20 November 2026.

The proof is a Lean 4 archive of 175,187 files and 17.4 million lines, without comments. Several independent checkers have accepted it (see [Sutherland's report](https://math.mit.edu/~drew/grh/)), and on 21 November the Lean FRO and the Mathlib Initiative certified in a joint statement that the statement and the proof of the Riemann hypothesis are correct ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). This repository writes the argument out for mathematicians and ties every statement to the archive.

| | |
|---|---|
| [`docs/book.pdf`](docs/book.pdf) | The argument written out for mathematicians, in English: a main text of 497 pages, an appendix of 963 pages with the longer proofs, and an index of the Lean declarations (1582 pages in all). Every statement the proof needs, in the order the proof uses it; the index at the end lists, for each statement by its number, the Lean declarations that prove it, with their files and lines. Chapter 4 proves the window criterion by a shorter argument with a Gaussian kernel, which is not formalised; the archive's proof is in the appendix. Arguments made for this proof are given with proofs, the longer ones in the appendix with an outline in the main text; published results are stated in the form the archive uses, with references. A background chapter collects the facts on the Weil representation and theta lifts that the proof uses. Nine parts: the window criterion, the prime sum and the auxiliary primes, the divisibility from one theta lift, its accumulation along the chain, the two bounds on one slope, the Tate–Shafarevich window bound, and the three inputs with the Galois representations and the local Langlands correspondence they use. LaTeX sources in `docs/src/book/`. |
| [`docs/simplification-notes.md`](docs/simplification-notes.md) | What was tried to shorten the proof or make it more elementary, and how each attempt came out: two simplifications used in the book, several ruled out, two still open. |
| [`docs/reading-guide-en.pdf`](docs/reading-guide-en.pdf) | A reading guide in English (22 pages). The argument in six steps, each tied to the archive's declarations: the prime sum over Frobenius classes, the theta-lift chain and the local computation behind its divisibility, the division of lattices and the two-sided slope estimate that plays the role of Stepanov's inequality, the Tate–Shafarevich window bound, how the three inputs are proved, and in what form the archive proves the published theorems it uses. An appendix gives the location of every declaration cited. |
| [`docs/reading-guide-zh.pdf`](docs/reading-guide-zh.pdf) | The same guide in Chinese (21 pages). LaTeX sources in `docs/src/` (the Chinese version uses the Noto Serif/Sans SC fonts). |
| [`paper/roadmap.pdf`](paper/roadmap.pdf) | Seven pages, in English. The top of the argument in five steps, each tied to declarations in the archive, then the published foundations and the points still to be traced. |
| [`web/index.html`](web/index.html) | A story version for readers with no mathematics, in Chinese and English. Read it online at <https://rh-lean-roadmap.github.io/rh-lean-roadmap/web/>. |
| [`video/east-of-the-line.mp4`](video/east-of-the-line.mp4) | A 75-second vertical video (Chinese, text only, original background music) for social media, with two cover images. |
| [`lean/Roadmap.lean`](lean/Roadmap.lean) | A small Lean file. Using only the archive's own theorems, it proves inside the archive that three inputs (`Green`, `VWin`, `HypsAlt …`) imply Mathlib's `RiemannHypothesis`. |
| [`lean/slim/`](lean/slim/) | A slicer and keep lists that cut the archive down to what `Roadmap.lean` uses: 18,096 of its 175,188 files and 3.2 of its 17.4 million lines. The slimmed copy builds with no errors. |

## How the book was written

Each chapter was drafted from the Lean source of the declarations it covers and checked against that source. Referee models from several families then read anonymised copies of the book over repeated rounds; every point they raised was settled against the Lean archive before the text was changed. Statements follow the Lean statements; where the archive proves a published theorem in a weaker form, the chapter states the form the archive proves. Where the text and the archive differ, the archive is authoritative. The text has not yet been reviewed by a human expert.

Sixty-three proofs, all in Part VIII, are headed “Proof (outline)”; each states its steps and ends by naming the Lean declaration that contains the complete proof. [`docs/outline-proofs.md`](docs/outline-proofs.md) lists them. A script builds the graph of citations between proofs, and the text is ordered so that no proof uses, directly or through other results, the statement it proves. Every build is also checked for undefined references, undefined citations and duplicate labels; there are none.

The typewriter font is JetBrains Mono (SIL Open Font License); put `JetBrainsMono.ttf` in `docs/src/book/fonts/` and compile `main.tex` with XeLaTeX or Tectonic.

## How much of the archive the proof uses

J. Shore traced the kernel proof terms of the five main theorems through a full build of the archive ([data and method](https://github.com/james-shore/rh-proof-dependencies), dataset v0.2.1). The five theorems use 804,912 of the archive's 1,061,400 declarations (75.8%), in 146,287 of its 175,187 files, and the used declarations span 10,737,728 of its 17,374,215 lines (61.8%). Each theorem alone uses at least 804,889 of these declarations. The top of the argument, from the three inputs to the theorems, uses 96,541 declarations in 5,683 files (about 680,000 lines; see `lean/Roadmap.lean`).

## About this repository

- The proof is Alpöge's archive; this repository explains its structure. The explanations come from reading the code and Alpöge's [remark](https://alpo.ge/remark.pdf), and the Lean code gives the exact statements.
- The archive carries no licence, so the steps below download it from its author's site and check it.
- An independent author, not a specialist in this area, set the direction and made the calls; the text and code were written and cross-checked by several AI models, including Anthropic's Claude. Alpöge works at Anthropic; this repository is independent of him and of Anthropic.

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

# 3. Fetch the prebuilt Mathlib and build what the roadmap imports.
cd lean
lake exe cache get
lake build +Supplements.Roadmap
```

`lake build +Supplements.Roadmap` compiles the import closure of the file, about 26,000 build jobs (the 17,276 archive files it reaches, plus Mathlib, which the cache provides prebuilt). In our test this took about 2 h 20 min with 24 build threads and about 160 GB of disk for build output; check your free space first. The last lines of output print the three inputs and `#print axioms Roadmap.rh_of_three_inputs`, which lists `propext`, `Classical.choice` and `Quot.sound`.

This build checks the step from the three inputs to the Riemann hypothesis. The inputs themselves are proved in the rest of the archive, which Sutherland's full build covers; building the whole archive takes about 1.7 TB of disk.

## A slimmed copy for `Roadmap.lean`

[`lean/slim/`](lean/slim/) holds a slicer and keep lists. Applied to the unpacked archive, they produce a copy that keeps only the declarations the step from the three inputs to the Riemann hypothesis uses, with the structures and elaboration lines those declarations need.

| | files | lines | size |
|---|---:|---:|---:|
| archive `src` | 175,188 | 17,374,270 | 1.03 GB |
| slimmed copy | 18,096 | 3,168,570 | 167 MB |

In the slimmed copy, `lake build +Supplements.Roadmap` completes with no errors (25,984 build jobs including Mathlib), and the file prints

```
'Roadmap.rh_of_three_inputs' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The three inputs are hypotheses of `rh_of_three_inputs`. Their proofs are in the full archive and are not part of the slimmed copy. The keep lists contain declaration names and line ranges only, no archive source text. Running the slicer again on the archive reproduces the tested copy file for file.

After step 2 above:

```
rh-lean-roadmap/lean/slim/make_slim.sh lean slim
cd slim && lake exe cache get && lake build +Supplements.Roadmap
```

## Verification status

On 21 November 2026 the Lean FRO and the Mathlib Initiative published a [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/): "We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct, and we congratulate him on this achievement." It lists four checks: the statement is Mathlib's `RiemannHypothesis`, vetted by experts in Lean and number theory; dozens of people compiled the archive without errors; `comparator` and `con-leche --compare` match the proved theorem with Mathlib's statement exactly; and the exported proof was accepted by Lean's kernel, by `con-leche` and `con-ron` (which carry a formal proof, relative to set theory, that they cannot accept a false proof) and by other independent checkers.

Sutherland's report (page last updated 2026-11-21 12:55 UTC) records the individual runs: all 175,187 modules compile; the five main theorems use only the three standard axioms; `leanchecker` and lean4lean replay every module; nanoda and con-leche accept the full export, and `con-leche --compare` justifies the five statements. Sutherland also joined the proof to [Robin1984](https://github.com/kimihiro64/Robin1984), an independent Lean formalization of Robin's and Lagarias's criteria; the joined proof gives Robin's inequality σ(*n*) < e^γ *n* log log *n* for every *n* > 5040 and Lagarias's inequality σ(*n*) ≤ *H*<sub>*n*</sub> + e^*H*<sub>*n*</sub> log *H*<sub>*n*</sub> for every *n* ≥ 1, statements about divisor sums and harmonic numbers alone, and nanoda and con-leche accept it. At that time Lean's default and paranoid kernels were replaying the export and an end-to-end `lake comparator` run was in progress. The report has the current state.

## Related work

[grh-lean](https://github.com/lsernau/grh-lean), released on 25 November 2026 by Luke Sernau with colleagues at Anthropic and Claude, is a shorter Lean rewriting of Alpöge's proof under the Apache 2.0 licence: a readable edition of about 300,000 lines of code with a reading guide, and a compact edition of about 76,000 lines. Its README says that it follows the method of the original proof, that many steps are proved by other arguments, and that no mathematician has read it through. On 26 November 2026 an independent check of the compact edition, run by an AI agent on a University of Waterloo compute allocation, reported that all 794 modules compile and that the five main theorems are accepted by Lean's default and paranoid kernels, lean4lean, nanoda, con-leche and con-ron, using only the three standard axioms ([check record](https://mrubinst.github.io/grh-lean-compact-check/)). The book and the slimmed copy in this repository follow Alpöge's original archive, and their Lean references point to that archive.

## Sources

- L. Alpöge, remark and Lean archive: <https://alpo.ge/remark.pdf>, <https://alpo.ge/lean.tar.gz.part01> … `part14`
- A. V. Sutherland, verification report: <https://math.mit.edu/~drew/grh/>
- Lean and Mathlib communities, joint statement of 21 November 2026: <https://leanprover-community.github.io/blog/posts/riemann-hypothesis/>
- T. Tao, blog post of 20 November 2026: <https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/>

## Licence

Text, web pages and video (`docs/`, `paper/`, `web/`, `video/`, `index.html`, this README): [CC BY 4.0](LICENSE). Lean file (`lean/`): [Apache-2.0](lean/LICENSE). These licences cover this repository; the Alpöge archive is separate.

---

## 中文简介

2026 年 11 月 20 日，Levent Alpöge 公布了和 Claude 一起完成的黎曼猜想与狄利克雷 GRH 的 Lean 证明。证明是一份 Lean 档案，17.5 万个文件、1740 万行，没有注释。几个独立的检查器已经接受了它，11 月 21 日 Lean FRO 和 Mathlib Initiative 发表联合声明，确认黎曼猜想的命题和证明都正确；Sutherland 还把它和另一个独立的形式化项目接在一起，推出了 Robin 不等式（所有 n > 5040）和 Lagarias 不等式（所有 n ≥ 1），这两个命题只讲约数和与调和数，不出现 ζ 函数。本仓库把证明写成数学家能读的文字，每条陈述都对应到档案里的定理和位置：

- `docs/book.pdf`：成文稿（英文），正文 497 页，附录 963 页放较长的证明，另附 Lean 声明索引（共 1582 页）。按证明使用的顺序写出它需要的每条陈述，书末索引按陈述编号列出证明它的 Lean 声明；为这个证明新做的论证都给出了证明，长证明放在附录、正文给出思路；已发表的结果按档案用到的形式陈述并引用。文字主要由 AI 模型写成，还没有人类专家审读过；文字与档案不一致时以 Lean 档案为准；其中明确标为“Proof (outline)”的 63 处（全部在第八部分）列在 `docs/outline-proofs.md`，每处末尾写明给出完整证明的 Lean 声明；脚本检查过全书证明之间的引用与交叉引用，无循环论证、无未定义引用；
- `docs/reading-guide-zh.pdf`：中文解读版（21 页），六步讲完证明，每一步对应到档案里的定理和位置，附录列出全部引用声明的完整位置；`docs/reading-guide-en.pdf` 是英文版；
- `paper/roadmap.pdf`：7 页英文导读，把证明顶层的五步和档案里的具体声明一一对上；
- `web/index.html`：中英双语的讲故事版，不需要数学背景，在线阅读：<https://rh-lean-roadmap.github.io/rh-lean-roadmap/web/>；
- `video/east-of-the-line.mp4`：75 秒竖屏短视频（纯文字介绍、原创背景音乐），附两张封面；
- `lean/Roadmap.lean`：一个小 Lean 文件，只用档案自己的定理串出“三个输入 ⇒ 黎曼猜想”，在档案里编译通过，只依赖三条标准公理；
- `lean/slim/`：把档案切到 `Roadmap.lean` 实际用到的部分（175,188 个文件中的 18,096 个，1,737 万行中的 317 万行），切出来的精简版编译零报错，同样只依赖三条标准公理。三个输入本身的证明仍在完整档案里，精简版不包含。清单里只有声明名和行号，不含档案源码。
- 相关工作：Luke Sernau 与 Anthropic 的同事和 Claude 于 2026 年 11 月 25 日发布的 [grh-lean](https://github.com/lsernau/grh-lean) 是 Alpöge 证明的一个更短的 Lean 重写（Apache 2.0 许可）：可读版约 30 万行代码，附阅读指南；紧凑版约 7.6 万行。它的 README 说明它沿用原证明的方法，许多步骤换用了别的论证，还没有数学家通读过。2026 年 11 月 26 日，一次在滑铁卢大学计算配额上由 AI 代理运行的独立检查报告：紧凑版 794 个模块全部编译通过，五条主定理被 Lean 默认内核、paranoid 内核、lean4lean、nanoda、con-leche 和 con-ron 全部接受，只依赖三条标准公理（[检查记录](https://mrubinst.github.io/grh-lean-compact-check/)）。本仓库的成文稿和精简副本依据 Alpöge 的原始档案，Lean 引用指向原档案。

证明本身是 Alpöge 的档案。档案没有许可证，上面给了从作者网站下载、校验和编译的步骤。本仓库由一位不做这个方向的独立作者定方向、做取舍，文字和代码由多个 AI 模型（其中包括 Anthropic 的 Claude）写成并交叉核对；Alpöge 在 Anthropic 工作，本仓库独立于他和 Anthropic。
