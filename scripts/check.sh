#!/usr/bin/env bash
# Bookkeeping checks: hashes, coverage, and links.
#
# scripts/verify.py checks that the wordlists are correct. This checks that the
# files around them agree with each other. CI runs this exact script, so a green
# tick means the same thing as a clean run here.
#
#   ./scripts/check.sh

set -uo pipefail
cd "$(dirname "$0")/.."

fail=0
note() { printf '  %-46s %s\n' "$1" "$2"; }
bad() { fail=1; printf '    %s\n' "$1"; }

sums=$(command -v sha256sum >/dev/null && echo "sha256sum -c" || echo "shasum -c")

out=$($sums SHA256SUMS 2>&1 | grep -v ': OK$' || true)
[ -z "$out" ] && note "hashes match SHA256SUMS" "ok" || { note "hashes match SHA256SUMS" "FAIL"; echo "$out" | while read -r l; do bad "$l"; done; fail=1; }

diff=$(diff <(cut -c67- SHA256SUMS | sort) <(find wordlists -type f ! -name '.DS_Store' | sort) || true)
[ -z "$diff" ] && note "SHA256SUMS covers every file" "ok" || { note "SHA256SUMS covers every file" "FAIL"; echo "$diff" | while read -r l; do bad "$l"; done; fail=1; }

miss=""
while read -r url; do
  grep -qF "$url" sources.tsv || miss+="in README but not sources.tsv: $url"$'\n'
done < <(grep -o '\[source\](\([^)]*\))' README.md | sed 's/\[source\](\(.*\))/\1/')
[ -z "$miss" ] && note "README sources are in sources.tsv" "ok" || { note "README sources are in sources.tsv" "FAIL"; printf '%s' "$miss" | while read -r l; do bad "$l"; done; fail=1; }

miss=""
while IFS=$'\t' read -r file url; do
  case "$file" in '#'*|'') continue;; esac
  [ -e "$file" ] || miss+="sources.tsv points at a missing file: $file"$'\n'
done < sources.tsv
[ -z "$miss" ] && note "sources.tsv paths exist" "ok" || { note "sources.tsv paths exist" "FAIL"; printf '%s' "$miss" | while read -r l; do bad "$l"; done; fail=1; }

wrapped=$(grep -n '`\[[^]]*\](' README.md || true)
[ -z "$wrapped" ] && note "README links are not inside code spans" "ok" || { note "README links are not inside code spans" "FAIL"; echo "$wrapped" | while read -r l; do bad "line ${l%%:*} renders as text, backticks belong around the label"; done; fail=1; }

miss=""
while read -r target; do
  case "$target" in http*) continue;; esac
  [ -e "$target" ] || miss+="broken README link: $target"$'\n'
done < <(grep -o '](\([^)]*\))\|src="\([^"]*\)"' README.md | sed 's/](\(.*\))/\1/; s/src="\(.*\)"/\1/')
[ -z "$miss" ] && note "README links resolve" "ok" || { note "README links resolve" "FAIL"; printf '%s' "$miss" | while read -r l; do bad "$l"; done; fail=1; }

echo
[ "$fail" -eq 0 ] && echo "all checks passed" || echo "some checks failed"
exit $fail
