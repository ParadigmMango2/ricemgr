import logging
import os
import xdg_base_dirs


RICEMGR_DIR = "ricemgr"
CONFIG_DIR = os.path.join(xdg_base_dirs.xdg_config_home(), RICEMGR_DIR)
DATA_DIR = os.path.join(xdg_base_dirs.xdg_data_home(), RICEMGR_DIR)
LOG_FILE = "ricemgr.log"

logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def ensure_config_dir():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
        logger.info("Built config directory")


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        logger.info("Built data directory")


if __name__ == "__main__":
    ensure_config_dir()
    ensure_data_dir()

    print(RICEMGR_DIR)
    print("Hello World")

