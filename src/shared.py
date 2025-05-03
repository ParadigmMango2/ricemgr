import os

import logging
import settings


os.makedirs(settings.DATA_DIR, exist_ok=True)
logging.basicConfig(filename=settings.LOG_PATH,
                    format=settings.LOG_FORMAT)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
