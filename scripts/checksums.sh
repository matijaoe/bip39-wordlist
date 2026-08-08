#!/usr/bin/env bash
# Rewrite SHA256SUMS from what is on disk.
#
# Run this after adding, removing or changing anything under wordlists/.
# scripts/check.sh fails if SHA256SUMS is stale, so forgetting is caught, but
# the fix belongs in one place rather than a command copied from the readme.
#
#   ./scripts/checksums.sh

set -euo pipefail
cd "$(dirname "$0")/.."

sums=$(command -v sha256sum >/dev/null && echo sha256sum || echo "shasum -a 256")

before=$([ -f SHA256SUMS ] && wc -l < SHA256SUMS | tr -d ' ' || echo 0)
find wordlists -type f ! -name '.DS_Store' | sort | xargs $sums > SHA256SUMS
after=$(wc -l < SHA256SUMS | tr -d ' ')

echo "SHA256SUMS: $after entries (was $before)"
