# BIP-39 English Wordlists

The BIP-39 English wordlist in several formats, plus printable backup sheets from hardware and metal-plate vendors.

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


`decimal` and `index` differ only in where the numbering starts. `index` is zero-indexed, which is how wallets and the BIP-39 spec count. `decimal` is one-indexed, which is how most printed plates number their rows.

Sheets showing more than one notation are filed under the rarer one. The `binary` sheets also print a decimal index, but you would use them for the bits.

The last part of the name is the vendor, or a short description where there is no vendor. The lists below drop the shared `bip-39-` prefix.

## Formats

The `.json` and `.txt` files are generated from the [BIP-39 English wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). `bip-39-english.txt` is that file unchanged, so it can be diffed against the spec directly.

### <img src="assets/json.svg" width="18"> `.json`

- [`array.json`](json/bip-39-array.json) - the 2048 words in order
- [`tuples.json`](json/bip-39-tuples.json) - `[index, binary, word]` rows
- [`records.json`](json/bip-39-records.json) - `{index, order, binary, word}` objects

Everything except the word itself is derived from the index, so you can compute what you need rather than pick a file for it:

```js
order  = index + 1
binary = index.toString(2).padStart(11, '0')
hex    = index.toString(16).toUpperCase().padStart(3, '0')
```

### <img src="assets/txt.svg" width="18"> `.txt`

- [`english.txt`](txt/bip-39-english.txt) - the upstream BIP-39 wordlist, unchanged
- [`oneline.txt`](txt/bip-39-oneline.txt) - all 2048 words on one line, space separated
- [`decimal.txt`](txt/bip-39-decimal.txt) - number and word, starting at 1
- [`index.txt`](txt/bip-39-index.txt) - index and word, starting at 0
- [`binary.txt`](txt/bip-39-binary.txt) - index, 11-bit binary and word

The first line of each:

```
english.txt   abandon
oneline.txt   abandon ability able about above absent …
decimal.txt      1  abandon
index.txt        0  abandon
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

[`SHA256SUMS`](SHA256SUMS) holds a SHA-256 for every file here. To check they are all unchanged:

```console
$ shasum -c SHA256SUMS        # sha256sum -c SHA256SUMS on linux
pdf/decimal/bip-39-decimal-coinplate-1p.pdf: OK
...
```

That proves the files match what was published here. To check a sheet still matches the vendor's own copy, hash theirs and compare to the same line:

```console
$ curl -sL https://getcoinplate.com/wp-content/uploads/2022/05/BIP39-Wordlist-English-one-page-printable.pdf | shasum -a 256
13ecc022d8203324c8a5485b0136eb0b795fbbe7402f6aae065ca97461851416
```

A mismatch there does not necessarily mean tampering. Vendors re-export their sheets, and a new timestamp inside the PDF changes the hash while the wordlist stays the same.

[`sources.tsv`](sources.tsv) pairs every file with the URLs it can be fetched from, so that check can be scripted rather than done by hand. Some files list a fallback, where the same bytes are served from a second host or an archive copy.

The check that survives that is the wordlist itself. `bip-39-english.txt` is the upstream file unchanged, so it can be diffed against the spec directly:

```console
$ curl -sL https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt | diff - txt/bip-39-english.txt
```

## License

This is a derivative work of the original BIP-39 wordlist. See [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) for more information. The PDFs are the work of their respective vendors and are redistributed here for convenience. The format icons are from [Material Icon Theme](https://github.com/material-extensions/vscode-material-icon-theme), MIT licensed.
