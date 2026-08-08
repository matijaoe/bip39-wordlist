#!/usr/bin/env python3
"""Check every generated file against txt/bip-39-english.txt.

The wordlist is the single source of truth. Everything else here is derived
from it, so it can be regenerated and compared rather than taken on trust.
Checksums prove a file has not changed; this proves it was right to begin with.

Whitespace is deliberately not asserted. Lines are split on runs of spaces and
the values compared, because column padding is a rendering choice and is
already pinned byte for byte by SHA256SUMS.
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
failures = []


def check(name, condition, detail=""):
    if condition:
        print(f"  ok    {name}")
    else:
        print(f"  FAIL  {name}{': ' + detail if detail else ''}")
        failures.append(name)


def read(path):
    return (ROOT / path).read_text().splitlines()


words = read("txt/bip-39-english.txt")

print("the wordlist itself")
check("2048 words", len(words) == 2048, f"found {len(words)}")
check("no duplicates", len(set(words)) == len(words))
check("alphabetical", words == sorted(words))
check("first four letters unique", len({w[:4] for w in words}) == len(words))
check("every word is 3 to 8 letters", all(3 <= len(w) <= 8 and w.isalpha() for w in words))

print("txt")
one = (ROOT / "txt/bip-39-oneline.txt").read_text().split()
check("oneline.txt has the same words in order", one == words)

rows = [ln.split() for ln in read("txt/bip-39-decimal.txt")]
check("decimal.txt numbers from 1", [r[0] for r in rows] == [str(i + 1) for i in range(2048)])
check("decimal.txt words match", [r[1] for r in rows] == words)

rows = [ln.split() for ln in read("txt/bip-39-index.txt")]
check("index.txt numbers from 0", [r[0] for r in rows] == [str(i) for i in range(2048)])
check("index.txt words match", [r[1] for r in rows] == words)

rows = [ln.split() for ln in read("txt/bip-39-binary.txt")]
check("binary.txt numbers from 0", [r[0] for r in rows] == [str(i) for i in range(2048)])
check("binary.txt bits are the 11 bit index", [r[1] for r in rows] == [format(i, "011b") for i in range(2048)])
check("binary.txt words match", [r[2] for r in rows] == words)

print("json")
data = json.loads((ROOT / "json/bip-39-array.json").read_text())
check("array.json is the words in order", data == words)

data = json.loads((ROOT / "json/bip-39-tuples.json").read_text())
check("tuples.json is [index, binary, word]",
      data == [[i, format(i, "011b"), w] for i, w in enumerate(words)])

data = json.loads((ROOT / "json/bip-39-records.json").read_text())
check("records.json fields are consistent",
      data == [{"index": i, "order": i + 1, "binary": format(i, "011b"), "word": w}
               for i, w in enumerate(words)])

print()
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed")
