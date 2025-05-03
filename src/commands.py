from core import init
import settings
import shutil


def handle_init(args):
    init()


def handle_clean(args):
    shutil.rmtree(settings.CONFIG_DIR)
    shutil.rmtree(settings.DATA_DIR)

    print("Cleaned ricemgr")
