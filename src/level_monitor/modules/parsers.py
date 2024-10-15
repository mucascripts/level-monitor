import re

from . import models, regex


def match_characters_raw(response_text: str) -> list[tuple[str, str, str]]:
    pattern = regex.get_characters_regex()

    return re.findall(pattern, response_text)


def parse_characters(characters_raw: list[tuple[str, str, str]]) -> dict[str, models.Character]:
    characters = {
        character_raw[0]: models.Character.from_tuple(character_raw)
        for character_raw in characters_raw
    }

    return characters
