import os
import textwrap
import tomllib

import settings
from shared import logger


def touch(file_path):
    open(file_path, 'a').close()


def init_profiles_conf():
    with open(settings.PROFILES_PATH, 'w') as file:
        file.write(textwrap.dedent("""\
            title = "profiles"
        """))


def ensure_config_dir():
    if not os.path.exists(settings.CONFIG_DIR):
        os.makedirs(settings.CONFIG_DIR)

        touch(settings.FILES_PATH)
        touch(settings.PACKAGES_PATH)
        touch(settings.ENVIRONMENT_PATH)

        init_profiles_conf()

        logger.info("Built config directory")


def ensure_data_dir():
    if not os.path.exists(settings.DATA_DIR) \
            or not os.path.exists(settings.PROFILE_DIR):
        os.makedirs(settings.DATA_DIR, exist_ok=True)
        os.makedirs(settings.PROFILE_DIR)

        logger.info("Built data directory")


def confirm_dialog():
    response = input("Are you sure you want to do this (y/N): ")

    if response not in ["Y", "y"]:
        exit(0)


def init():
    ensure_config_dir()
    ensure_data_dir()
