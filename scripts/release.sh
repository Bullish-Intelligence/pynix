#!/usr/bin/env bash
# release.sh: the release job of pynix. The names are proposed.
#
# Usage: scripts/release.sh [--skip-status] TAG        (TAG is pynix-vX.Y.Z or pynix-vX.Y.Z-rc.N)
#
# Run it through the devenv (devenv shell -- scripts/release.sh TAG) from a clean checkout of the commit to tag. The
# devenv gives the Git identity, uv, and the pinned tools. The job never pushes.
#
# Steps:
#   0  refuse unless `testee status` of the commit at HEAD is GREEN (by commit id: jj does not know `HEAD`);
#      then run `uv sync --locked`, so the job has its own Python environment (Testee does not run for this script)
#   1  build .#manifests, .#libraries, .#packageNames; check that src/ equals them (scripts/check_generated.sh)
#   2  run the 11 gates with the canaries (gates/run_gates.sh)
#   3  write provenance/ and the changelog text
#   4  commit provenance/ and CHANGELOG.md as one release commit
#   5  make the manifest artifact: a commit with no parent that holds the three manifests; annotated tag manifests/TAG
#   6  make the annotated tag TAG on the release commit; its message holds the changelog, the gate line, and the hashes
#   7  print the push command; the job does not push
#
# --skip-status skips step 0. Use it only to test this script on a scratch clone, where no verdict exists.
#
# Environment:
#   PYNIX_RELEASE_WORK  work directory (default: a new directory under $TMPDIR; the job deletes it at the end)
#   PYNIX_RELEASE_LOG   directory for the raw logs (default ${XDG_STATE_HOME:-~/.local/state}/pynix-release/TAG)
#
# Exit codes: 0 released; 2 wrong use or a failed precondition; 4 a step failed. A failed step after step 4 undoes the
# commit and the tags. A release with no change since the previous tag is allowed (owner, 010-D53).
set -euo pipefail
export PYTHONDONTWRITEBYTECODE=1

skip_status=0
tag=
while [ $# -gt 0 ]; do
  case "$1" in
    --skip-status) skip_status=1; shift ;;
    -*) echo "release: unknown option $1" >&2; exit 2 ;;
    *) [ -z "$tag" ] || { echo "release: one TAG only" >&2; exit 2; }; tag=$1; shift ;;
  esac
done
[ -n "$tag" ] || { sed -n 2,3p "$0" >&2; exit 2; }
if [[ ! $tag =~ ^pynix-v[0-9]+\.[0-9]+\.[0-9]+(-rc\.[0-9]+)?$ ]]; then
  echo "release: the tag must look like pynix-vX.Y.Z or pynix-vX.Y.Z-rc.N, not $tag" >&2
  exit 2
fi
version=${tag#pynix-v}
mtag=manifests/$tag

root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
pyver=$(sed -n 's/^version = "\(.*\)"$/\1/p' pyproject.toml | head -1)
[ "$pyver" = "${version%%-*}" ] || { echo "release: the tag $tag does not match version $pyver in pyproject.toml" >&2; exit 2; }
log=${PYNIX_RELEASE_LOG:-${XDG_STATE_HOME:-$HOME/.local/state}/pynix-release/$tag}
mkdir -p "$log"
if [ -n "${PYNIX_RELEASE_WORK:-}" ]; then
  work=$PYNIX_RELEASE_WORK
  keep_work=1
else
  work=$(mktemp -d "${TMPDIR:-/tmp}/pynix-release.XXXXXX")
  keep_work=0
fi
rm -rf "$work"
mkdir -p "$work"

say() { echo "[release $tag] $*" | tee -a "$log/run.txt"; }
die() { say "STOP: $*"; exit 4; }

orig=
committed=0
made_tags=()
cleanup() {
  rc=$?
  if [ "$rc" != 0 ] && [ "$rc" != 3 ]; then
    for t in "${made_tags[@]}"; do git tag -d "$t" >/dev/null 2>&1 || true; done
    if [ "$committed" = 1 ] && [ -n "$orig" ]; then
      git reset --hard -q "$orig" && say "undid the release commit (back to $orig)"
    fi
    [ "$rc" = 2 ] || [ "$rc" = 4 ] || { say "STOP: a command failed (exit $rc); see $log"; rc=4; }
  fi
  [ "$keep_work" = 1 ] || rm -rf "$work"
  exit "$rc"
}
trap cleanup EXIT

# --- preconditions ----------------------------------------------------------------------------------------------
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "release: not a Git work tree" >&2; exit 2; }
[ -z "$(git status --porcelain)" ] || { echo "release: the checkout is not clean; use a clean checkout of the commit to tag" >&2; exit 2; }
git var GIT_AUTHOR_IDENT >/dev/null 2>&1 && git var GIT_COMMITTER_IDENT >/dev/null 2>&1 \
  || { echo "release: no Git identity; run through the devenv (devenv shell -- scripts/release.sh $tag)" >&2; exit 2; }
