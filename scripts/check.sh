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
[ -z "$out" ] && note "recorded hashes still match" "ok" || { note "recorded hashes still match" "FAIL"; echo "$out" | while read -r l; do bad "$l"; done; fail=1; }

diff=$(diff <(cut -c67- SHA256SUMS | sort) <(find pdf txt json -type f ! -name '.DS_Store' | sort) || true)
[ -z "$diff" ] && note "every file is recorded in SHA256SUMS" "ok" || { note "every file is recorded in SHA256SUMS" "FAIL"; echo "$diff" | while read -r l; do bad "$l"; done; fail=1; }

miss=""
while read -r url; do
  grep -qF "$url" sources.tsv || miss+="in README but not sources.tsv: $url"$'\n'
done < <(grep -o '\[source\](\([^)]*\))' README.md | sed 's/\[source\](\(.*\))/\1/')
[ -z "$miss" ] && note "every README source url is in sources.tsv" "ok" || { note "every README source url is in sources.tsv" "FAIL"; printf '%s' "$miss" | while read -r l; do bad "$l"; done; fail=1; }

miss=""
while IFS=$'\t' read -r file url; do
  case "$file" in '#'*|'') continue;; esac
  [ -e "$file" ] || miss+="sources.tsv points at a missing file: $file"$'\n'
done < sources.tsv
[ -z "$miss" ] && note "every sources.tsv path exists" "ok" || { note "every sources.tsv path exists" "FAIL"; printf '%s' "$miss" | while read -r l; do bad "$l"; done; fail=1; }

miss=""
while read -r target; do
  case "$target" in http*) continue;; esac
  [ -e "$target" ] || miss+="broken README link: $target"$'\n'
done < <(grep -o '](\([^)]*\))\|src="\([^"]*\)"' README.md | sed 's/](\(.*\))/\1/; s/src="\(.*\)"/\1/')
[ -z "$miss" ] && note "every relative README link resolves" "ok" || { note "every relative README link resolves" "FAIL"; printf '%s' "$miss" | while read -r l; do bad "$l"; done; fail=1; }

echo
[ "$fail" -eq 0 ] && echo "all checks passed" || echo "some checks failed"
exit $fail
