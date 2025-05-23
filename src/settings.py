import os
import xdg_base_dirs


RICEMGR_DIR = "ricemgr"
HOME_DIR = os.path.expanduser("~")
CONFIG_DIR = os.path.join(xdg_base_dirs.xdg_config_home(), RICEMGR_DIR)
DATA_DIR = os.path.join(xdg_base_dirs.xdg_data_home(), RICEMGR_DIR)
PROFILE_DIR = os.path.join(DATA_DIR, "profiles")

HOME_KEY = "$HOME_DIR"
CONFIG_KEY = "$CONFIG_DIR"
DATA_KEY = "$DATA_DIR"

LOG_FILE = "ricemgr.log"
LOG_PATH = os.path.join(DATA_DIR, LOG_FILE)
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

FILES_FILE = "files.toml"
FILES_PATH = os.path.join(CONFIG_DIR, FILES_FILE)
PACKAGES_FILE = "packages.toml"
PACKAGES_PATH = os.path.join(CONFIG_DIR, PACKAGES_FILE)
PROFILES_FILE = "profiles.toml"
PROFILES_PATH = os.path.join(CONFIG_DIR, PROFILES_FILE)
ENVIRONMENT_FILE = "environment.toml"
ENVIRONMENT_PATH = os.path.join(CONFIG_DIR, ENVIRONMENT_FILE)