for t in "$tag" "$mtag"; do
  git rev-parse -q --verify "refs/tags/$t" >/dev/null && { echo "release: the tag $t exists; a release tag never moves" >&2; exit 2; }
done
orig=$(git rev-parse HEAD)
say "start: HEAD $orig, work $work"

# --- 0. the verdict of Testee ----------------------------------------------------------------------------------
if [ "$skip_status" = 1 ]; then
  say "0 testee status skipped (--skip-status: test use only)"
else
  head=$(git rev-parse HEAD)
  testee status -r "$head" >"$log/testee-status.txt" 2>&1 || { cat "$log/testee-status.txt" >&2; die "testee status -r $head is not GREEN"; }
  say "0 testee status GREEN: $(tail -1 "$log/testee-status.txt")"
fi

# --- 0. the Python environment ----------------------------------------------------------------------------------
# A new devenv Python makes devenv create an empty venv. Testee runs `setup:sync` for itself, but not for this script.
say "0 uv sync --locked"
uv sync --locked >"$log/uv-sync.txt" 2>&1 || { tail -5 "$log/uv-sync.txt" >&2; die "uv sync --locked failed (see $log/uv-sync.txt)"; }
PY=$(uv run --no-sync python -c 'import sys; print(sys.executable)') || { echo "release: no uv environment; run uv sync" >&2; exit 2; }
export PY

# --- the previous release ---------------------------------------------------------------------------------------
# The highest release tag below TAG, in version order (a release candidate sorts below its release).
prev=$("$PY" -I - "$tag" $(git tag -l 'pynix-v*' || true) <<'PYEOF'
import re
import sys

def key(t):
    m = re.fullmatch(r"pynix-v(\d+)\.(\d+)\.(\d+)(?:-rc\.(\d+))?", t)
    return (int(m[1]), int(m[2]), int(m[3]), 1 if m[4] is None else 0, int(m[4] or 0)) if m else None

tag, others = sys.argv[1], sys.argv[2:]
below = sorted((t for t in others if key(t) and key(t) < key(tag)), key=key)
print(below[-1] if below else "")
PYEOF
)
prev_dir=$work/prev
if [ -n "$prev" ]; then
  git rev-parse -q --verify "refs/tags/manifests/$prev" >/dev/null || die "the previous release $prev has no tag manifests/$prev"
  mkdir -p "$prev_dir/manifests"
  for m in nixos home-manager flake-parts; do git show "manifests/$prev:$m.json" >"$prev_dir/manifests/$m.json"; done
  git show "$prev:provenance/inputs.json" >"$prev_dir/inputs.json"
  git show "$prev:src/pynix_pkgs/names.json" >"$prev_dir/names.json"
  "$PY" -I - "$prev_dir" <<'PYEOF' || die "the artifact of the previous release differs from its provenance"
import hashlib
import json
import sys
from pathlib import Path

d = Path(sys.argv[1])
want = json.loads((d / "inputs.json").read_text())["manifests"]
for name, digest in want.items():
    got = hashlib.sha256((d / "manifests" / name).read_bytes()).hexdigest()
    if got != digest:
        sys.exit(f"{name}: artifact {got}, provenance {digest}")
PYEOF
  say "previous release: $prev (artifact equals its provenance)"
else
  say "previous release: none (first release)"
fi

