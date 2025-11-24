import logging
import time

LOG_FILE= 'automation_run.log'

logging.basicConfig(level=logging.INFO)

logger= logging.getLogger('DevOpsScript')
logger.serLevel(logging.DEBUG)

file_handler = logging.FileHandler(LOG_FILENAME, mode = 'a')
file_handler.setLevel(logging.INFO)

console
