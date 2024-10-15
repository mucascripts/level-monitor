import logging

import requests
import tenacity

log = logging.getLogger(__name__)


@tenacity.retry(
    wait=tenacity.wait_fixed(30),
    stop=tenacity.stop_after_attempt(3),
    retry=tenacity.retry_if_exception_type(requests.RequestException),
    after=tenacity.after_log(log, logging.INFO),
)
def get_guild_page(guild_name: str, page: int) -> str:
    response = requests.get(
        url=f"https://www.mucabrasil.com.br/?go=guild&n={guild_name}&p={page}",
        timeout=10,
    )

    response.raise_for_status()

    return response.text
