# fabric_logger/app.py

import logging
import os

def setup_logger(
    log_file='app.log',
    log_level=logging.INFO,
    log_format='%(asctime)s %(levelname)s %(message)s'
):
    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format=log_format
    )

    # Also log to stdout
    console = logging.StreamHandler()
    console.setLevel(log_level)
    console.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(console)

    logging.info("Logger initialized with level: %s", logging.getLevelName(log_level))

def get_logger(name):
    return logging.getLogger(name)
