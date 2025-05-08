import os
import textwrap
import toml

import settings
from shared import logger


# ====== FILE OPERATIONS ======
def touch(file_path):
    open(file_path, 'a').close()


def init_profiles_conf():
    data = {
        "title": "profiles"
    }

    with open(settings.PROFILES_PATH, 'w') as file:
        toml.dump(data, file)


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


def modify_toml(toml_file_path, modifier_func):
    with open(toml_file_path, "r") as file:
        data = toml.load(file)

    modifier_func(data)

    with open(toml_file_path, "w") as file:
        toml.dump(data, file)


# ====== CLI UTILS ======
def confirm_dialog():
    response = input("Are you sure you want to do this (y/N): ")

    if response not in ["Y", "y"]:
        exit(0)


# ====== MISC ======
def init():
    ensure_config_dir()
    ensure_data_dir()
