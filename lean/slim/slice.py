"""Build a slimmed copy of the Alpöge archive keeping only declarations reached from Roadmap.rh_of_three_inputs.

Usage: python slice.py ORIG_ARCHIVE_DIR REACH_TSV OUT_DIR [EXTRA_KEEP_TSV] [DROP_OPEN_TSV]
  REACH_TSV rows: module \t startLine \t endLine \t name   (startLine 0 = no range)
  EXTRA_KEEP_TSV (optional, same format): declarations added back after compile errors.
"""
import os, re, sys, shutil, collections, json

ORIG, REACH, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
EXTRA = sys.argv[4] if len(sys.argv) > 4 else None
DROPOPEN = sys.argv[5] if len(sys.argv) > 5 else None
drop_open = collections.defaultdict(set)
if DROPOPEN and os.path.exists(DROPOPEN):
    for l in open(DROPOPEN, encoding="utf-8"):
        p_ = l.rstrip("\n").split("\t")
        if len(p_) == 2: drop_open[p_[0]].add(p_[1])
SRC = os.path.join(ORIG, "src")
KEEP_ELAB = os.environ.get("KEEP_ELAB", "0") == "1"
AXIOMS = collections.defaultdict(set)   # module -> set of 1-based start lines of declarations to turn into axioms
if os.environ.get("AXIOMS"):
    for _l in open(os.environ["AXIOMS"], encoding="utf-8"):
        _q = _l.rstrip("\n").split("\t")
        if len(_q) >= 2 and _q[1].isdigit(): AXIOMS[_q[0]].add(int(_q[1]))

def axiomize(block_lines):
    """Keep a theorem's statement and drop its proof: cut at the first ':=' outside brackets,
    and replace the keyword theorem/lemma by axiom."""
    text = "\n".join(block_lines)
    depth = 0; cut = None
    for i, ch in enumerate(text):
        if ch in "([{⦃⟨": depth += 1
        elif ch in ")]}⦄⟩": depth -= 1
        elif ch == ":" and depth == 0 and text[i:i + 2] == ":=":
            cut = i; break
    if cut is None: return block_lines
    head = text[:cut].rstrip()
    head = re.sub(r"\b(theorem|lemma)\b", "axiom", head, count=1)
    return head.split("\n") + [""]
STD = ("Mathlib", "Init", "Lean", "Std", "Batteries", "Aesop", "Qq", "ProofWidgets", "Plausible", "ImportGraph", "LeanSearchClient")

def mpath(m): return os.path.join(SRC, *m.split(".")) + ".lean"

ranges = collections.defaultdict(list); names = set()
for fn in [REACH] + ([EXTRA] if EXTRA and os.path.exists(EXTRA) else []):
    for line in open(fn, encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) < 4: continue
        m, s, e, n = p[0], int(p[1]), int(p[2]), p[3]
        names.add(n)
        if s > 0: ranges[m].append((s, e))
ranges["Supplements.Roadmap"].append((1, 10 ** 9))   # keep the roadmap file whole
AUXRE = re.compile(r"(eq|match|proof|simp|unfold|sizeOf|rec|recOn|casesOn|brecOn|below|noConfusion|noConfusionType|inj|injEq|mk|ext|ext_iff|eq_def|congr_simp|eq_\d+|match_\d+|proof_\d+)(_\d+)*")
def parent_of(n):
    parts = n.split(".")
    while parts and (parts[-1].startswith("_") or AUXRE.fullmatch(parts[-1])): parts = parts[:-1]
    return ".".join(parts)
keep_by_name = collections.defaultdict(set)
_rows = [l.rstrip("\n").split("\t") for l in open(REACH, encoding="utf-8")]
_with = {r[3] for r in _rows if len(r) > 3 and r[1] != "0"}
for r in _rows:
    if len(r) > 3 and r[1] == "0":
        pa = parent_of(r[3])
        if pa and pa not in _with:
            keep_by_name[r[0]].add(pa.split(".")[-1]); kept_mods_extra = None
