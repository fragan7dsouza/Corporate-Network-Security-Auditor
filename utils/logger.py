
import logging
import os
from datetime import datetime

logger = logging.getLogger('cnsa_logger')
logger.propagate = False

def configure_logging(level=logging.INFO):
    """Sets up the centralized logging file and console handlers."""
    if logger.handlers:
        return

    LOG_DIR = "logs"
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    LOG_FILE = os.path.join(LOG_DIR, f"cnsa_log_{datetime.now().strftime('%Y%m%d')}.log")

    logger.setLevel(level) 
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler() 
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    logger.info("Centralized logging system configured.")

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)