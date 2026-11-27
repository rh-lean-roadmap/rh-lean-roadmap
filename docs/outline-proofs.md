# Proofs given in outline

The book (`docs/book.pdf`) gives every statement the proof of RH and GRH needs. The proofs listed below are given in outline: each is headed “Proof (outline)”, states its steps precisely, and ends by naming the Lean declaration of the archive that contains the complete proof. The other proofs are written out; where one of them compresses a step, the Lean declarations cited for the statement prove it.

| Statement | Title | Lean declaration with the complete proof |
|---|---|---|
| Proposition B8.10y | The same-word estimate by leading minors | `GlobalTheory.rowsPos_typeP` |
| Proposition B8.02b-fibre | Weighted fibre over an embedded datum | `GlobalTheory.DegAsm.sum_weights_per_datum` |
| Lemma B8.02yac | Bessel uniqueness under an opposite-sign gap | `CompanionTheory.Bmu.besselMapUniqGap` |
| Proposition B8.02ya | Real Bessel integrals and local proportionality | `ReciprocityTheory.ChartRestriction.DS.Lap.TopClosed.besselNVG`; `CompanionTheory.Lime.BM.wuDecayOfGap_holds'` |
| Lemma B8.10hba | Polynomial contractions between compact types | `GlobalTheory.WigSh.exists_shifted_types_lower_bound` |
| Lemma B8.10hab | Theorem P, compact form | `Formalism.FourierDecayAlt.P.CutSE.actual_compact_theorem` |
| Lemma B8.10hbe | Compact coefficient forms on residual slices | `Formalism.FourierDecayAlt.P.vector_isomorphism_compact_support`; `Formalism.FourierDecayAlt.P.PBASM.rr_top_rep` |
| Proposition B8.10hb | Standardized minor-moment bound on the wave grid | `CompanionTheory.WaveGrid.WEnd.wBp_of`; `CompanionTheory.WaveGrid.WGlue.wLoc1N_of` |
| Lemma B8.10hc | Torus rescaling of local Bessel integrals | `CompanionTheory.WaveGrid.WGlue.w_in_frame` |
| Lemma B8.10h | The weighted sum of real orbital integrals | `CompanionTheory.WaveGrid.weighted_bound_rotated_uniform` |
| Lemma B8.10db | Siegel--Weil generic mass comparison | `GlobalTheory.localMass_le_genericMass_nine`; `GlobalTheory.T.familyGenericMassPositiveBounded_proof` |
| Proposition B8.10dc | Rotated archimedean reduction for corank-one subtotals | `Formalism.MainStatements.RowRest.analytic_pinnedTheoremB_uniform`; `Formalism.MainStatements.RowRest.bDat_theoremB_global` |
| Lemma B8.10d | The two signed corank-one sums | `GlobalTheory.rowNGP_of_siegelWeil`; `GlobalTheory.rowMainEqP_of_siegelWeil` |
| Proposition B8.10ac | Higher-corank loop pair sums | `GlobalTheory.RowsFive.rowsND_of`; `GlobalTheory.RowsFive.rowsDeg_of` |
| Proposition B8.10ad | Represented-frame genus mean and switch partner bounds | `Formalism.MainNotions.BridgeLemma.RowsOne`; `Formalism.L2.SG.RowsU.rowsFU` |
| Lemma B8.10a | Summing the loop pairs | `Formalism.FourierDecayAlt.P.GrowthPolynomialOperator.t_LoopsJoint` |
| Lemma B8.10e | The distinct-word scalar contribution | `Formalism.FourierDecayAlt.P.RealInputsCompactSupport.real_inputs_closed_compact_support_of`; `Formalism.FourierDecayAlt.P.GrowthPolynomialOperator.t_MainRow` |
| Lemma B8.21f | The finite layer-sum denominator estimate | `GlobalTheory.SumSize.Join.sum_size_finite_away_archimedean_combined` |
| Lemma B8.21g | The finite sum estimates | `LeafFixedPointPairing.GlobalTheory.CompanionTheory.LeafFixedPointPlaceNorm.fp_tie_alt` |
| Lemma B8.21h | The base evaluation estimate | `GlobalTheory.QuotientNormCoisometry.leafHeightMapBound_tie_of_infK` |
| Lemma B8.21i | The frame estimate for the evaluation lattice | `GlobalTheory.BigTop.Fun.LeafMMTie.mm_tie_alt` |
| Lemma B8.21j | The square valuation estimate | `GlobalTheory.SqTop.OneSqNoSmall.oneSqSt_of_claims'`; `GlobalTheory.BigTop.Fun.oneSq_of_log_derivative_bound_thA` |
| Lemma B8.21k | The coordinate denominator bound | `GlobalTheory.NormSum.DenomBound.intSt_of_forall_inp` |
| Lemma B8.21l | The lattice norm bound | `GlobalTheory.BigTop.Fun.int_tie_alt` |
| Lemma B8.21ma | The two Galois means | `GlobalTheory.PositiveMeans.means_le`; `GlobalTheory.ArchFree.means.means_le` |
| Lemma B8.21m | The archimedean norm estimate | `GlobalTheory.ArchFree.norm.norm_meanInf_posLog_le`; `GlobalTheory.BigTop.Fun.arch_tie_of_logDeriv_bound` |
| Lemma B8.21n | Existence of a fitted evaluation datum | `GlobalTheory.BigTop.Fun.ex_of_claims_alt` |
| Lemma B8.21o | Comparison map and base kernel on a fitted grid | `GlobalTheory.BigTop.Fun.oneMap_of_bundle_setAt_kernel_conditions`; `GlobalTheory.BigTop.Fun.leafKernel_of_linK_injK_constK_formula2K` |
| Lemma B8.21p | Fitted-grid size, weight, and modulus bounds | `GlobalTheory.BigTop.Fun.wt_tie_alt`; `GlobalTheory.BigTop.Fun.desPol_alt` |
| Proposition B8.26u | Existence of good root towers | `GlobalTheory.CompanionTheory.Ar.Link.good_tower_and_volume_final` |
| Lemma B8.26a | The Hodge test class | `GlobalTheory.CompanionTheory.Ar.Top.slope_lower_of_base_settings` |
| Lemma B8.25gca | Uniform bound for cuspidal theta derivatives | `UpperTheory.Dv.Thin.theta_sup_le` |
| Lemma B8.25gcb | Lower bound for a family of block theta derivatives | `UpperTheory.Dv.Thin.theta_lower` |
| Proposition B8.28u | Column-differential formal-group matching | `GlobalTheory.ColApprox.exists_germ_cols`; `GlobalTheory.ColumnGerm.exists_germ_on_copies` |
| Lemma B8.28vc | Formal connection identities in an integral chart | `ReciprocityTheory.ChartRestriction.G.TB.WickVanishing.Val.harmonic_value_integral`; `ReciprocityTheory.ChartRestriction.G.TB.WickVanishing.Nab.connection_first_identity` |
| Proposition B8.28v | Harmonic valuation lower bound in an integral chart | `GlobalTheory.PlaceInt.chBound_zero_of_isUnit_discr`; `GlobalTheory.PlaceInt.ChartRam.chBound_ramified` |
| Lemma B8.28wa | Mixed translates and the chart lower bound | `GlobalTheory.PlaceInt.TermBound.term_bound` |
| Lemma B8.28xe | Oscillation at split places | `GlobalTheory.RefSum.oscLe_two`; `GlobalTheory.OscSplit.oscLe_split` |
| Lemma B8.28xfa | Frobenius orbits and character minors | `GlobalTheory.CharMinor.colength_bound`; `GlobalTheory.RefSum.hasChars_frame_of_hasAF` |
| Lemma B8.28xga | Typed formal factors | `GlobalTheory.PrimePart.typedPartAt`; `GlobalTheory.PrimePart.formalGroupTypes` |
| Lemma B8.28xgb | Lower depth on an even Frobenius orbit | `GlobalTheory.DepthLow.detDepth_lower`; `GlobalTheory.RefSum.facBetween_fine` |
| Lemma B8.28xhb | Two radii for a typed determinant | `GlobalTheory.FGDepth.InertBound.content_le_detDepth_add` |
| Lemma B8.28yb | A theta family with a controlled harmonic value | `GlobalTheory.PowGerm.lemmaBT_of_characters` |
| Lemma B8.28yc | Integral expansion and the theta normaliser | `GlobalTheory.PowGerm.pointStatements_on_copies`; `GlobalTheory.PtTie.harmonicValue_translate` |
| Proposition B8.28z | Weight-change inequality for reference depths | `GlobalTheory.RefSum.WFree.refExp_vp_le_shift` |
| Lemma B8.42bof-lattices | Residue lattices and the Herr class | `GlobalTheory.Present.RedLat.red_isLat` |
| Lemma B8.42bobk | Model lattices of the canonical residue realization | `GlobalTheory.Models.CharModel.model_chr_eq`; `GlobalTheory.ModelCount.count` |
| Lemma B8.42bobh | The character obstruction | `GlobalTheory.Models.ModTh.hom_chr_eq_zero` |
| Lemma B8.42bob | The \psi-shift dimension estimate and admissible cohomology classes | `GlobalTheory.TopSteps.CharVanish.stmt_of_real`; `GlobalTheory.TopSteps.admissibleUntwistedCharUnramified_of_residueRealisation` |
| Lemma B8.42bqa | Normalization, \Delta-invariant ring relations, and component splitting | `Formalism.MainNotions.N.Ln34.ClassMapPf.classMapPf_of`; `Formalism.MainNotions.N.Ln34.splitR_of_steps` |
| Lemma B8.42bqe | Model comparison and invariant coordinates | `Formalism.MainNotions.N.Ln34.modelflink_pf`; `Formalism.MainNotions.N.Ln34.modelqlink_pf` |
| Proposition B8.42bqc | Frames, slot lifting, and the component bound | `Formalism.MainNotions.N.Ln34.LevelExpansions.mix_local`; `Formalism.MainNotions.N.Ln34.univlink_pf` |
| Lemma B8.42bs1d | The local lifting input at a type prime | `GlobalTheory.TheoremTClosing.main`; `GlobalTheory.InertiaEigenvalues.theoremT_all_records` |
| Lemma B8.42bs1f | The local cut-cocycle bound from either family | `GlobalTheory.Pass.LocDirect.main`; `GlobalTheory.Pass.LocDual.main` |
| Proposition B8.42bs1 | The paired-character estimate at the type primes | `GlobalTheory.ClosingLocalInputs.main_alt_alt` |
| Lemma B8.42bud | Cocycle reduction on the negative components | `Formalism.MainNotions.RamifiedCoefficientChains.S9.LocalLemmasFromLiterature.local_lemmas_of_literature`; `Formalism.MainNotions.N.Pv.LocalLengthBound.rhoLift_of` |
| Lemma B8.42buea | A recursive letter and its interpolation cost | `Formalism.MainNotions.RamifiedCoefficientChains.S9.lemGA_of_pieces`; `Formalism.MainNotions.RamifiedCoefficientChains.S9.lemGB_of` |
| Lemma B8.42bue | First Frobenius correction of the chosen coordinates | `Formalism.MainNotions.N.Pv.LocalLengthBound.pass3`; `Formalism.MainNotions.N.Pv.LocalLengthBound.pass4` |
| Lemma B8.42bv | Separated-cluster lifting and colength bound at unramified primes | `GlobalTheory.T.theoremE_corollaryA_closing_all_data` |
| Lemma B8.42bw | Unrestricted and short-interval coordinate lifting at unramified primes | `Formalism.MainNotions.N.Ln17.sum_alt`; `Formalism.MainNotions.N.Ln17.frobenius_statement_of_fontaine` |
| Lemma B8.42bx | Inert word dichotomy and final-row congruence passage | `GlobalTheory.NLink.starAD_of_global`; `GlobalTheory.NLink.BBSize.main` |
| Lemma B8.50a | Degree of a separated row | `Formalism.MainNotions.GappedMultiplicityBounds.theorem_three_rows_of_real_place` |
| Lemma B8.55b | Independence of comparison values | `GlobalTheory.ClassSumSpan.atDict_indep` |
| Proposition B8.55 | Bounded rows of the indefinite realization | `GlobalTheory.Fc.R1.row_hRB_univ_alt` |
| Proposition B9.19 | Crystalline data | `UpperTheory.Gal.Int.Geo.steps_holds` |

# 以梗概给出的证明

成文稿里下面这些证明只给出梗概：标题写作“Proof (outline)”，每一步都陈述准确，末尾写明档案里给出完整证明的 Lean 声明。其余证明都写出了推导；个别证明里压缩了的步骤，以该陈述对应的 Lean 声明为准。上表按陈述编号列出。