FULLKEEP_F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "full_keep.txt")
FULL = set(l.strip() for l in open(FULLKEEP_F, encoding="utf-8") if l.strip()) if os.path.exists(FULLKEEP_F) else set()
if os.environ.get("FULLALL") == "1":
    FULL = None   # resolved after kept_mods is known
if FULL and os.environ.get("FULLALL") != "1":
    for _n in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "full_names.json"))):
        names.add(_n)
    for _m in FULL: ranges[_m].append((1, 10 ** 9))
kept_mods = set(ranges)
if os.environ.get("KEEPALL"):
    # keep every module of the import closure with its imports unchanged; only declarations inside are pruned
    kept_mods |= set(l.strip() for l in open(os.environ["KEEPALL"], encoding="utf-8") if l.strip())
if FULL is None:
    FULL = set(kept_mods)
LIB_ROOTS = set(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib_roots.json"))))
LIB_ROOTS |= {"Nat", "Int", "List", "Array", "Fin", "Option", "String", "Std", "Lean", "Function", "Classical",
              "Decidable", "Eq", "Prod", "Sum", "Subtype", "Bool", "Char", "Float", "IO", "Except", "Id", "Quot", "Quotient"}
alive_ns = set()
for n_ in names:
    parts = n_.replace("_root_.", "").split(".")
    for i in range(len(parts) - 1):
        for j in range(i + 1, len(parts)):
            alive_ns.add(".".join(parts[i:j]))
ARCH_ROOTS = set(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "archive_roots.json"))))
def ns_dead(t):
    t = t.replace("_root_.", "")
    r0 = t.split(".")[0]
    if r0 in LIB_ROOTS or r0 not in ARCH_ROOTS: return False
    return t not in alive_ns
short_names = collections.defaultdict(set)
for n in names:
    parts = n.split(".")
    for k in range(1, len(parts) + 1): short_names[".".join(parts[-k:])].add(n)

def read_imports(m):
    out = []
    for ln in open(mpath(m), encoding="utf-8", errors="replace"):
        t = ln.split()
        if not t: continue
        if t[0] in ("public", "private", "meta"): t = t[1:]
        if t[:1] == ["meta"]: t = t[1:]
        if t[:1] != ["import"]:
            if out: break
            continue
        out += [x for x in t[1:] if x != "all"]
    return out

_flat = {}
def flat_imports(m, stack=()):
    """Imports of module m, with dropped archive modules replaced by their own (flattened) imports."""
    res = []
    for x in read_imports(m):
        if x.startswith(STD) or x in kept_mods or not os.path.exists(mpath(x)):
            res.append(x)
        else:
            if x not in _flat:
                _flat[x] = flat_imports(x, stack + (x,)) if x not in stack else []
            res += _flat[x]
    seen, out = set(), []
    for x in res:
        if x not in seen: seen.add(x); out.append(x)
    return out

CONT = ("termination_by", "decreasing_by", "where", "deriving", "|")
DECL = re.compile(r"^(@\[[^\]]*\]\s*)*((private|protected|noncomputable|scoped|nonrec|partial|unsafe)\s+)*"
                  r"(theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque|axiom)\b")
PREFIX = re.compile(r"^((set_option|include|omit|open|variable)\b.*\bin\s*$|@\[[^\]]*\]\s*$|(private|protected|noncomputable)\s*$)")
DROP = re.compile(r"^(example\b|#print\b|#check\b|#eval\b|#exit\b|#guard\b)")

def merge_open_continuations(out):
    res = []
    for ln in out:
        if res and res[-1].startswith("open ") and ln[:1] in (" ", "\t") and ln.strip() and not res[-1].rstrip().endswith(" in"):
            res[-1] = res[-1].rstrip() + " " + ln.strip()
        else:
            res.append(ln)
    return res

