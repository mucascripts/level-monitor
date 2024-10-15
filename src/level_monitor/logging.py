import logging
import os

from level_monitor import config

settings = config.get_settings()

_THIRD_PARTY_LOG_NAMES: set[str] = set()

_FIRST_PARTY_LOG_NAME = __package__.partition(".")[0]


def configure_logging() -> None:
    logformat = "[%(asctime)s][%(levelno)s]: %(message)s"
    formatter = logging.Formatter(logformat)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.NOTSET)

    all_log_names = {_FIRST_PARTY_LOG_NAME}.union(_THIRD_PARTY_LOG_NAMES)

    for log_name in all_log_names:
        log = logging.getLogger(log_name)
        log.handlers = []
        log.setLevel(settings.log_level)
        log.addHandler(console_handler)

        if settings.log_dir_path:
            log_file_path = os.path.join(settings.log_dir_path, f"{log_name}.log")
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.NOTSET)
            log.addHandler(file_handler)
