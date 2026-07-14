#!/usr/bin/env bash
# URANTiOS instruction guards
#
# Mechanically enforces the machine-checkable rules from CLAUDE.md so that
# violations cannot merge regardless of which model produced them.
#
# Fatal checks (exit non-zero):
#   1. Canonical corpus integrity: urantia-book/*.json must match the
#      checksum manifest (tests/corpus.sha256).
#   2. JSON validity: every .json in the repo must parse.
#
# Warning checks (reported, never fatal, because pre-existing prose is not
# retro-edited):
#   3. Em dashes in Markdown outside the canonical corpus.
#   4. Common American spellings in Markdown outside the canonical corpus.
#
# Regenerate the manifest ONLY on an explicit, authorised corpus change:
#   cd "$(git rev-parse --show-toplevel)" && sha256sum urantia-book/*.json > tests/corpus.sha256

set -u
cd "$(git rev-parse --show-toplevel)"

fail=0

echo "🛡️  URANTiOS guards"
echo

echo "1️⃣  Canonical corpus integrity"
if [ ! -f tests/corpus.sha256 ]; then
    echo "   ❌ Manifest tests/corpus.sha256 is missing."
    fail=1
elif sha256sum --check --quiet tests/corpus.sha256; then
    count=$(wc -l < tests/corpus.sha256)
    echo "   ✅ All $count canonical files match the manifest."
else
    echo "   ❌ Canonical corpus differs from the manifest. urantia-book/ is READ-ONLY."
    fail=1
fi

echo
echo "2️⃣  JSON validity"
json_bad=0
while IFS= read -r f; do
    if ! python3 -m json.tool "$f" > /dev/null 2>&1; then
        echo "   ❌ Invalid JSON: $f"
        json_bad=1
    fi
done < <(git ls-files '*.json')
if [ "$json_bad" -eq 0 ]; then
    echo "   ✅ All tracked JSON files parse."
else
    fail=1
fi

echo
echo "3️⃣  Em dashes in Markdown (warning only)"
emdash_hits=$(git ls-files '*.md' | grep -v '^urantia-book/' | xargs -r grep -l -- '—' || true)
if [ -n "$emdash_hits" ]; then
    echo "   ⚠️  Em dashes found in:"
    echo "$emdash_hits" | sed 's/^/      /'
else
    echo "   ✅ No em dashes found."
fi

echo
echo "4️⃣  American spellings in Markdown (warning only)"
spelling_hits=$(git ls-files '*.md' | grep -v '^urantia-book/' \
    | xargs -r grep -l -w -E 'color|colors|behavior|behaviors|initialize|initializes|initialized|organize|organizes|organized|analyze|analyzes|analyzed|favor|favors' || true)
if [ -n "$spelling_hits" ]; then
    echo "   ⚠️  American spellings found in:"
    echo "$spelling_hits" | sed 's/^/      /'
else
    echo "   ✅ No flagged American spellings found."
fi

echo
if [ "$fail" -eq 0 ]; then
    echo "✅ Guards passed."
else
    echo "❌ Guards FAILED (fatal checks above)."
fi
exit "$fail"
