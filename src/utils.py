import logging
from typing import Any, Union

def custom_logger(logger_name: str, log_level: Union[str, int] = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def load_file_from_s3(bucket: str, key: str) -> str:
    raise NotImplementedError

