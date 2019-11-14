import logging
from typing import Callable
from functools import partial

DEBUG = partial(int, 10)
INFO = partial(int, 20)
WARNING = partial(int, 30)
ERROR = partial(int, 40)
CRITICAL = partial(int, 50)

def log_it(level: Callable, msg: str) -> None:
    logger = logging.getLogger('pybites_logger')
    logger.log(level(), msg)


if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(INFO, "This is an info message.")
    log_it(WARNING, "This is a warning message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
