# rh-lean-roadmap

A guide for human readers to the Lean proof of the Riemann hypothesis and of the generalized Riemann hypothesis for Dirichlet *L*-functions, announced by Levent Alpöge on 20 November 2026.

The proof is a Lean 4 archive of 175,187 files and 17.4 million lines, without comments. Several independent checkers have accepted it (see [Sutherland's report](https://math.mit.edu/~drew/grh/)), and on 21 November the Lean and Mathlib communities, with the endorsement of the Lean FRO and the Mathlib Initiative, certified that the statement and the proof are correct ([joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)). This repository writes the argument out for mathematicians and ties every statement to the archive.

| | |
|---|---|
| [`docs/book.pdf`](docs/book.pdf) | The argument written out for mathematicians, in English (422 pages). Every statement the proof needs, in the order the proof uses it, each followed by the location of the Lean declaration that proves it. Arguments made for this proof are given with proofs; published results are stated in the form the archive uses, with references. Nine parts: the window criterion, the prime sum and the auxiliary primes, the divisibility from one theta lift, its accumulation along the chain, the two bounds on one slope, the Tate–Shafarevich window bound, and the three inputs with the Galois representations and the local Langlands correspondence they use. LaTeX sources in `docs/src/book/`. |
| [`docs/reading-guide-en.pdf`](docs/reading-guide-en.pdf) | A reading guide in English (22 pages). The argument in six steps, each tied to the archive's declarations: the prime sum over Frobenius classes, the theta-lift chain and the local computation behind its divisibility, the division of lattices and the two-sided slope estimate that plays the role of Stepanov's inequality, the Tate–Shafarevich window bound, how the three inputs are proved, and in what form the archive proves the published theorems it uses. An appendix gives the location of every declaration cited. |
| [`docs/reading-guide-zh.pdf`](docs/reading-guide-zh.pdf) | The same guide in Chinese (21 pages). LaTeX sources in `docs/src/` (the Chinese version uses the Noto Serif/Sans SC fonts). |
| [`paper/roadmap.pdf`](paper/roadmap.pdf) | Seven pages, in English. The top of the argument in five steps, each tied to declarations in the archive, then the published foundations and the points still to be traced. |
| [`web/index.html`](web/index.html) | A story version for readers with no mathematics, in Chinese and English. Read it online at <https://rh-lean-roadmap.github.io/rh-lean-roadmap/>. |
| [`video/east-of-the-line.mp4`](video/east-of-the-line.mp4) | A 75-second vertical video (Chinese, text only, original background music) for social media, with two cover images. |
| [`lean/Roadmap.lean`](lean/Roadmap.lean) | A small Lean file. Using only the archive's own theorems, it proves inside the archive that three inputs (`Green`, `VWin`, `HypsAlt …`) imply Mathlib's `RiemannHypothesis`. |

## How the book was written

Each chapter was drafted from the Lean source of the declarations it covers, checked against that source by a second model, revised, and checked and revised a second time. Statements follow the Lean statements; where the archive proves a published theorem in a weaker form, the chapter states the form the archive proves. The typewriter font is JetBrains Mono (SIL Open Font License); put `JetBrainsMono.ttf` in `docs/src/book/fonts/` and compile `main.tex` with XeLaTeX or Tectonic.

## About this repository

- The proof is Alpöge's archive; this repository explains its structure. The explanations come from reading the code and Alpöge's [remark](https://alpo.ge/remark.pdf), and the Lean code gives the exact statements.
- The archive carries no licence, so the steps below download it from its author's site and check it.
- An independent author set the direction and made the calls; the text and code were written and cross-checked by several AI models, including Anthropic's Claude. Alpöge works at Anthropic; this repository is independent of him and of Anthropic.

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

## Verification status

On 21 November 2026 the Lean and Mathlib communities published a [joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/), endorsed by the Lean FRO and the Mathlib Initiative: "We have full confidence that Alpöge's proof of the Riemann Hypothesis is correct." It lists four checks: the statement is Mathlib's `RiemannHypothesis`, vetted by experts in Lean and number theory; dozens of people compiled the archive without errors; `comparator` and `con-leche --compare` match the proved theorem with Mathlib's statement exactly; and the exported proof was accepted by Lean's kernel, by `con-leche` and `con-ron` (which carry a formal proof, relative to set theory, that they cannot accept a false proof) and by other independent checkers.

Sutherland's report (page last updated 2026-11-21 12:55 UTC) records the individual runs: all 175,187 modules compile; the five main theorems use only the three standard axioms; `leanchecker` and lean4lean replay every module; nanoda and con-leche accept the full export, and `con-leche --compare` justifies the five statements. Sutherland also joined the proof to [Robin1984](https://github.com/kimihiro64/Robin1984), an independent Lean formalization of Robin's and Lagarias's criteria; the joined proof gives Robin's inequality σ(*n*) < e^γ *n* log log *n* for every *n* > 5040 and Lagarias's inequality σ(*n*) ≤ *H*<sub>*n*</sub> + e^*H*<sub>*n*</sub> log *H*<sub>*n*</sub> for every *n* ≥ 1, statements about divisor sums and harmonic numbers alone, and nanoda and con-leche accept it. At that time Lean's default and paranoid kernels were replaying the export and an end-to-end `lake comparator` run was in progress. The report has the current state.

## Sources

- L. Alpöge, remark and Lean archive: <https://alpo.ge/remark.pdf>, <https://alpo.ge/lean.tar.gz.part01> … `part14`
- A. V. Sutherland, verification report: <https://math.mit.edu/~drew/grh/>
- Lean and Mathlib communities, joint statement of 21 November 2026: <https://leanprover-community.github.io/blog/posts/riemann-hypothesis/>
- T. Tao, blog post of 20 November 2026: <https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/>

## Licence

Text, web page and video (`docs/`, `paper/`, `web/`, `video/`, this README): [CC BY 4.0](LICENSE). Lean file (`lean/`): [Apache-2.0](lean/LICENSE). These licences cover this repository; the Alpöge archive is separate.

---

## 中文简介

2026 年 11 月 20 日，Levent Alpöge 公布了和 Claude 一起完成的黎曼猜想与狄利克雷 GRH 的 Lean 证明。证明是一份 Lean 档案，17.5 万个文件、1740 万行，没有注释。几个独立的检查器已经接受了它，11 月 21 日 Lean 和 Mathlib 社区发表联合声明（Lean FRO 和 Mathlib Initiative 背书），确认命题和证明都正确；Sutherland 还把它和另一个独立的形式化项目接在一起，推出了 Robin 不等式（所有 n > 5040）和 Lagarias 不等式（所有 n ≥ 1），这两个命题只讲约数和与调和数，不出现 ζ 函数。本仓库把证明写成数学家能读的文字，每条陈述都对应到档案里的定理和位置：

- `docs/book.pdf`：成文稿（英文，422 页），按证明使用的顺序写出它需要的每条陈述，后面注明证明它的 Lean 声明；为这个证明新做的论证都给出了证明，已发表的结果按档案用到的形式陈述并引用；
- `docs/reading-guide-zh.pdf`：中文解读版（21 页），六步讲完证明，每一步对应到档案里的定理和位置，附录列出全部引用声明的完整位置；`docs/reading-guide-en.pdf` 是英文版；
- `paper/roadmap.pdf`：7 页英文导读，把证明顶层的五步和档案里的具体声明一一对上；
- `web/index.html`：中英双语的讲故事版，不需要数学背景，在线阅读：<https://rh-lean-roadmap.github.io/rh-lean-roadmap/>；
- `video/east-of-the-line.mp4`：75 秒竖屏短视频（纯文字介绍、原创背景音乐），附两张封面；
- `lean/Roadmap.lean`：一个小 Lean 文件，只用档案自己的定理串出“三个输入 ⇒ 黎曼猜想”，在档案里编译通过，只依赖三条标准公理。

证明本身是 Alpöge 的档案。档案没有许可证，上面给了从作者网站下载、校验和编译的步骤。本仓库由一位独立作者定方向、做取舍，文字和代码由多个 AI 模型（其中包括 Anthropic 的 Claude）写成并交叉核对；Alpöge 在 Anthropic 工作，本仓库独立于他和 Anthropic。
