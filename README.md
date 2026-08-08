# BIP-39 wordlists

BIP-39 wordlists in several formats, plus printable backup sheets from hardware and metal-plate vendors.

## Naming

Files are named `bip-39-<format>-<source>.<ext>`:


| Format     | Numbering                  | Range                       |
| ---------- | -------------------------- | --------------------------- |
| `plain`    | none, words only           | —                           |
| `decimal`  | decimal, starts at 1       | `1`-`2048`                  |
| `index`    | decimal, starts at 0       | `0`-`2047`                  |
| `hex`      | hexadecimal, starts at 0   | `000`-`7FF`                 |
| `binary`   | 11-bit binary, starts at 0 | `00000000000`-`11111111111` |
| `diceware` | dice rolls or bit patterns | —                           |


`decimal` and `index` differ only in the start value. `index` starts at 0 (BIP-39 / wallets). `decimal` starts at 1 (most plates).

Sheets with more than one notation use the rarer one, for example binary over decimal.

The last part of the name is the vendor, or a short label if there is none. Plain lists live under `txt/lang/` and use the language name from the [BIP-39 wordlists](https://github.com/bitcoin/bips/tree/master/bip-0039). The lists below drop the `bip-39-` prefix.

## Formats

### <img src="assets/json.svg" width="18"> `.json`

From `lang/english.txt`:

- [`array.json`](json/bip-39-array.json) - the 2048 words in order
- [`tuples.json`](json/bip-39-tuples.json) - `[index, binary, word]` rows
- [`records.json`](json/bip-39-records.json) - `{index, order, binary, word}` objects

Only the word is stored; the rest follows from the index:

```js
order  = index + 1
binary = index.toString(2).padStart(11, '0')
hex    = index.toString(16).toUpperCase().padStart(3, '0')
```

### <img src="assets/txt.svg" width="18"> `.txt`

#### Upstream

From the BIP, under `txt/lang/`. One word per line, 2048 lines:

- [`chinese_simplified.txt`](txt/lang/bip-39-chinese_simplified.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/chinese_simplified.txt)
- [`chinese_traditional.txt`](txt/lang/bip-39-chinese_traditional.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/chinese_traditional.txt)
- [`czech.txt`](txt/lang/bip-39-czech.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/czech.txt)
- [`english.txt`](txt/lang/bip-39-english.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt)
- [`french.txt`](txt/lang/bip-39-french.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/french.txt)
- [`italian.txt`](txt/lang/bip-39-italian.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/italian.txt)
- [`japanese.txt`](txt/lang/bip-39-japanese.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/japanese.txt)
- [`korean.txt`](txt/lang/bip-39-korean.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/korean.txt)
- [`portuguese.txt`](txt/lang/bip-39-portuguese.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/portuguese.txt)
- [`spanish.txt`](txt/lang/bip-39-spanish.txt) - [source](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/spanish.txt)

#### Derived

From `lang/english.txt`:

- [`oneline.txt`](txt/bip-39-oneline.txt) - all 2048 words on one line, space separated
- [`decimal.txt`](txt/bip-39-decimal.txt) - number and word, starting at 1
- [`index.txt`](txt/bip-39-index.txt) - index and word, starting at 0
- [`hex.txt`](txt/bip-39-hex.txt) - hex and word, starting at 000
- [`binary.txt`](txt/bip-39-binary.txt) - index, 11-bit binary and word

```
english.txt   abandon
oneline.txt   abandon ability able about above absent …
decimal.txt      1  abandon
index.txt        0  abandon
hex.txt        000  abandon
binary.txt       0  00000000000  abandon
```

### <img src="assets/pdf.svg" width="18"> `.pdf`

#### Decimal (1 to 2048)

- [`decimal-bitplates.pdf`](pdf/decimal/bip-39-decimal-bitplates.pdf) - 1 page, A4 - [source](https://www.bitplates.com/uploads/b/e5142000-c8c3-11ea-8d36-7f18722a8965/1753b200-c132-11ed-8ccc-bf9df506f69a.pdf)
- [`decimal-coinplate-1p.pdf`](pdf/decimal/bip-39-decimal-coinplate-1p.pdf) - 1 page, A4, vertical - [source](https://getcoinplate.com/wp-content/uploads/2022/05/BIP39-Wordlist-English-one-page-printable.pdf)
- [`decimal-coinplate-2p.pdf`](pdf/decimal/bip-39-decimal-coinplate-2p.pdf) - 2 pages, A4, horizontal - [source](https://getcoinplate.com/wp-content/uploads/2022/10/BIP39-Wordlist-2-page-printout-PDF.pdf)
- [`decimal-cold-code.pdf`](pdf/decimal/bip-39-decimal-cold-code.pdf) - 2 pages, US Letter - [source](https://www.coldcodecrypto.com/s/Cold-Code-Wordlist.pdf)
- [`decimal-coldcard.pdf`](pdf/decimal/bip-39-decimal-coldcard.pdf) - 4 pages, US Letter - [source](https://raw.githubusercontent.com/Coldcard/wordlist-paper/master/wordlist-decimal.pdf)
- [`decimal-coldti.pdf`](pdf/decimal/bip-39-decimal-coldti.pdf) - 7 pages, US Letter - [source](https://coldti.com/coldti-bip39.pdf)
- [`decimal-kryptodots.pdf`](pdf/decimal/bip-39-decimal-kryptodots.pdf) - 2 pages, A4 - [source](https://kryptodots.com/wp-content/downloads/bip-0039-English-wordlist-2pag-v2.6.pdf)
- [`decimal-lwallet.pdf`](pdf/decimal/bip-39-decimal-lwallet.pdf) - 1 page, A4 - [source](https://lwallet.com.ua/wp-content/uploads/2022/05/BIP39_Wordlist.pdf)
- [`decimal-tinyseed.pdf`](pdf/decimal/bip-39-decimal-tinyseed.pdf) - 6 pages, A4 - [source](https://raw.githubusercontent.com/tinyseed-backup/word-lists/main/BIP39_Tinyseed_io.pdf)

#### Index (0 to 2047)

- [`index-coldbit.pdf`](pdf/index/bip-39-index-coldbit.pdf) - 1 page, A4 - [source](https://coldbit.com/wp-content/uploads/2019/05/bip-39-wordlist.pdf)

#### Hexadecimal (000 to 7FF)

- [`hex-coldcard.pdf`](pdf/hex/bip-39-hex-coldcard.pdf) - 4 pages, US Letter - [source](https://raw.githubusercontent.com/Coldcard/wordlist-paper/master/wordlist.pdf)

#### Binary (11 bits, 0 to 2047)

- [`binary-massmux.pdf`](pdf/binary/bip-39-binary-massmux.pdf) - 9 pages, A4 - [source](https://www.massmux.com/wp-content/uploads/2023/04/BIP39-Binary.pdf)
- [`binary-lookup-table.pdf`](pdf/binary/bip-39-binary-lookup-table.pdf) - 4 pages, US Letter

#### Diceware

- [`diceware-bitbox.pdf`](pdf/diceware/bip-39-diceware-bitbox.pdf) - 4 pages, A4 - [source](https://bitbox.swiss/bitbox02/BitBox_Diceware_LookupTable.pdf)
  - five dice rolls and a coin flip
- [`diceware-binary.pdf`](pdf/diceware/bip-39-diceware-binary.pdf) - 3 pages, US Letter - [source](https://www.rudefox.io/custody/walkthrough/create-seed/lookup-tables.pdf)
  - eleven bits from coins or dice, plus a worksheet page for recording rolls

#### Plain (no numbering)

- [`plain-blockplate.pdf`](pdf/plain/bip-39-plain-blockplate.pdf) - 1 page, US Letter - [source](https://cdn.shopify.com/s/files/1/2362/8267/files/bip_39_wordlist_revb.pdf)
- [`plain-btcguide.pdf`](pdf/plain/bip-39-plain-btcguide.pdf) - 2 pages, A4 - [source](https://btcguide.github.io/assets/guide/bip39_wordlist.pdf)

## Verifying

[`SHA256SUMS`](SHA256SUMS) has a SHA-256 for every file under `pdf/`, `txt/` and `json/`. README, scripts and icons are omitted. To check the files:

```console
$ shasum -c SHA256SUMS        # sha256sum -c SHA256SUMS on linux
pdf/decimal/bip-39-decimal-coinplate-1p.pdf: OK
...
```

To compare a vendor file to the copy here, hash theirs and match the line in `SHA256SUMS`:

```console
$ curl -sL https://bitbox.swiss/bitbox02/BitBox_Diceware_LookupTable.pdf | shasum -a 256
9db3c8986b20737a3b76207a0fb325fec17fb3221aac32d2df470c2615e37535

$ grep diceware-bitbox SHA256SUMS
9db3c8986b20737a3b76207a0fb325fec17fb3221aac32d2df470c2615e37535  pdf/diceware/bip-39-diceware-bitbox.pdf
```

A different hash is not always tampering. Vendors often re-export PDFs; a new timestamp changes the hash even when the words are the same.

[`sources.tsv`](sources.tsv) lists each file and its download URL.

Upstream plain lists match the BIP byte for byte:

```console
$ curl -sL https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt | diff - txt/lang/bip-39-english.txt
```

## License

This is a derivative work of the original BIP-39 wordlist. See [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) for more information. The PDFs are the work of their respective vendors and are redistributed here for convenience. The format icons are from [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme), MIT licensed.
