import re
from typing import Literal

import requests
from bs4 import BeautifulSoup

CUBE_URL = "http://seas3.elte.hu/cube/index.pl"

UNICODE_NORMALIZATION_FORM: Literal["NFD"] = "NFD"


def touch_up_ipa_string(text: str) -> str:
    return (
        re.sub(r"[\u00A0\u1680\u2000-\u200B\u202F\u205F\u3000]", " ", text)
        .replace("ʧ", "tʃ")
        .replace("ʤ", "dʒ")
    )


def fetch_cube_pronunciations(word: str, include_non_full_word_matches: bool) -> list[tuple[str, str]]:
    params = {
        "s": word,  # The word to search
        "invr": "on",  # Use /ɹ/ instead of /r/
        "asp": "on",  # Be explicit about lenition after /s/
        "thop": "on",  # Show aspiration
        "trick": "on",  # Palatalise 'tr', 'dr' etc
        "fullw": "on",  # Include full word matches only
    }

    if include_non_full_word_matches:
        del params["fullw"]

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
                    cleaned_ipa = touch_up_ipa_string(raw_ipa)
                    results.append((word_text, cleaned_ipa))
            case _:
                continue

    return results