def overlaps(a, b, ivs):
    return any(not (e < a or s > b) for s, e in ivs)

def slice_file(m):
    lines = open(mpath(m), encoding="utf-8", errors="replace").read().split("\n")
    body_start = 0
    for i, ln in enumerate(lines):
        t = ln.split()
        if t and (t[0] == "import" or (t[0] in ("public", "private", "meta") and "import" in t[:3])): body_start = i + 1
        elif t and body_start: break
    starts = [i for i in range(body_start, len(lines))
              if lines[i] and not lines[i][0].isspace() and not lines[i].startswith(CONT)]
    blocks = [(s, (starts[k + 1] if k + 1 < len(starts) else len(lines))) for k, s in enumerate(starts)]
    ivs = ranges.get(m, [])
    out, pending, stats = [], [], collections.Counter()
    if m in FULL:
        out = merge_open_continuations(lines[body_start:])
        if drop_open.get(m):
            fx = []
            for ln in out:
                if ln.startswith("open ") and not ln.startswith("open private"):
                    toks = ln.split()
                    if "(" in ln and len(toks) > 1 and toks[1] in drop_open[m]: continue
                    kt = [t for t in toks[1:] if t not in drop_open[m]]
                    if len(kt) < len(toks) - 1:
                        if not kt or kt == ["in"]: continue
                        ln = "open " + " ".join(kt)
                fx.append(ln)
            out = fx
        stats["full_kept_modules"] += 1
        return ["import " + x for x in flat_imports(m)] + [""] + out, stats
    for s, e in blocks:
        head = lines[s]
        text = lines[s:e]
        only_blank = all(not x.strip() for x in lines[s + 1:e])
        joined = " ".join(x.strip() for x in lines[s:e] if x.strip())
        multi_open_prefix = head.startswith(("open ", "set_option ", "variable ", "include ", "omit ")) and re.search(r"\bin$", joined) is not None
        if (PREFIX.match(head) and only_blank) or multi_open_prefix:
            pending.append((s, e)); continue
        if DROP.match(head):
            pending = []; stats["dropped_other"] += 1; continue
        if DECL.match(head):
            ls, le = (pending[0][0] if pending else s) + 1, e    # 1-based inclusive
            mid = re.search(r"\b(theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque|axiom)\s+([^\s:(\[{]+)", head)
            declared = mid.group(2).split(".")[-1] if mid else None
            attrs = " ".join(lines[ps] for ps, _ in pending) + " " + head
            elab_only = KEEP_ELAB and (re.search(r"\b(instance)\b", head.split(":=")[0].split("where")[0]) or
                                       re.search(r"@\[[^\]]*\b(simp|ext|coe|norm_cast|push_cast|reducible|instance|simps|elab_as_elim|induction_eliminator|cases_eliminator|default_instance|macro_inline|inline|irreducible)\b", attrs))
            if overlaps(ls, le, ivs) or (declared and declared in keep_by_name.get(m, ())) or elab_only:
                if elab_only and not overlaps(ls, le, ivs): stats["kept_elab_only"] += 1; stats["kept_elab_lines"] += le - ls + 1
                for ps, pe in pending: out += lines[ps:pe]
                if (s + 1) in AXIOMS.get(m, ()) and re.search(r"\b(theorem|lemma)\b", head):
                    out += axiomize(text); stats["axiomized"] += 1
                else:
                    out += text
                stats["kept_decl"] += 1
            else:
                stats["dropped_decl"] += 1
            pending = []; continue
        for ps, pe in pending: out += lines[ps:pe]
        pending = []
        if head.startswith("attribute "):
            mm = re.match(r"^(attribute\s+\[[^\]]*\]\s*)(.*)$", head)
            if mm and only_blank:
                ids = [x for x in mm.group(2).split() if x]
                keep = ids if KEEP_ELAB else [x for x in ids if x in short_names]
                if keep: out.append(mm.group(1) + " ".join(keep)); stats["kept_attr"] += 1
                else: stats["dropped_attr"] += 1
                continue
        out += text; stats["kept_struct"] += 1
    out = merge_open_continuations(out)
    if drop_open.get(m):
        fixed = []
        for ln in out:
            if ln.startswith("open ") and not ln.startswith("open private"):
                toks = ln.split()
                if "(" in ln and len(toks) > 1 and toks[1] in drop_open[m]: continue
                kept_t = [t for t in toks[1:] if t not in drop_open[m]]
                if len(kept_t) < len(toks) - 1:
                    if not kept_t or kept_t == ["in"]: continue
                    ln = "open " + " ".join(kept_t)
            fixed.append(ln)
        out = fixed
    declared_here = set()
    for ln in out:
        if ln.startswith("namespace "):
            t_ = ln.split()
            if len(t_) > 1: declared_here.add(t_[1])
    if KEEP_ELAB:
        fixed3 = []
        for ln in out:
            mm = re.match(r"^open\s+(scoped\s+)?([^()]*?)(\s+in)?\s*$", ln)
            if mm and "hiding" not in ln and "renaming" not in ln and "=>" not in ln and not ln.startswith("open private") and " from " not in ln:
                toks = mm.group(2).split()
                live = [t for t in toks if not ns_dead(t) or t in declared_here]
                if len(live) < len(toks):
                    stats["dead_ns_removed"] += len(toks) - len(live)
                    if not live:
                        continue
                    ln = "open " + (mm.group(1) or "") + " ".join(live) + (mm.group(3) or "")
            fixed3.append(ln)
        out = fixed3
    fixed2 = []
    for ln in out:
        mm = re.match(r"^(open\s+)(\S+)(\s*)\(([^)]*)\)(.*)$", ln)
        if mm:
            ns_, ids = mm.group(2), mm.group(4).split()
            r0_ = ns_.replace("_root_.", "").split(".")[0]
            lib_ns = r0_ in LIB_ROOTS or r0_ not in ARCH_ROOTS
            keep_ids = [x for x in ids if lib_ns or (ns_ + "." + x) in names]
            if not keep_ids:
                stats["dropped_open_list"] += 1
                continue
            if len(keep_ids) < len(ids):
                ln = mm.group(1) + ns_ + " (" + " ".join(keep_ids) + ")" + mm.group(5); stats["trimmed_open_list"] += 1
        fixed2.append(ln)
    out = fixed2
    imps = flat_imports(m)
    return ["import " + x for x in imps] + [""] + out, stats

