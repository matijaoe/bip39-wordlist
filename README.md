# BIP-39 wordlists

[![integrity](https://github.com/matijaoe/bip39-wordlist/actions/workflows/integrity.yml/badge.svg)](https://github.com/matijaoe/bip39-wordlist/actions/workflows/integrity.yml)

BIP-39 wordlists in several formats, plus printable backup sheets from hardware and metal-plate vendors.

[pdf](#pdf) · [decimal](#decimal-1-to-2048) · [index](#index-0-to-2047) · [hex](#hexadecimal-000-to-7ff) · [binary](#binary-11-bits-0-to-2047) · [diceware](#diceware) · [plain](#plain-no-numbering)

[txt](#txt) · [json](#json)

## Naming

Files are named `bip-39-<format>-<source>.<ext>`:


| Format     | Numbering                  | Range                       |
| ---------- | -------------------------- | --------------------------- |
| `plain`    | none, words only           | —                           |
| `decimal`  | decimal, starts at 1       | `1`-`2048`                  |
| `index`    | decimal, starts at 0       | `0`-`2047`                  |
| `hex`      | hexadecimal, starts at 0   | `000`-`7FF`                 |
| `binary`   | 11-bit binary, starts at 0 | `00000000000`-`11111111111` |
| `diceware` | rolls or draws as printed  | —                           |


`decimal` and `index` differ only in the start value. `index` starts at 0 (BIP-39 / wallets). `decimal` starts at 1 (most plates).

`binary` is eleven bits as the lookup key. Coin flips, a d6 read as odd/even, or cards mapped to bits still use a binary list. `diceware` is when the sheet's keys are the physical results (`11111 h`, d8 faces, a card).

Sheets with more than one notation use the rarer one, for example binary over decimal, or a card map over binary.

The last part of the name is the vendor, or a short label if there is none. Plain lists live under `wordlists/txt/lang/` and use the language name from the [BIP-39 wordlists](https://github.com/bitcoin/bips/tree/master/bip-0039). The lists below drop the `bip-39-` prefix.

## Formats

###  `.txt`

#### Upstream

From the BIP, under `wordlists/txt/lang/`. One word per line, 2048 lines:

- [`chinese_simplified.txt`](wordlists/txt/lang/bip-39-chinese_simplified.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/chinese_simplified.txt)
- [`chinese_traditional.txt`](wordlists/txt/lang/bip-39-chinese_traditional.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/chinese_traditional.txt)
- [`czech.txt`](wordlists/txt/lang/bip-39-czech.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/czech.txt)
- [`english.txt`](wordlists/txt/lang/bip-39-english.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt)
- [`french.txt`](wordlists/txt/lang/bip-39-french.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/french.txt)
- [`italian.txt`](wordlists/txt/lang/bip-39-italian.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/italian.txt)
- [`japanese.txt`](wordlists/txt/lang/bip-39-japanese.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/japanese.txt)
- [`korean.txt`](wordlists/txt/lang/bip-39-korean.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/korean.txt)
- [`portuguese.txt`](wordlists/txt/lang/bip-39-portuguese.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/portuguese.txt)
- [`spanish.txt`](wordlists/txt/lang/bip-39-spanish.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/spanish.txt)

#### Derived

From `lang/english.txt`:

- [`oneline.txt`](wordlists/txt/bip-39-oneline.txt) - all 2048 words on one line, space separated
- [`decimal.txt`](wordlists/txt/bip-39-decimal.txt) - number and word, starting at 1
- [`index.txt`](wordlists/txt/bip-39-index.txt) - index and word, starting at 0
- [`hex.txt`](wordlists/txt/bip-39-hex.txt) - hex and word, starting at 000
- [`binary.txt`](wordlists/txt/bip-39-binary.txt) - 11-bit binary and word
- [`diceware-d4.txt`](wordlists/txt/bip-39-diceware-d4.txt) - five rolls of a d4 and a coin flip
- [`index-binary.txt`](wordlists/txt/bip-39-index-binary.txt) - index, 11-bit binary and word

```
english.txt       abandon
oneline.txt       abandon ability able about above absent …
decimal.txt          1  abandon
index.txt            0  abandon
hex.txt            000  abandon
binary.txt        00000000000  abandon
index-binary.txt     0  00000000000  abandon
diceware-d4.txt   11111 h  abandon
```

###  `.json`

From `lang/english.txt`:

- [`array.json`](wordlists/json/bip-39-array.json) - the 2048 words in order
- [`tuples.json`](wordlists/json/bip-39-tuples.json) - `[index, binary, word]` rows
- [`records.json`](wordlists/json/bip-39-records.json) - `{index, order, binary, word}` objects

Only the word is stored; the rest follows from the index:

```js
order  = index + 1
binary = index.toString(2).padStart(11, '0')
hex    = index.toString(16).toUpperCase().padStart(3, '0')
```

###  `.pdf`

#### Decimal (1 to 2048)

- [`decimal-bitplates.pdf`](wordlists/pdf/decimal/bip-39-decimal-bitplates.pdf) - 1 page, A4 - [source](https://www.bitplates.com/uploads/b/e5142000-c8c3-11ea-8d36-7f18722a8965/1753b200-c132-11ed-8ccc-bf9df506f69a.pdf)
- [`decimal-coinplate-1p.pdf`](wordlists/pdf/decimal/bip-39-decimal-coinplate-1p.pdf) - 1 page, A4, vertical - [source](https://getcoinplate.com/wp-content/uploads/2022/05/BIP39-Wordlist-English-one-page-printable.pdf)
- [`decimal-coinplate-2p.pdf`](wordlists/pdf/decimal/bip-39-decimal-coinplate-2p.pdf) - 2 pages, A4, horizontal - [source](https://getcoinplate.com/wp-content/uploads/2022/10/BIP39-Wordlist-2-page-printout-PDF.pdf)
- [`decimal-cold-code.pdf`](wordlists/pdf/decimal/bip-39-decimal-cold-code.pdf) - 2 pages, US Letter - [source](https://www.coldcodecrypto.com/s/Cold-Code-Wordlist.pdf)
- [`decimal-coldcard.pdf`](wordlists/pdf/decimal/bip-39-decimal-coldcard.pdf) - 4 pages, US Letter - [source](https://raw.githubusercontent.com/Coldcard/wordlist-paper/master/wordlist-decimal.pdf)
- [`decimal-coldti.pdf`](wordlists/pdf/decimal/bip-39-decimal-coldti.pdf) - 7 pages, US Letter - [source](https://coldti.com/coldti-bip39.pdf)
- [`decimal-kryptodots.pdf`](wordlists/pdf/decimal/bip-39-decimal-kryptodots.pdf) - 2 pages, A4 - [source](https://kryptodots.com/wp-content/downloads/bip-0039-English-wordlist-2pag-v2.6.pdf)
- [`decimal-lwallet.pdf`](wordlists/pdf/decimal/bip-39-decimal-lwallet.pdf) - 1 page, A4 - [source](https://lwallet.com.ua/wp-content/uploads/2022/05/BIP39_Wordlist.pdf)
- [`decimal-tinyseed.pdf`](wordlists/pdf/decimal/bip-39-decimal-tinyseed.pdf) - 6 pages, A4 - [source](https://raw.githubusercontent.com/tinyseed-backup/word-lists/main/BIP39_Tinyseed_io.pdf)

#### Index (0 to 2047)

- [`index-coldbit.pdf`](wordlists/pdf/index/bip-39-index-coldbit.pdf) - 1 page, A4 - [source](https://coldbit.com/wp-content/uploads/2019/05/bip-39-wordlist.pdf)

#### Hexadecimal (000 to 7FF)

- [`hex-coldcard.pdf`](wordlists/pdf/hex/bip-39-hex-coldcard.pdf) - 4 pages, US Letter - [source](https://raw.githubusercontent.com/Coldcard/wordlist-paper/master/wordlist.pdf)
- [`hex-moonsettler.pdf`](wordlists/pdf/hex/bip-39-hex-moonsettler.pdf) - 1 page, A4 - [source](https://raw.githubusercontent.com/moonsettler/guides/main/bip39-cheatsheet.pdf)
- [`hex-dictionary.pdf`](wordlists/pdf/hex/bip-39-hex-dictionary.pdf) - 3 pages, US Letter, horizontal
  - numbered `100` to `8FF`, not `000` to `7FF`: the leading digit is the block of 256, so subtract `100` for the index
  - printed from a spreadsheet, which turned `true` into `TRUE` at `84A` and `false` into `FALSE` at `392`

#### Binary (11 bits, 0 to 2047)

- [`binary-massmux.pdf`](wordlists/pdf/binary/bip-39-binary-massmux.pdf) - 9 pages, A4 - [source](https://www.massmux.com/wp-content/uploads/2023/04/BIP39-Binary.pdf)
- [`binary-lookup-table.pdf`](wordlists/pdf/binary/bip-39-binary-lookup-table.pdf) - 4 pages, US Letter
- [`binary-blockstream.pdf`](wordlists/pdf/binary/bip-39-binary-blockstream.pdf) - 51 pages, A4 - [print source](https://help.blockstream.com/generate-recovery-phrase-offline-binary-table)
  - these methods first convert their results to 11 bits:
    - [Coin](https://help.blockstream.com/generate-recovery-phrase-offline-coin) - one coin; 11 flips per word
    - [D6](https://help.blockstream.com/generate-recovery-phrase-offline-d6) - one d6; roll until you collect 11 bits per word
    - [D8](https://help.blockstream.com/generate-recovery-phrase-offline-d8) - one d8; four rolls per word; keep the first 11 bits
    - [Poker](https://help.blockstream.com/generate-recovery-phrase-offline-poker) - one 52-card deck without Jokers; use the card map; return each card and shuffle after each draw; printable guide under Diceware
    - [Piacentine](https://help.blockstream.com/generate-recovery-phrase-offline-piacentine) - one 40-card regional deck; use the card map; return each card and shuffle after each draw
    - [Tarot](https://help.blockstream.com/generate-recovery-phrase-offline-tarot) - one 78-card deck; use the card map; return each card and shuffle after each draw

#### Diceware

- [`diceware-d8-rudefox.pdf`](wordlists/pdf/diceware/bip-39-diceware-d8-rudefox.pdf) - 3 pages, US Letter - [source](https://www.rudefox.io/custody/walkthrough/create-seed/lookup-tables.pdf)
  - eleven d8 rolls for each group of three provisional words; includes a 24-word worksheet
- [`diceware-d6-veeb.pdf`](wordlists/pdf/diceware/bip-39-diceware-d6-veeb.pdf) - 4 pages, A4 - [source](https://raw.githubusercontent.com/veebch/Bip39-Dice/master/BIP39DiceManualCalculator.pdf)
  - eleven fair d6 rolls per provisional word; read odd as 0 and even as 1, then look up the bits
- [`diceware-d6-bitbox.pdf`](wordlists/pdf/diceware/bip-39-diceware-d6-bitbox.pdf) - 4 pages, A4 - [source](https://bitbox.swiss/bitbox02/BitBox_Diceware_LookupTable.pdf)
  - one d6 and an optional coin; record five results from 1 to 4; reroll 5 or 6; then flip the coin or roll once more
  - BitBox also publishes [step-by-step instructions](https://bitbox.swiss/bitbox02/BitBox_Diceware_HowTo.pdf)
- [`diceware-d6-bitcoinkeys.pdf`](wordlists/pdf/diceware/bip-39-diceware-d6-bitcoinkeys.pdf) - 4 pages, US Letter - [source](https://bitcoinkeys.guide/bip39-word-table.pdf)
  - one d6 and one coin; keep five results from 1 to 4; reroll 5 or 6; then flip the coin once per provisional word
  - [`diceware-d6-12w-bitcoinkeys.pdf`](wordlists/pdf/diceware/bip-39-diceware-d6-12w-bitcoinkeys.pdf) - adds instructions and a worksheet for a 12-word phrase, 6 pages, US Letter - [source](https://bitcoinkeys.guide/roll-12-word-seed.pdf)
  - [`diceware-d6-24w-bitcoinkeys.pdf`](wordlists/pdf/diceware/bip-39-diceware-d6-24w-bitcoinkeys.pdf) - adds instructions and a worksheet for a 24-word phrase, 6 pages, US Letter - [source](https://bitcoinkeys.guide/roll-24-word-seed.pdf)
- [`diceware-d6-taelfrinn.pdf`](wordlists/pdf/diceware/bip-39-diceware-d6-taelfrinn.pdf) - 3 pages, US Letter - [source](https://raw.githubusercontent.com/taelfrinn/Bip39-diceware/master/coin_plus_d6_bip39.pdf)
  - four d6 and one coin; roll all four dice and flip the coin once per provisional word; reroll excluded results
- [`diceware-poker-blockstream.pdf`](wordlists/pdf/diceware/bip-39-diceware-poker-blockstream.pdf) - 53 pages, A4 - [guide and print source](https://help.blockstream.com/generate-recovery-phrase-offline-poker)
  - one 52-card deck without Jokers; return each card and shuffle after each draw; includes a card map and the binary table
- [`diceware-d16-blockstream.pdf`](wordlists/pdf/diceware/bip-39-diceware-d16-blockstream.pdf) - 51 pages, A4 - [guide and print source](https://help.blockstream.com/generate-recovery-phrase-offline-d8-d16-d16)
  - one d8 and two d16 dice; roll each die once per word
- [`diceware-d8-coin-blockstream.pdf`](wordlists/pdf/diceware/bip-39-diceware-d8-coin-blockstream.pdf) - 51 pages, A4 - [guide and print source](https://help.blockstream.com/generate-recovery-phrase-offline-d8-d8-d8-coin-coin)
  - three d8 dice and two coins; roll each die once and flip each coin once per word
- [`diceware-d16-blockstream-legacy.pdf`](wordlists/pdf/diceware/bip-39-diceware-d16-blockstream-legacy.pdf) - 17 pages, US Letter - [source](https://storage.googleapis.com/dxp-production-assets/content/blockstream-jade/add-more-security-functionality/create-a-recovery-phrase-using-dice/JadeDiceRollsGuide.pdf) - legacy Jade guide
  - two d16 and one d8; roll all three dice once for each of the first 11 or 23 words

#### Plain (no numbering)

- [`plain-blockplate.pdf`](wordlists/pdf/plain/bip-39-plain-blockplate.pdf) - 1 page, US Letter - [source](https://cdn.shopify.com/s/files/1/2362/8267/files/bip_39_wordlist_revb.pdf)
- [`plain-btcguide.pdf`](wordlists/pdf/plain/bip-39-plain-btcguide.pdf) - 2 pages, A4 - [source](https://btcguide.github.io/assets/guide/bip39_wordlist.pdf)

## Verifying

[`SHA256SUMS`](SHA256SUMS) has a SHA-256 for every file under `wordlists/`:

```console
$ shasum -c SHA256SUMS        # sha256sum -c SHA256SUMS on linux
wordlists/pdf/decimal/bip-39-decimal-coinplate-1p.pdf: OK
...
```

To compare a vendor file to the copy here, hash theirs and match the line in `SHA256SUMS`:

```console
$ curl -sL https://bitbox.swiss/bitbox02/BitBox_Diceware_LookupTable.pdf | shasum -a 256
9db3c8986b20737a3b76207a0fb325fec17fb3221aac32d2df470c2615e37535

$ grep d6-bitbox SHA256SUMS
9db3c8986b20737a3b76207a0fb325fec17fb3221aac32d2df470c2615e37535  wordlists/pdf/diceware/bip-39-diceware-d6-bitbox.pdf
```

A different hash is not always tampering. Vendors often re-export PDFs; a new timestamp changes the hash even when the words are the same.

[`sources.tsv`](sources.tsv) lists each file and its direct download URL.

Upstream plain lists match the BIP byte for byte:

```console
$ curl -sL https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt | diff - wordlists/txt/lang/bip-39-english.txt
```

## Checks

Verifying above is for a file you downloaded. These two scripts check the repo itself. They need Python 3 and a shell, with nothing to install.

`scripts/verify.py` checks the wordlists are correct. Every list is compared against its pinned hash from the BIP, and every derived file is rebuilt from English and compared:

```bash
python3 scripts/verify.py
```

```
  upstream wordlists       10 ok
  english properties       3 ok
  file shape               44 ok
  derived txt              10 ok
  json                     3 ok

all checks passed
```

`scripts/check.sh` checks the bookkeeping agrees:

```bash
./scripts/check.sh
```

```
  hashes match SHA256SUMS                        ok
  SHA256SUMS covers every file                   ok
  README sources are in sources.tsv              ok
  sources.tsv paths exist                        ok
  README links are not inside code spans         ok
  README links resolve                           ok

all checks passed
```

GitHub Actions runs these exact two commands on every push and pull request, so the badge above means what a clean local run means. Together they guarantee that every wordlist matches the BIP byte for byte, that every derived file follows from English, that nothing is missing from `SHA256SUMS`, and that no link in this README is broken.

A separate weekly job re-fetches every URL in `sources.tsv` and reports when a vendor changes their file. It does not fail the build, because a vendor re-exporting a PDF is not a fault here.

## Adding a wordlist

Two kinds of file live here and they need different things.

**A sheet published by someone else.** Name it `bip-39-<format>-<vendor>.<ext>` and put it in the folder for its numbering. The format is what the sheet prints, not what the vendor sells: `decimal` starts at 1, `index` starts at 0, and a sheet showing more than one notation uses the rarer one. Use a short label when there is no vendor.

Download their copy and compare it before recording the URL:

```console
$ curl -sL <url> | shasum -a 256
```

Add the row to `sources.tsv` only if that matches. A source link that does not verify is worse than no link.

If the publisher supplies only a print button, save the print view and link the page from the README. Do not add the page to `sources.tsv`, because it does not return the stored PDF bytes.

**A file built here** from `lang/english.txt`. It gets no `sources.tsv` row, because nobody published it. It needs a case in `scripts/verify.py` describing how to rebuild it, and a line in the sample block above if it is a `.txt`.

Either way, finish with:

```bash
./scripts/checksums.sh
./scripts/check.sh
python3 scripts/verify.py
```

`check.sh` fails if the file is missing from `SHA256SUMS` or from the lists above, so a half-finished addition cannot pass quietly. What it cannot see is whether a built file is correct, only that it is listed. That is what the `verify.py` case is for.

## License

This is a derivative work of the original BIP-39 wordlist. See [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) for more information. The PDFs are the work of their respective vendors and are redistributed here for convenience. The format icons are from [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme), MIT licensed.
