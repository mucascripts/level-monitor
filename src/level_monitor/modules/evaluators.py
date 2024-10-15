from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import Character

_RESET_TABLES = {
    "free": {
        0: 300,
        11: 325,
        21: 350,
        36: 375,
        81: 400,
    },
    "premium": {
        0: 300,
        16: 325,
        31: 350,
        51: 375,
        141: 400,
    },
}


def _get_reset_level(resets: int, table: str) -> int:
    if table not in _RESET_TABLES:
        error_msg = (
            f"Tabela de resets `{table}` inválida. Valores permitidos: {_RESET_TABLES.keys()}"
        )
        raise ValueError(error_msg)

    character_next_reset = resets + 1

    result = 0
    for reset_amount, reset_level in _RESET_TABLES[table].items():
        if character_next_reset >= reset_amount and reset_level > result:
            result = reset_level
    return result


def is_reset_ready(character: "Character", table: str) -> bool:
    return character.level >= _get_reset_level(character.resets, table)
