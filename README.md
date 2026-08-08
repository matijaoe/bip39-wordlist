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

### `.json`

- [`array.json`](json/bip-39-array.json) - the 2048 words in order
- [`tuples.json`](json/bip-39-tuples.json) - `[index, binary, word]` rows
- [`records.json`](json/bip-39-records.json) - `{index, order, binary, word}` objects

Everything except the word itself is derived from the index, so you can compute what you need rather than pick a file for it:

```js
order  = index + 1
binary = index.toString(2).padStart(11, '0')
hex    = index.toString(16).toUpperCase().padStart(3, '0')
```

### `.txt`

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

### `.pdf`

#### Decimal (1 to 2048)

- [`decimal-bitplates.pdf`](pdf/decimal/bip-39-decimal-bitplates.pdf) - 1 page, A4
- [`decimal-coinplate.pdf`](pdf/decimal/bip-39-decimal-coinplate.pdf) - 1 page, A4
- [`decimal-cold-code.pdf`](pdf/decimal/bip-39-decimal-cold-code.pdf) - 2 pages, Letter
- [`decimal-coldcard.pdf`](pdf/decimal/bip-39-decimal-coldcard.pdf) - 4 pages, Letter
- [`decimal-kryptodots.pdf`](pdf/decimal/bip-39-decimal-kryptodots.pdf) - 2 pages, A4
- [`decimal-lwallet.pdf`](pdf/decimal/bip-39-decimal-lwallet.pdf) - 1 page, A4
- [`decimal-tinyseed.pdf`](pdf/decimal/bip-39-decimal-tinyseed.pdf) - 6 pages, A4

#### Index (0 to 2047)

- [`index-coldbit.pdf`](pdf/index/bip-39-index-coldbit.pdf) - 1 page, A4

#### Hexadecimal (000 to 7FF)

- [`hex-coldcard.pdf`](pdf/hex/bip-39-hex-coldcard.pdf) - 4 pages, Letter

#### Binary (11 bits, 0 to 2047)

- [`binary-massmux.pdf`](pdf/binary/bip-39-binary-massmux.pdf) - 9 pages, A4, one row per word
- [`binary-lookup-table.pdf`](pdf/binary/bip-39-binary-lookup-table.pdf) - 4 pages, Letter, 64 words per column

#### Diceware

- [`diceware-bitbox.pdf`](pdf/diceware/bip-39-diceware-bitbox.pdf) - 4 pages, A4, five dice rolls and a coin flip
- [`diceware-binary.pdf`](pdf/diceware/bip-39-diceware-binary.pdf) - 2 pages, A4, eleven bits from coins or dice

#### Plain (no numbering)

- [`plain-blockplate.pdf`](pdf/plain/bip-39-plain-blockplate.pdf) - 1 page, Letter
- [`plain-btcguide.pdf`](pdf/plain/bip-39-plain-btcguide.pdf) - 2 pages, A4

## License

This is a derivative work of the original BIP-39 wordlist. See [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) for more information. The PDFs are the work of their respective vendors and are redistributed here for convenience.
