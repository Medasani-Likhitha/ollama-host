import sys
from loguru import logger

logger.remove()
logger.add(sys.stdout, format="{time} | <level>{level}</level> | {message}")
logger.add('app.log', rotation='10 MB', format="{time} | <level>{level}</level> | {message} | {extra[logger_context]}")

custom_logger = None


def log_message(text, *args, **kwargs):
    global custom_logger
    level = kwargs.pop("level", "info")
    if args:
        custom_logger = logger.bind(logger_context=args)
    elif kwargs:
        custom_logger = logger.bind(logger_context=kwargs)
    if level == "info":
        custom_logger.info(text, *args, **kwargs)
    elif level == "debug":
        custom_logger.debug(text, *args, **kwargs)
    elif level == "trace":
        custom_logger.trace(text, *args, **kwargs)
    elif level == "error":
        custom_logger.error(text, *args, **kwargs)
    elif level == "critical":
        custom_logger.critical(text, *args, **kwargs)
    elif level == "warning":
        custom_logger.warning(text, *args, **kwargs)
    elif level == "success":
        custom_logger.success(text, *args, **kwargs)