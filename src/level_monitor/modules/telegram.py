import requests

from level_monitor.config import get_settings

settings = get_settings()


def send_telegram_message(msg: str) -> None:
    if settings.telegram_bot_api_token is None or settings.telegram_chat_id is None:
        return

    url = f"https://api.telegram.org/bot{settings.telegram_bot_api_token}/sendMessage"

    params = {
        "chat_id": settings.telegram_chat_id,
        "text": msg,
    }

    r = requests.get(
        url=url,
        params=params,
        timeout=10,
    )

    r.raise_for_status()