# --- 1. build the outputs; check src/ ---------------------------------------------------------------------------
say "1 nix build .#manifests .#libraries .#packageNames"
manifests=$(nix build --no-link --print-out-paths "path:$root#manifests" 2>>"$log/nix-build.txt") || die "nix build .#manifests failed (see $log/nix-build.txt)"
libraries=$(nix build --no-link --print-out-paths "path:$root#libraries" 2>>"$log/nix-build.txt") || die "nix build .#libraries failed"
names=$(nix build --no-link --print-out-paths "path:$root#packageNames" 2>>"$log/nix-build.txt") || die "nix build .#packageNames failed"
say "1 manifests $manifests; libraries $libraries; packageNames $names"
bash scripts/check_generated.sh >"$log/check-generated.txt" 2>&1 || { cat "$log/check-generated.txt" >&2; die "src/ differs from the generated output (scripts/check_generated.sh)"; }
say "1 $(tail -1 "$log/check-generated.txt")"
[ -z "$(git status --porcelain)" ] || die "a step wrote files into the checkout: $(git status --porcelain | head -3 | tr '\n' ' ')"

# --- 2. the gates -----------------------------------------------------------------------------------------------
say "2 gates with canaries (about 5 minutes)"
set +e
MANIFEST_DIR=$manifests LOGDIR=$log/gates bash gates/run_gates.sh src "$work/gates" >"$log/gates.txt" 2>&1
gate_rc=$?
set -e
gate_line=$(sed -n 2p "$work/gates/summary.txt" 2>/dev/null || true)
gate_line=${gate_line#result: }
say "2 gates exit $gate_rc: $gate_line"
[ "$gate_rc" = 0 ] || { tail -20 "$log/gates.txt" >&2; die "the gates failed (see $log/gates.txt)"; }
"$PY" -I - "$work/gates/summary.json" <<'PYEOF' || die "the gate summary does not hold 11 passing checks"
import json
import sys

s = json.load(open(sys.argv[1]))
ok = s["pass"] and len(s["checks"]) == 11 and all(c["status"] == "PASS" for c in s["checks"])
sys.exit(0 if ok else 1)
PYEOF
[ -z "$(git status --porcelain)" ] || die "the gates wrote files into the checkout"

# --- 3. provenance and changelog --------------------------------------------------------------------------------
say "3 provenance and changelog"
fetch_src() {
  nix eval --raw --impure --expr \
    'let l = (builtins.fromJSON (builtins.readFile '"$root"'/flake.lock)).nodes."'"$1"'".locked; in (builtins.fetchTree l).outPath' 2>>"$log/nix-build.txt"
}
nixpkgs_src=$(fetch_src nixpkgs) || die "cannot read the nixpkgs source"
hm_src=$(fetch_src home-manager) || die "cannot read the Home Manager source"

prov=$work/provenance
mkdir -p "$prov"
sed '1s|.*|library: src|' "$work/gates/summary.txt" >"$prov/gates-summary.txt"
( cd "$manifests" && sha256sum nixos.json home-manager.json flake-parts.json ) >"$prov/manifests.sha256"
"$PY" -I - "$root" "$tag" "$version" "$prov" "$orig" "$("$PY" --version)" <<'PYEOF'
import json
import subprocess
import sys
import tomllib
from pathlib import Path

root, tag, version, prov, commit = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4]), sys.argv[5]


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True).stdout.strip()


lock = json.loads((root / "flake.lock").read_text())["nodes"]
sources = {}
for name in ("nixpkgs", "home-manager", "flake-parts"):
    node = lock[name]["locked"]
    sources[name] = {k: node[k] for k in ("rev", "narHash", "lastModified")}
