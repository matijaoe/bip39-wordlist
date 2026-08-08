# BIP-39 English Wordlists

The BIP-39 English wordlist in several formats, plus printable backup sheets from hardware and metal-plate vendors.

## Naming

Files are named `bip-39-<format>-<source>.<ext>`:

| Format | Numbering | Range |
| --- | --- | --- |
| `plain` | none, words only | — |
| `decimal` | decimal, starts at 1 | `1`-`2048` |
| `index` | decimal, starts at 0 | `0`-`2047` |
| `hex` | hexadecimal, starts at 0 | `000`-`7FF` |
| `binary` | 11-bit binary, starts at 0 | `00000000000`-`11111111111` |
| `diceware` | dice rolls or bit patterns | — |

`decimal` and `index` hold the same numbers. Only the starting point differs. `index` is zero-indexed, which is how wallets and the BIP-39 spec count. `decimal` is one-indexed, which is how most printed plates number their rows.

Some sheets show more than one notation. Those are filed under the rarer one. The `binary` sheets also print a decimal index, but you would use them for the bits.

The last part of the name identifies the file within its format. It is the vendor where there is one, and a short description where there isn't.

## Formats

The `.json` and `.txt` files are generated from the [BIP-39 English wordlist](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). `bip-39-english.txt` is that file unchanged, so it can be diffed against the spec directly. The PDFs come from the vendors named below.

### `.json`

- [`bip-39-array.json`](json/bip-39-array.json) - the 2048 words in order
- [`bip-39-tuples.json`](json/bip-39-tuples.json) - `[index, binary, word]` rows
- [`bip-39-records.json`](json/bip-39-records.json) - `{index, order, binary, word}` objects

Everything except the word itself is derived from the index, so you can compute what you need rather than pick a file for it:

```js
order  = index + 1
binary = index.toString(2).padStart(11, '0')
hex    = index.toString(16).toUpperCase().padStart(3, '0')
```

### `.txt`

- [`bip-39-english.txt`](txt/bip-39-english.txt) - the upstream BIP-39 wordlist, unchanged
- [`bip-39-oneline.txt`](txt/bip-39-oneline.txt) - all 2048 words on one line, space separated
- [`bip-39-decimal.txt`](txt/bip-39-decimal.txt) - number and word, starting at 1
- [`bip-39-index.txt`](txt/bip-39-index.txt) - index and word, starting at 0
- [`bip-39-binary.txt`](txt/bip-39-binary.txt) - index, 11-bit binary and word

### `.pdf`

#### Decimal (1 to 2048)

- [Bitplates](pdf/decimal/bip-39-decimal-bitplates.pdf) - 1 page, A4
- [Coinplate](pdf/decimal/bip-39-decimal-coinplate.pdf) - 1 page, A4
- [Cold Code](pdf/decimal/bip-39-decimal-cold-code.pdf) - 2 pages, Letter
- [Coldcard](pdf/decimal/bip-39-decimal-coldcard.pdf) - 4 pages, Letter
- [Kryptodots](pdf/decimal/bip-39-decimal-kryptodots.pdf) - 2 pages, A4
- [LWallet](pdf/decimal/bip-39-decimal-lwallet.pdf) - 1 page, A4
- [Tiny Seed](pdf/decimal/bip-39-decimal-tinyseed.pdf) - 6 pages, A4

#### Index (0 to 2047)

- [Coldbit](pdf/index/bip-39-index-coldbit.pdf) - 1 page, A4

#### Hexadecimal (000 to 7FF)

- [Coldcard](pdf/hex/bip-39-hex-coldcard.pdf) - 4 pages, Letter

#### Binary (11 bits, 0 to 2047)

- [massmux](pdf/binary/bip-39-binary-massmux.pdf) - 9 pages, A4, one row per word
- [Lookup table](pdf/binary/bip-39-binary-lookup-table.pdf) - 4 pages, Letter, 64 words per column

#### Diceware

- [BitBox](pdf/diceware/bip-39-diceware-bitbox.pdf) - 4 pages, A4, five dice rolls and a coin flip
- [Binary](pdf/diceware/bip-39-diceware-binary.pdf) - 2 pages, A4, eleven bits from coins or dice

#### Plain (no numbering)

- [Blockplate](pdf/plain/bip-39-plain-blockplate.pdf) - 1 page, Letter
- [BTC Guide](pdf/plain/bip-39-plain-btcguide.pdf) - 2 pages, A4

## License

This is a derivative work of the original BIP-39 wordlist. See [BIP-39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) for more information. The PDFs are the work of their respective vendors and are redistributed here for convenience.
