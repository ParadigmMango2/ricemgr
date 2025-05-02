import logging
import os
import xdg_base_dirs


RICEMGR_DIR_NAME = "ricemgr"
RICEMGR_DIR = os.path.join(xdg_base_dirs.xdg_config_home(), RICEMGR_DIR_NAME)
LOG_FILE = "ricemgr.log"

logging.basicConfig(filename=LOG_FILE,
                    format='%(asctime)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


if __name__ == "__main__":
    if not os.path.exists(RICEMGR_DIR):
        os.makedirs(RICEMGR_DIR)
        logger.info("Built config directory")

    print(RICEMGR_DIR)
    print("Hello World")

