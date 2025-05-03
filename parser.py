import argparse


# ===== Main Parser =====
parser = argparse.ArgumentParser(prog="ricemgr")
command_subparser = parser.add_subparsers(
    title="commands",
    # dest="command",
    help='Available commands',
    required=True
)


# --- File Parser ----
file_parser = command_subparser.add_parser("file", help="Manage rice dotfiles and other files")
file_subparser = file_parser.add_subparsers(
    title="file commands",
    # dest="file_cmd",
    required=True
)


# --- Package Parser ----
package_parser = command_subparser.add_parser("package", help="Manage rice packages")
package_subparser = package_parser.add_subparsers(
    title="package commands",
    # dest="package_cmd",
    required=True
)


# --- Profile Parser ----
profile_parser = command_subparser.add_parser("profile", help="Manage rice profiles")
profile_subparser = profile_parser.add_subparsers(
    title="profile commands",
    # dest="profile_cmd",
    required=True
)

# new profile parser
new_profile_parser = profile_subparser.add_parser("new", help="Create a new rice profile")
new_profile_parser.add_argument("name", help="Profile name")
# parser_profile_new.set_defaults(func=handle_profile_new)

# delete profile parser
new_profile_parser = profile_subparser.add_parser("delete", help="Delete a rice profile")
new_profile_parser.add_argument("profile", help="Profile")
# parser_profile_new.set_defaults(func=handle_profile_new)

# new profile parser
list_profile_parser = profile_subparser.add_parser("list", help="List rice profiles")
# parser_profile_new.set_defaults(func=handle_profile_new)

# sync profile parser
sync_profile_parser = profile_subparser.add_parser("sync", help="Sync current rice profile")
# parser_profile_new.set_defaults(func=handle_profile_new)

# edit profile parser
edit_profile_parser = profile_subparser.add_parser("edit", help="Edit current rice profile")
edit_profile_parser.add_argument("config", help="Config file")
# parser_profile_new.set_defaults(func=handle_profile_new)

# switch profile parser
switch_profile_parser = profile_subparser.add_parser("switch", help="Switch rice profile")
switch_profile_parser.add_argument("profile", help="Profile")
# parser_profile_new.set_defaults(func=handle_profile_new)

# export profile parser
export_profile_parser = profile_subparser.add_parser("export", help="Export current rice profile")
export_profile_parser.add_argument("file", help="Rice profile file")
# parser_profile_new.set_defaults(func=handle_profile_new)

# import profile parser
import_profile_parser = profile_subparser.add_parser("import", help="Import a rice profile")
import_profile_parser.add_argument("file", help="Rice profile file")
# parser_profile_new.set_defaults(func=handle_profile_new)
