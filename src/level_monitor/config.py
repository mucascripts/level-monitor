import logging
from functools import lru_cache
from typing import Any, Literal

from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    ## - Monitoramento - ##
    chars_names: set[str]
    guild_name: str
    guild_page: int = 1
    reset_table: Literal["free", "premium"] = "free"

    # - Telegram Bot -
    telegram_bot_api_token: str
    telegram_chat_id: str

    # - Logging -
    log_level: int | str = "WARNING"
    log_dir_path: str = "logs"

    class Config:
        env_file = ".env"

        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name in ["chars_names"]:
                return {item.strip() for item in raw_val.split(",")}
            return cls.json_loads(raw_val)  # type: ignore

    @validator("log_level")
    def valid_log_level(cls, v: int | str) -> int | str:
        if isinstance(v, str):
            v = v.upper()
            if not isinstance(logging.getLevelName(v), int):
                error_msg = "O `log_level` passado é inválido"
                raise ValueError(error_msg)  # noqa: TRY004
        return v


@lru_cache(1)
def get_settings() -> Settings:
    return Settings()
