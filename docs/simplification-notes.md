# Attempts to simplify the proof

November 2026. Several model families proposed ways to shorten the argument or make it more elementary. Each proposal was then tested against the Lean archive and the literature by other models working in isolation. No human expert has checked these notes.

## Adopted in the book

1. **Kato's Euler system is cited directly.** The archive builds the Euler system it needs from Siegel units. The book now cites Kato's theorem (Kato 2004, Theorem 14.2(1)) and keeps only the statements that connect it to the archive's setting.
2. **A shorter proof of the window criterion.** Chapter 4 of the book proves the window criterion (Theorem 3.2) with a Gaussian kernel whose centre is moved inside the window by at most one period of the dominant pair of poles. It replaces about seven pages of estimates for high derivatives of the Laplace transform. A second model checked it step by step and numerically. This proof is not formalised; the archive's proof is in the appendix of the book.

## Possible, not yet done

The archive proves weaker forms of several published theorems for itself. Five such blocks (Kato's construction, the deformation argument behind the vanishing of an adjoint Selmer group, Green's regular characters, the construction of the Galois representations of Part IX, and the cuspidal parameters of the weak local correspondence) take 38 pages of the main text and 73 pages of the appendix. They can be replaced by citations together with bridging statements. The largest block, the Galois representations, needs a bridge that is not yet written: the archive uses general polarizations, local components outside the Iwahori case and arbitrary period rings.

## Ruled out

- **An elementary proof.** Stepanov's method over the integers gives bounds of Chebyshev strength. The short proof of Deligne's theorem over finite fields uses two independent limits (the degree of the field extension and the tensor power) and a Frobenius operator whose eigenvalues are the zeros. Over the rationals there is one scale and no such operator.
- **Cheaper layers.** By the explicit formula, the error term is at least of size the square root of x on every window of fixed logarithmic length. So if the error is x/m plus m to the power a for each of m layers, then a is at least 1. The archive has a = 1, the best exponent of this form.
- **The bound Re s > 2/3 without the Tate–Shafarevich window bound.** Without gluing lattices across Hecke characters, the base term above the two auxiliary primes is strictly negative at every layer. The archive controls exactly this term with the window bound.
- **Half of the Tate–Shafarevich budget from the polarization sign.** The polarization sends the extension from the first scalar block to block e onto a different extension, so it gives no sign on a single block.
- **A reference character ramified at one large prime.** Such a character violates the unramifiedness required at that prime, and the negative base term above the auxiliary primes remains.
- **The large sieve with Landau–Page instead of zero density.** It suffices for the thin positions, which the book already treats this way. The main window still needs a box free of zeros.

## Open

- **Siegel–Weil positivity on definite unitary groups instead of the covolume bound on indefinite Shimura varieties.** The bound needed is one-sided and allows a controlled error, and the archive already proves that a definite theta lift is onto the relevant spectral block. What is missing is an upper bound for the covolume of the integral image.
- **A determinant argument instead of the slope filtration in Part V.** It works for a single embedding. The error budget over all embeddings is not verified.

## An observation

Taking the trivial character and k = 2j in Proposition B6.30 bounds the logarithm of the order of K_{4j}(Z), away from a fixed finite set of primes, by a polynomial in j. This is the shape of bound Soulé conjectured, and much stronger than the bounds known so far. The window bound is therefore a strong arithmetic result in its own right, and it is the part of the proof that resists shortening.

---

# 简化尝试记录（中文）

2026 年 11 月，几家模型分别提出缩短论证或改成更初等证明的办法，再由其他模型在隔离的情况下对照 Lean 档案和文献逐条检验。这份记录没有经过人类专家审读。

**已经用进书里的**：Kato 的 Euler 系改为直接引用 Kato 2004 的定理 14.2(1)；第 4 章用高斯核给出窗口判据的较短证明，替换了约 7 页高阶导数估计。这一证明经另一模型逐步和数值核对，没有形式化，档案原来的证明放在附录。

**可以做、还没做的**：档案自己证明了几条已发表定理的弱化版，其中五大段共占正文 38 页、附录 73 页，可以改为引用加桥接陈述。最大的一段（第九部分的 Galois 表示）还缺一个桥接。

**已经排除的**：初等证明；把每层代价降到 m 的一次方以下（显式公式给出每个窗口里至少根号 x 量级的误差，所以指数至少是 1，档案已经做到 1）；不用 Tate–Shafarevich 窗口界证 Re s > 2/3（两个辅助素数上方的基准项每层都严格为负）；用极化符号让 Sha 只算一半；换成只在一个大素数分歧的参考特征；用大筛法加 Landau–Page 代替零点密度。

**还不确定的**：用定号酉群的 Siegel–Weil 正性代替不定号 Shimura 簇上的余体积界，缺整像余体积的上界；第五部分用行列式代替斜率滤过，全部嵌入上的误差预算没有核实。

**一个观察**：命题 B6.30 取平凡特征和 k = 2j，可以推出 K_{4j}(Z) 的阶（除去固定有限个素数）的对数不超过 j 的多项式。这正是 Soulé 猜想的形状，比已知的界强得多。窗口界本身就是一个很强的算术结果，也是这个证明里最难缩短的部分。
