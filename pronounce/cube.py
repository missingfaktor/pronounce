import re
import unicodedata
from typing import Literal

import requests
from bs4 import BeautifulSoup

CUBE_URL = "http://seas3.elte.hu/cube/index.pl"

UNICODE_SPACES = [
    "\u0020",  # SPACE
    "\u00A0",  # NO-BREAK SPACE
    "\u1680",  # OGHAM SPACE MARK
    "\u2000",  # EN QUAD
    "\u2001",  # EM QUAD
    "\u2002",  # EN SPACE
    "\u2003",  # EM SPACE
    "\u2004",  # THREE-PER-EM SPACE
    "\u2005",  # FOUR-PER-EM SPACE
    "\u2006",  # SIX-PER-EM SPACE
    "\u2007",  # FIGURE SPACE
    "\u2008",  # PUNCTUATION SPACE
    "\u2009",  # THIN SPACE
    "\u200A",  # HAIR SPACE
    "\u202F",  # NARROW NO-BREAK SPACE ← used in CUBE
    "\u205F",  # MEDIUM MATHEMATICAL SPACE
    "\u3000",  # IDEOGRAPHIC SPACE
]

SPACE_REGEX = "[" + "".join(re.escape(ch) for ch in UNICODE_SPACES) + r"\s" + "]"

UNICODE_NORMALIZATION_FORM: Literal["NFD"] = "NFD"


def normalize_ipa(text: str) -> str:
    no_spaces = re.sub(SPACE_REGEX, "", text)
    decomposed = unicodedata.normalize(UNICODE_NORMALIZATION_FORM, no_spaces)
    return "".join(decomposed)


def fetch_cube_pronunciations(word: str, full_word: bool) -> list[tuple[str, str]]:
    params = {
        "s": word,  # The word to search
        "invr": "on",  # Use /ɹ/ instead of /r/
        "asp": "on",  # Be explicit about lenition after /s/
        "thop": "on",  # Show aspiration
        "trick": "on",  # Palatalise 'tr', 'dr' etc
    }

    if full_word:
        params["fullw"] = "on"

    response = requests.get(CUBE_URL, params=params)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    rows = soup.select("div.matchbox table.res tr")

    for row in rows:
        match row.find_all("td"):
            case [_, word_cell, ipa_cell, *_]:
                for span in word_cell.find_all("span", class_="play"):
                    span.extract()
                word_text = word_cell.get_text(strip=True)
                ipa_span = ipa_cell.find("span", class_="ipa")
                if ipa_span:
                    raw_ipa = ipa_span.get_text()
                    cleaned_ipa = normalize_ipa(raw_ipa)
                    results.append((word_text, cleaned_ipa))
            case _:
                continue

    return results
