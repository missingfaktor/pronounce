# pronounce

A simple command-line utility for looking up modern English pronunciations using Geoff
Lindsey’s [CUBE dictionary](http://seas3.elte.hu/cube/index.pl?s=cube&grammar=1&fullw=1).

I'm a big admirer of Geoff Lindsey’s work on updating how English pronunciation is analysed and taught. His [YouTube
channel](https://www.youtube.com/@DrGeoffLindsey) and his
book [English After RP](https://www.englishspeechservices.com/english-after-rp/) have been hugely influential in how I
understand phonetics and phonology.

The CUBE (Current British English) dictionary offers up-to-date, research-backed transcriptions for thousands of English
words. This CLI tool lets you query it right from your terminal.

If you're curious about why the CUBE dictionary uses forms like `/ij/` instead of the traditional `/iː/`, I highly
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
$ scripts/run.sh pontif                

✅ Looked up pontif in 1.5s
                CUBE Pronunciations                 
┏━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  # ┃ Word          ┃ Pronunciation               ┃
┡━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│  1 │ pontifex      │ pʰ ɔ́ n t ɪ f ɛ k s          │
├────┼───────────────┼─────────────────────────────┤
│  2 │ pontiff       │ pʰ ɔ́ n t ɪ f                │
├────┼───────────────┼─────────────────────────────┤
│  3 │ pontiffs      │ pʰ ɔ́ n t ɪ f s              │
├────┼───────────────┼─────────────────────────────┤
│  4 │ pontifical    │ pʰ ɔ n tʰ ɪ́ f ɪ k ə l       │
├────┼───────────────┼─────────────────────────────┤
│  5 │ pontificals   │ pʰ ɔ n tʰ ɪ́ f ɪ k ə l z     │
├────┼───────────────┼─────────────────────────────┤
│  6 │ pontificate   │ pʰ ɔ n tʰ ɪ́ f ɪ kʰ ɛj t     │
├────┼───────────────┼─────────────────────────────┤
│  7 │ pontificate   │ pʰ ɔ n tʰ ɪ́ f ɪ k ə t       │
├────┼───────────────┼─────────────────────────────┤
│  8 │ pontificated  │ pʰ ɔ n tʰ ɪ́ f ɪ kʰ ɛj t ɪ d │
├────┼───────────────┼─────────────────────────────┤
│  9 │ pontificates  │ pʰ ɔ n tʰ ɪ́ f ɪ kʰ ɛj t s   │
├────┼───────────────┼─────────────────────────────┤
│ 10 │ pontificates  │ pʰ ɔ n tʰ ɪ́ f ɪ k ə t s     │
├────┼───────────────┼─────────────────────────────┤
│ 11 │ pontificating │ pʰ ɔ n tʰ ɪ́ f ɪ kʰ ɛj t ɪ ŋ │
├────┼───────────────┼─────────────────────────────┤
│ 12 │ pontification │ pʰ ɔ n tʰ ɪ́ f ɪ kʰ ɛ́j ʃ ə n │
└────┴───────────────┴─────────────────────────────┘


$ scripts/run.sh --full-word going

✅ Looked up going in 1.5s
     CUBE Pronunciations     
┏━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ # ┃ Word  ┃ Pronunciation ┃
┡━━━╇━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 1 │ going │ g ə́w ɪ ŋ      │
└───┴───────┴───────────────┘


$ scripts/run.sh --full-word train

✅ Looked up train in 1.8s
             CUBE Pronunciations             
┏━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ Word        ┃ Pronunciation           ┃
┡━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ gravy train │ g ɹ ɛ́j v ɪj   tʃ ɹ ɛj n │
├───┼─────────────┼─────────────────────────┤
│ 2 │ train       │ tʃ ɹ ɛ́j n               │
└───┴─────────────┴─────────────────────────┘
```
