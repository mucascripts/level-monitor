import logging
import time

from level_monitor.modules.models import Character
from level_monitor.modules.parsers import match_characters_raw, parse_characters
from level_monitor.modules.requests import get_guild_page
from level_monitor.modules.telegram import send_telegram_message

log = logging.getLogger(__name__)


def _get_characters(guild_name: str, page: int) -> dict[str, Character]:
    guild_page = get_guild_page(guild_name, page)

    characters_raw = match_characters_raw(guild_page)

    return parse_characters(characters_raw)


def _get_characters_data(
    character_names: set[str],
    guild_name: str,
    guild_page: int = 1,
) -> dict[str, Character]:
    all_characters = _get_characters(guild_name, guild_page)

    filtered_characters: dict[str, Character] = {}

    for name, character in all_characters.items():
        if name in character_names:
            filtered_characters[name] = character

    for character_name in character_names:
        if character_name not in filtered_characters:
            log.warning(
                f"Personagem {character_name} não encontrado na "
                f"página {guild_page} da guild {guild_name}"
            )

    return filtered_characters


def main(
    character_names: set[str],
    guild_name: str,
    guild_page: int,
    reset_table: str,
) -> None:
    last_level: dict[str, int] = {name: 0 for name in character_names}
    stuck_characters: set[str] = set()
    reset_ready_characters: set[str] = set()

    while True:
        log.info("-" * 80)
        log.info("Consultando site")

        data = _get_characters_data(character_names, guild_name, guild_page)

        for character in data.values():
            level_info = f"(Level={character.level}, Resets={character.resets})"

            if character.reset_ready(reset_table):
                if character.name not in reset_ready_characters:
                    msg = f"Personagem {character.name} pronto para resetar. {level_info}"
                    log.info(f"Enviando mensagem no telegram: `{msg}`")
                    send_telegram_message(msg)
                    reset_ready_characters.add(character.name)
            else:
                reset_ready_characters.discard(character.name)

            is_stuck = (
                character.level == last_level[character.name]
            ) and character.name not in reset_ready_characters

            if is_stuck:
                if character.name not in stuck_characters:
                    msg = (
                        f"Personagem {character.name} está a 10 minutos no mesmo level! "
                        f"{level_info}"
                    )
                    log.info(f"Enviando mensagem no telegram: `{msg}`")
                    send_telegram_message(msg)
                    stuck_characters.add(character.name)
            else:
                stuck_characters.discard(character.name)

            last_level[character.name] = character.level

            log.info(f"{character}")

        log.info(f"Personagens parados:              {stuck_characters or '{}'}")
        log.info(f"Personagens prontos para resetar: {reset_ready_characters or '{}'}")
        log.info("")

        time.sleep(600)
