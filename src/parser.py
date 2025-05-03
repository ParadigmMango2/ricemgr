import argparse
import commands


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

# new file parser
add_file_parser = file_subparser.add_parser("new", help="Add a file to the current profile")
add_file_parser.add_argument("file", help="File")
# parser_profile_new.set_defaults(func=handle_add_file)

# list file parser
list_file_parser = file_subparser.add_parser("list", help="List files in current profile")
# parser_profile_new.set_defaults(func=handle_list_file)

# sync file parser
sync_file_parser = file_subparser.add_parser("sync", help="Sync a file")
sync_file_parser.add_argument("file", help="File")
# parser_profile_new.set_defaults(func=handle_sync_file)

# remove file parser
remove_file_parser = file_subparser.add_parser("remove", help="Remove a file from the current profile")
remove_file_parser.add_argument("file", help="File")
# parser_profile_new.set_defaults(func=handle_remove_file)



# --- Package Parser ----
package_parser = command_subparser.add_parser("package", help="Manage rice packages")
package_subparser = package_parser.add_subparsers(
    title="package commands",
    # dest="package_cmd",
    required=True
)

# add package parser
add_package_parser = package_subparser.add_parser("add", help="Add a package requirement to the current profile")
add_package_parser.add_argument("package", help="Package")
add_package_parser.add_argument("-v", "--version", help="Package version")
# parser_profile_new.set_defaults(func=handle_add_package)

# list package parser
list_package_parser = package_subparser.add_parser("list", help="List required packages in current profile")
# parser_profile_new.set_defaults(func=handle_list_package)

# sync package parser
sync_package_parser = package_subparser.add_parser("sync", help="Sync a package with system")
sync_package_parser.add_argument("package", help="Package")
# parser_profile_new.set_defaults(func=handle_sync_package)

# edit package parser
edit_package_parser = package_subparser.add_parser("edit", help="Edit package list of current profile")
# parser_profile_new.set_defaults(func=handle_edit_package)

# remove package parser
remove_package_parser = package_subparser.add_parser("remove", help="Remove a package requirement from the current profile")
remove_package_parser.add_argument("package", help="Package")
# parser_profile_new.set_defaults(func=handle_remove_package)



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
# parser_profile_new.set_defaults(func=handle_new_profile)

# new profile parser
list_profile_parser = profile_subparser.add_parser("list", help="List rice profiles")
# parser_profile_new.set_defaults(func=handle_list_profile)

# sync profile parser
sync_profile_parser = profile_subparser.add_parser("sync", help="Sync current rice profile")
# parser_profile_new.set_defaults(func=handle_sync_profile)

# edit profile parser
edit_profile_parser = profile_subparser.add_parser("edit", help="Edit current rice profile")
edit_profile_parser.add_argument("config", help="Config file")
# parser_profile_new.set_defaults(func=handle_edit_profile)

# delete profile parser
delete_profile_parser = profile_subparser.add_parser("delete", help="Delete a rice profile")
delete_profile_parser.add_argument("profile", help="Profile")
# parser_profile_new.set_defaults(func=handle_delete_profile)

# switch profile parser
switch_profile_parser = profile_subparser.add_parser("switch", help="Switch rice profile")
switch_profile_parser.add_argument("profile", help="Profile")
# parser_profile_new.set_defaults(func=handle_switch_profile)

# export profile parser
export_profile_parser = profile_subparser.add_parser("export", help="Export current rice profile")
export_profile_parser.add_argument("file", help="Rice profile file")
# parser_profile_new.set_defaults(func=handle_export_profile)

# import profile parser
import_profile_parser = profile_subparser.add_parser("import", help="Import a rice profile")
import_profile_parser.add_argument("file", help="Rice profile file")
# parser_profile_new.set_defaults(func=handle_import_profile)



# ===== init parser =====
init_parser = command_subparser.add_parser("init", help="Manually initialize ricemgr")
init_parser.set_defaults(func=commands.handle_init)



# ===== clean parser =====
clean_parser = command_subparser.add_parser("clean", help="Clean all ricemgr files")
clean_parser.set_defaults(func=commands.handle_clean)