def main():
    if os.path.exists(os.path.join(OUT, "src")): shutil.rmtree(os.path.join(OUT, "src"))
    os.makedirs(os.path.join(OUT, "src"))
    for f in ("lakefile.toml", "lean-toolchain", "lake-manifest.json"):
        shutil.copy(os.path.join(ORIG, f), os.path.join(OUT, f))
    os.makedirs(os.path.join(OUT, ".lake"), exist_ok=True)
    if os.path.isdir(os.path.join(ORIG, ".lake", "packages")) and not os.path.exists(os.path.join(OUT, ".lake", "packages")):
        os.symlink(os.path.join(ORIG, ".lake", "packages"), os.path.join(OUT, ".lake", "packages"))
    total = collections.Counter(); nlines = 0
    for m in sorted(kept_mods):
        if not os.path.exists(mpath(m)): continue
        body, st = slice_file(m); total.update(st)
        dst = os.path.join(OUT, "src", *m.split(".")) + ".lean"
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w", encoding="utf-8").write("\n".join(body).rstrip() + "\n")
        nlines += len(body)
    json.dump({"modules": len(kept_mods), "lines": nlines, **total}, open(os.path.join(OUT, "slice_stats.json"), "w"), indent=1)
    print("modules", len(kept_mods), "lines", nlines, dict(total))

main()
