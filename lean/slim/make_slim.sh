#!/bin/bash
# Build the slimmed copy of the archive.
# Usage: make_slim.sh ARCHIVE_LEAN_DIR OUT_DIR
#   ARCHIVE_LEAN_DIR is the unpacked ./lean directory of the archive, with lean/Roadmap.lean copied to
#   src/Supplements/Roadmap.lean as described in the top-level README.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
ARCH=$(cd "${1:?archive dir}" && pwd); OUT=${2:?output dir}
test -f "$ARCH/src/Supplements/Roadmap.lean" || { echo "copy lean/Roadmap.lean to $ARCH/src/Supplements/Roadmap.lean first" >&2; exit 2; }
gunzip -c "$HERE/reach_ranges.tsv.gz" > "$HERE/reach_ranges.tsv"
for f in extra_keep.tsv full_names.json; do gunzip -c "$HERE/$f.gz" > "$HERE/$f"; done
mkdir -p "$OUT"
KEEP_ELAB=1 python3 "$HERE/slice.py" "$ARCH" "$HERE/reach_ranges.tsv" "$OUT" "$HERE/extra_keep.tsv" "$HERE/drop_open.tsv"
echo "now run:  cd $OUT && lake exe cache get && lake build +Supplements.Roadmap"
