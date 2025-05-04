import os
import textwrap

from core import confirm_dialog, init, touch
import settings
from shared import logger
import shutil


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

    with open(settings.PROFILES_PATH, "a") as file:
        file.write(textwrap.dedent(f"""\
            
            
            [[profiles]]
            name = \"{args.name}\"
            path = \"{profile_path}\"
        """)) 
    # Try not to rely on the profile path here so we can keep the files
    # user-agnostic
    
    logger.info(f"Built profile \"{args.name}\"")


def handle_init(args):
    init()


def handle_clean(args):
    confirm_dialog()

    shutil.rmtree(settings.CONFIG_DIR)
    shutil.rmtree(settings.DATA_DIR)

    print("Cleaned ricemgr")
