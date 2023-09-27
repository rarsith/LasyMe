from pathlib import Path


def to_user_home_dir(parent_directory=None):
    if not parent_directory:
        return Path.home()
    return Path.home() / parent_directory


def create_file_in_home_dir(file_name):
    user_file_path = to_user_home_dir() / file_name
    if user_file_path.exists():
        return


def convert_path_to_universal(path_to_convert):
    universal_path = Path(path_to_convert)
    return universal_path


def create_implicit_structure(root_path):
    lasyme_container = "lasyme_data"
    lasy_databases_folder = "lasy_databases"
    lasy_configuration_folder = "lasy_config"
    lasy_default_configuration_folder = "config_defaults"
    lasy_default_configuration_file = "lasy_default_config_data.json"



if __name__ == "__main__":
    home_usr = to_user_home_dir("lasy_me_databases")
    print(home_usr)
    path_to_conv = r'C:\Users\Username\Documents\file.txt'
    convert_path_to_universal(path_to_conv)
