from level_monitor import config
from level_monitor.main import main

settings = config.get_settings()


if __name__ == "__main__":
    main(
        character_names=settings.chars_names,
        guild_name=settings.guild_name,
        guild_page=settings.guild_page,
        reset_table=settings.reset_table,
    )
