# tests/test.py

import os
import sys
import logging

# Add the package to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fabric_logger import setup_logger, get_logger

def test_logging():
    log_file = 'test.log'
    setup_logger(log_file=log_file)

    logger = get_logger(__name__)
    test_message = 'Test log message'
    logger.info(test_message)
    
    # Ensure the log file is created and contains the test message
    try:
        with open(log_file, 'r') as f:
            log_contents = f.read()
            assert test_message in log_contents
    except FileNotFoundError:
        assert False, f"Log file '{log_file}' was not created."
    

if __name__ == "__main__":
    test_logging()
