import os
import shutil
import textwrap
import toml

from core import confirm_dialog, init, modify_toml, touch
from paths import SmartPath
import settings
from shared import logger


def handle_new_profile(args):
    profile_path = os.path.join(settings.PROFILE_DIR, args.name)
    os.mkdir(profile_path)

    files_dir = os.path.join(profile_path, "files")
    os.mkdir(files_dir)

    files_file = "files.toml"
    files_path = os.path.join(profile_path, files_file)
    touch(files_path)

    packages_file = "packages.toml"
    packages_path = os.path.join(profile_path, packages_file)
    touch(packages_path)

    def add_profile_to_toml(data):
        if "profiles" not in data:
            data["profiles"] = []

        data["profiles"].append({
            "name": args.name,
            "path": SmartPath.to_smartpath(profile_path)
        })

    modify_toml(settings.PROFILES_PATH, add_profile_to_toml)
    
    print(f"Built profile \"{args.name}\"")
    logger.info(f"Built profile \"{args.name}\"")


def handle_delete_profile(args):
    with open(settings.PROFILES_PATH, "r") as file:
        data = toml.load(file)

    print(data)

    confirm_dialog()

    with open(settings.PROFILES_PATH, "w") as file:
        toml.dump(data, file)

    # format_toml(settings.PROFILES_PATH)

    print(f"Deleted profile \"{args.profile}\"")
    logger.info(f"Deleted profile \"{args.profile}\"")


def handle_init(args):
    init()


def handle_clean(args):
    confirm_dialog()

    shutil.rmtree(settings.CONFIG_DIR)
    shutil.rmtree(settings.DATA_DIR)

    print("Cleaned ricemgr")
