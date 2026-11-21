import Formalism.GammaFactorNonvanishing.CritLine
import Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.TopPlug

/-!
# A roadmap through the Alpöge–Claude proof of RH and Dirichlet GRH

This file restates the top of the proof with the archive's own theorems: Riemann's hypothesis
follows from three inputs (`Green`, `VWin`, `HypsAlt …`). The three inputs, the theta-lift
machinery behind them and the published-literature foundations are proved in the rest of the
archive.
-/

open Formalism.BasicNotions Formalism.MainNotions GlobalTheory.Fc

namespace Roadmap

/-- Step 0. The target is Mathlib's own definition of the Riemann hypothesis. -/
example : RiemannHypothesis ↔
    ∀ s : ℂ, riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * (n + 1)) → s ≠ 1 → s.re = 1 / 2 :=
  Iff.rfl

/-- Step 1 (classical). Non-vanishing of every Dirichlet `L`-function on `Re s > 1/2` gives RH:
take the trivial character modulo `1`. The critical-line statements use the functional equation. -/
theorem rh_of_every_character (h : UpperTheory.EveryCharacter) : RiemannHypothesis :=
  Formalism.VW.rh_of_every h

/-- Step 1′ (classical). Primitive characters suffice: an imprimitive `L`-function is the
primitive one times finitely many Euler factors, none of which vanishes on `Re s > 0`. -/
theorem every_character_of_primitive (h : Formalism.HC.ZeroFreeAll) : UpperTheory.EveryCharacter :=
  UpperTheory.Top.imprimitive h

/-- Steps 2–5 (the new argument, as packaged by the archive). Given the three inputs, every
primitive Dirichlet `L`-function has no zero with `Re s > 1/2`. Inside: Landau positivity on
windows `[Y, Y^(3/2)]`, and the Stepanov-type balance with chains of length `m ≥ x^(1/2-ε)`. -/
theorem zero_free_of_three_inputs
    (hG : GlobalTheory.GLq.Green) (hV : UpperTheory.Top.VWin)
    (h : Nonempty (HypsAlt (fun 𝒞 => Closed 𝒞 fun Fm _ => LinkN Fm) DefiniteSideCondition)) :
    Formalism.HC.ZeroFreeAll :=
  UpperTheory.Top.zero_free_all_of_green_v_win hG hV h

/-- The core reduction: the three inputs imply the Riemann hypothesis. -/
theorem rh_of_three_inputs
    (hG : GlobalTheory.GLq.Green) (hV : UpperTheory.Top.VWin)
    (h : Nonempty (HypsAlt (fun 𝒞 => Closed 𝒞 fun Fm _ => LinkN Fm) DefiniteSideCondition)) :
    RiemannHypothesis :=
  rh_of_every_character (every_character_of_primitive (zero_free_of_three_inputs hG hV h))

end Roadmap

/-! The three inputs, as the archive states them. -/
#print GlobalTheory.GLq.Green
#print UpperTheory.Top.VWin
#print UpperTheory.Top.VWinAt
#print Formalism.HC.ZeroFreeAll
#print axioms Roadmap.rh_of_three_inputs
