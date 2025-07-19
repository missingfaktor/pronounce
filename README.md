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
$ scripts/run.sh thoughtful 

✅ Looked up thoughtful in 1.8s
         CUBE Pronunciations          
┏━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ # ┃ Word           ┃ Pronunciation ┃
┡━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 1 │ thoughtful     │ θóːtfəl       │
├───┼────────────────┼───────────────┤
│ 2 │ thoughtfully   │ θóːtfəlɪj     │
├───┼────────────────┼───────────────┤
│ 3 │ thoughtfulness │ θóːtfəlnəs    │
└───┴────────────────┴───────────────┘
```

```
$scripts/run.sh going --full-word

✅ Looked up going in 1.5s
     CUBE Pronunciations     
┏━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ # ┃ Word  ┃ Pronunciation ┃
┡━━━╇━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 1 │ going │ gə́wɪŋ         │
└───┴───────┴───────────────┘
```