uv = {p["name"]: p["version"] for p in tomllib.loads((root / "uv.lock").read_text())["package"]}
tools = {name: uv[name] for name in ("pydantic", "pydantic-core", "ruff", "ty")}
tools["python (gates)"] = sys.argv[6].split()[-1]
hashes = dict(line.split()[::-1] for line in (prov / "manifests.sha256").read_text().splitlines())
summary = json.loads((prov.parent / "gates" / "summary.json").read_text())
out = {
    "tag": tag,
    "version": version,
    "commit": commit,
    "manifests": hashes,
    "sources": sources,
    "tools": tools,
    "trees": {
        "src": git("rev-parse", "HEAD:src"),
        "generator": git("rev-parse", "HEAD:src/pynix/generate.py"),
        "runtime": git("rev-parse", "HEAD:src/nixdantic"),
        "decoder": git("rev-parse", "HEAD:src/decoder.nix"),
    },
    "gates": {
        "result": (prov / "gates-summary.txt").read_text().splitlines()[1],
        "canaries": any(c["name"] == "s5-canaries" for c in summary["checks"]),
        "file": "provenance/gates-summary.txt",
    },
    "manifest tag": "manifests/" + tag,
}
(prov / "inputs.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
PYEOF

changelog_args=(--inputs "$prov/inputs.json" --manifests "$manifests" --names "$names/names.json"
  --nixpkgs-src "$nixpkgs_src" --hm-src "$hm_src")
if [ -n "$prev" ]; then
  changelog_args+=(--prev-inputs "$prev_dir/inputs.json" --prev-manifests "$prev_dir/manifests" --prev-names "$prev_dir/names.json"
    --diff-json "$prov/manifest-diff.json")
fi
PYTHONPATH=$root/src "$PY" -B -m pynix.changelog "${changelog_args[@]}" >"$work/changelog.txt" 2>>"$log/changelog.txt" \
  || die "the changelog failed (see $log/changelog.txt)"
say "3 changelog: $(wc -l <"$work/changelog.txt") lines"

# --- 4. the release commit --------------------------------------------------------------------------------------
rm -rf provenance
cp -r "$prov" provenance
{
  echo "# Changelog"
  echo
  echo "## $tag"
  echo
  echo '```text'
  cat "$work/changelog.txt"
  echo '```'
  if [ -f CHANGELOG.md ]; then
    echo
    sed '1{/^# Changelog$/d}' CHANGELOG.md | sed '1{/^$/d}'
  fi
} >"$work/CHANGELOG.md"
cp "$work/CHANGELOG.md" CHANGELOG.md
git add provenance CHANGELOG.md
git commit -q -m "Release $tag: provenance and changelog" -m "$gate_line"
committed=1
release_commit=$(git rev-parse HEAD)
[ -z "$(git status --porcelain)" ] || die "the release commit left files behind"
say "4 release commit $release_commit (tree $(git rev-parse HEAD^{tree}))"

# --- 5. the manifest artifact: a commit with no parent ----------------------------------------------------------
readme=$work/README.md
echo "Option manifests of $tag: the output of \`nix build .#manifests\` at the tagged commit. This tag holds data, not source." >"$readme"
entries=
for f in nixos.json home-manager.json flake-parts.json; do
  blob=$(git hash-object -w "$manifests/$f")
  entries+=$(printf '100644 blob %s\t%s\n' "$blob" "$f")$'\n'
done
entries+=$(printf '100644 blob %s\tREADME.md\n' "$(git hash-object -w "$readme")")$'\n'
art_tree=$(printf '%s' "$entries" | git mktree)
art_commit=$(git commit-tree "$art_tree" -m "Option manifests of $tag")
{
  echo "Option manifests of $tag"
  echo
  echo "Release tag: $tag. The walk used nixpkgs $(git show "$release_commit:provenance/inputs.json" | "$PY" -I -c 'import json,sys; print(json.load(sys.stdin)["sources"]["nixpkgs"]["rev"])')."
  echo
  sed 's/^/sha256 /' "$prov/manifests.sha256"
} >"$work/mtag-message.txt"
git tag -a "$mtag" -F "$work/mtag-message.txt" "$art_commit"
made_tags+=("$mtag")
say "5 artifact commit $art_commit (tree $art_tree), tag $mtag"

# --- 6. the release tag -----------------------------------------------------------------------------------------
{
  echo "pynix $version"
  echo
  cat "$work/changelog.txt"
  echo
  echo "gates: $gate_line"
  echo "manifests: tag $mtag (commit $art_commit)"
  sed 's/^/sha256 /' "$prov/manifests.sha256"
} >"$work/tag-message.txt"
git tag -a "$tag" -F "$work/tag-message.txt" "$release_commit"
made_tags+=("$tag")
say "6 tag $tag -> $release_commit"
committed=0
made_tags=()

# --- 7. the next command ----------------------------------------------------------------------------------------
art_bytes=$(git rev-list --objects "$mtag" | git pack-objects --stdout -q 2>/dev/null | wc -c)
say "artifact: pack of the manifest tag $art_bytes bytes"
say "released $tag (release commit $release_commit, manifests $art_commit)"
cat <<EOF

Released $tag. Nothing was pushed. Push the tags to origin:

  git push origin $tag $mtag

The release commit descends from the tested commit. Keep it on the branch (fast-forward main to $release_commit)
so that the next release finds provenance/ and CHANGELOG.md.
EOF
