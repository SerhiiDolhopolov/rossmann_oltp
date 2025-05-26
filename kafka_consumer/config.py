import os
import json
import logging
import logging.config

from dotenv import load_dotenv


load_dotenv()

KAFKA_CONSUMER_LOGGING_CONFIG = os.getenv("KAFKA_CONSUMER_LOGGING_CONFIG")
CONSUMER_ID = os.getenv("CONSUMER_ID")


def init_logging():
    with open(KAFKA_CONSUMER_LOGGING_CONFIG, "r") as f:
        config = json.load(f)
    for handler in config.get("handlers", {}).values():
        filename = handler.get("filename")
        if filename:
            filename = filename.format(CONSUMER_ID=CONSUMER_ID)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            handler["filename"] = filename
    logging.config.dictConfig(config)