import os

import settings
from shared import logger


def touch(file_path):
    open(file_path, 'a').close()


def ensure_config_dir():
    if not os.path.exists(settings.CONFIG_DIR):
        os.makedirs(settings.CONFIG_DIR)

        touch(settings.PACKAGES_PATH)
        touch(settings.PROFILES_PATH)
        touch(settings.ENVIRONMENT_PATH)

        logger.info("Built config directory")


def ensure_data_dir():
    if not os.path.exists(settings.DATA_DIR) \
            or not os.path.exists(settings.PROFILE_DIR):
        os.makedirs(settings.DATA_DIR, exist_ok=True)
        os.makedirs(settings.PROFILE_DIR)

        logger.info("Built data directory")


def init():
    ensure_config_dir()
    ensure_data_dir()
