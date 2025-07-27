# pronounce

A simple command-line utility for looking up modern English pronunciations using Geoff
Lindsey’s [CUBE dictionary](http://seas3.elte.hu/cube/index.pl?s=cube&grammar=1&fullw=1).

I'm a big admirer of Geoff Lindsey’s work on updating how English pronunciation is analysed and taught. His [YouTube
channel](https://www.youtube.com/@DrGeoffLindsey) and his
book [English After RP](https://www.englishspeechservices.com/english-after-rp/) have been hugely influential in how I
understand phonetics and phonology.

The CUBE (Current British English) dictionary offers up-to-date, research-backed transcriptions for thousands of English
words. This CLI tool lets you query it right from your terminal.

If you're curious about why the CUBE dictionary uses forms like `/ɪj/` instead of the traditional `/iː/`, I highly
recommend watching [this video](https://www.youtube.com/watch?v=gtnlGH055TA) to understand the reasoning behind it.

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and packaging. All dependencies and
script entry points are managed through `pyproject.toml`.

You can set up your development environment using the following script:

```bash
scripts/setup.sh
```

## Usage

```
> pronounce --help

Usage: python -m pronounce.main [OPTIONS] WORD

Options:
  -n, --include_non_full_word_matches
                                  Include non full word matches
  --help                          Show this message and exit.


> pronounce drawing

✅ Looked up drawing in 1.5s
      CUBE Pronunciations      
┏━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ # ┃ Word    ┃ Pronunciation ┃
┡━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 1 │ drawing │ dʒ ɹ óː ɹ ɪ ŋ │
└───┴─────────┴───────────────┘


> pronounce -n whom

✅ Looked up whom in 1.4s
         CUBE Pronunciations          
┏━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ Word       ┃ Pronunciation     ┃
┡━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ 1 │ whom       │ h ʉ́w m            │
├───┼────────────┼───────────────────┤
│ 2 │ whomever   │ h ʉw m ɛ́ v ə      │
├───┼────────────┼───────────────────┤
│ 3 │ whomsoever │ h ʉ́w m s əw ɛ́ v ə │
├───┼────────────┼───────────────────┤
│ 4 │ whomst     │ h ʉ́w m s d        │
└───┴────────────┴───────────────────┘
```
