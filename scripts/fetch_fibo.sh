#!/usr/bin/env bash
# Reconstitute fibo-source/ (gitignored) as a sparse, blob-filtered clone pinned to the
# commit recorded in fibo-source.pin. Lets a fresh checkout rebuild the ETL inputs with one step.
set -euo pipefail

DOMAINS="FND LOAN FBC BE SEC DER IND MD BP CAE"
SHA="$(grep '^commit:' fibo-source.pin | awk '{print $2}')"
REPO="https://github.com/edmcouncil/fibo.git"

if [ ! -d fibo-source/.git ]; then
  git clone --filter=blob:none --no-checkout "$REPO" fibo-source
fi

git -C fibo-source sparse-checkout init --cone
git -C fibo-source sparse-checkout set $DOMAINS
# fetch the exact pinned commit (falls back to master if the host won't serve it directly)
git -C fibo-source fetch --filter=blob:none origin "$SHA" 2>/dev/null || git -C fibo-source fetch origin master
git -C fibo-source checkout "$SHA" 2>/dev/null || git -C fibo-source checkout FETCH_HEAD

echo "FIBO checked out at $(git -C fibo-source rev-parse --short HEAD) (pinned: ${SHA:0:7})"
