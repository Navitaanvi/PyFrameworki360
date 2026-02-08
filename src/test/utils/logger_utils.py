import logging
import os
from datetime import datetime
from time import strftime

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER,exist_ok=True)

log_file = os.path.join(
    LOG_FOLDER,f"automation_{datetime.now(),strftime('%Y%m%d_%H%M%S')}.log"
    )

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

