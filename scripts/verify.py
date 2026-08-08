#!/usr/bin/env python3
"""Check every generated file against wordlists/txt/lang/bip-39-english.txt.

Upstream plain lists are checked for shape and against pinned bitcoin/bips
hashes. English is the source of truth for the derived txt and json files, so
those can be regenerated and compared rather than taken on trust. Checksums
prove a file has not changed; this proves it was right to begin with.

Whitespace is deliberately not asserted. Lines are split on runs of spaces and
the values compared, because column padding is a rendering choice and is
already pinned byte for byte by SHA256SUMS.
"""

import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
failures = []

UPSTREAM_LANGS = [
    "chinese_simplified",
    "chinese_traditional",
    "czech",
    "english",
    "french",
    "italian",
    "japanese",
    "korean",
    "portuguese",
    "spanish",
]

# sha-256 of each wordlist as published in bitcoin/bips. Every other file here
# is derived from these, so without pinning them a corrupted list would still
# pass every check below, consistently and silently.
CANONICAL = {
    "chinese_simplified": "5c5942792bd8340cb8b27cd592f1015edf56a8c5b26276ee18a482428e7c5726",
    "chinese_traditional": "417b26b3d8500a4ae3d59717d7011952db6fc2fb84b807f3f94ac734e89c1b5f",
    "czech": "7e80e161c3e93d9554c2efb78d4e3cebf8fc727e9c52e03b83b94406bdcc95fc",
    "english": "2f5eed53a4727b4bf8880d8f3f199efc90e58503646d9ff8eff3a2ed3b24dbda",
    "french": "ebc3959ab7801a1df6bac4fa7d970652f1df76b683cd2f4003c941c63d517e59",
    "italian": "d392c49fdb700a24cd1fceb237c1f65dcc128f6b34a8aacb58b59384b5c648c2",
    "japanese": "2eed0aef492291e061633d7ad8117f1a2b03eb80a29d0e4e3117ac2528d05ffd",
    "korean": "9e95f86c167de88f450f0aaf89e87f6624a57f973c67b516e338e8e8b8897f60",
    "portuguese": "2685e9c194c82ae67e10ba59d9ea5345a23dc093e92276fc5361f6667d79cd3f",
    "spanish": "46846a5a0139d1e3cb77293e521c2865f7bcdb82c44e8d0a06a2cd0ecba48c0b",
}


passed = 0


def check(name, condition, detail=""):
    global passed
    if condition:
        passed += 1
    else:
        print(f"  FAIL  {name}{': ' + detail if detail else ''}")
        failures.append(name)


def group(title):
    """Print the tally for the previous group, then start a new one."""
    global _title, _mark
    if _title is not None:
        print(f"  {_title:<24} {passed - _mark} ok")
    _title, _mark = title, passed


_title = None
_mark = 0


def read(path):
    return (ROOT / path).read_text().splitlines()


def lang_path(lang):
    return f"wordlists/txt/lang/bip-39-{lang}.txt"


group("upstream wordlists")
for lang in UPSTREAM_LANGS:
    digest = hashlib.sha256((ROOT / lang_path(lang)).read_bytes()).hexdigest()
    check(f"{lang}.txt matches bitcoin/bips", digest == CANONICAL[lang], digest)
words = read(lang_path("english"))

group("english properties")
check("alphabetical", words == sorted(words))
check("first four letters unique", len({w[:4] for w in words}) == len(words))
check("every word is 3 to 8 letters", all(3 <= len(w) <= 8 and w.isalpha() for w in words))

group("file shape")
for name in ["decimal", "index", "hex", "binary", "oneline"] + UPSTREAM_LANGS:
    path = lang_path(name) if name in UPSTREAM_LANGS else f"wordlists/txt/bip-39-{name}.txt"
    raw = (ROOT / path).read_text()
    label = pathlib.Path(path).name
    check(f"{label} ends with exactly one newline",
          raw.endswith("\n") and not raw.endswith("\n\n"))
    check(f"{label} has no trailing whitespace",
          not any(ln != ln.rstrip() for ln in raw.splitlines()))
    if name != "oneline":
        check(f"{label} has 2048 lines", len(raw.splitlines()) == 2048,
              f"found {len(raw.splitlines())}")

group("derived txt")
one = (ROOT / "wordlists/txt/bip-39-oneline.txt").read_text().split()
check("oneline.txt has the same words in order", one == words)

rows = [ln.split() for ln in read("wordlists/txt/bip-39-decimal.txt")]
check("decimal.txt numbers from 1", [r[0] for r in rows] == [str(i + 1) for i in range(2048)])
check("decimal.txt words match", [r[1] for r in rows] == words)

rows = [ln.split() for ln in read("wordlists/txt/bip-39-index.txt")]
check("index.txt numbers from 0", [r[0] for r in rows] == [str(i) for i in range(2048)])
check("index.txt words match", [r[1] for r in rows] == words)

rows = [ln.split() for ln in read("wordlists/txt/bip-39-hex.txt")]
check("hex.txt values from 000 to 7FF", [r[0] for r in rows] == [f"{i:03X}" for i in range(2048)])
check("hex.txt words match", [r[1] for r in rows] == words)

rows = [ln.split() for ln in read("wordlists/txt/bip-39-binary.txt")]
check("binary.txt numbers from 0", [r[0] for r in rows] == [str(i) for i in range(2048)])
check("binary.txt bits are the 11 bit index", [r[1] for r in rows] == [format(i, "011b") for i in range(2048)])
check("binary.txt words match", [r[2] for r in rows] == words)

group("json")
data = json.loads((ROOT / "wordlists/json/bip-39-array.json").read_text())
check("array.json is the words in order", data == words)

data = json.loads((ROOT / "wordlists/json/bip-39-tuples.json").read_text())
check("tuples.json is [index, binary, word]",
      data == [[i, format(i, "011b"), w] for i, w in enumerate(words)])

data = json.loads((ROOT / "wordlists/json/bip-39-records.json").read_text())
check("records.json fields are consistent",
      data == [{"index": i, "order": i + 1, "binary": format(i, "011b"), "word": w}
               for i, w in enumerate(words)])

group(None)
print()
if failures:
    print(f"{len(failures)} check(s) failed")
    sys.exit(1)
print("all checks passed")
