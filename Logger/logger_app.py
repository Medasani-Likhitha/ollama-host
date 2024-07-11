import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="{time} | <level>{level}</level> | {message}")
logger.add('app.log', rotation='10 MB', format="{time} | <level>{level}</level> | {message} | {extra[logger_context]}")

custom_logger = None


def log_message(text, *args, **kwargs):
    global custom_logger
    if args:
        custom_logger = logger.bind(logger_context=args)
    elif kwargs:
        custom_logger = logger.bind(logger_context=kwargs)

    custom_logger.info(text, *args, **kwargs)