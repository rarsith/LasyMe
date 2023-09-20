from pathlib import Path


def to_user_home_dir():
    return Path.home()


def create_file_in_home_dir(file_name):
    user_file_path = to_user_home_dir() / file_name
    if user_file_path.exists():
        return


def convert_path_to_universal(path_to_convert):
    universal_path = Path(path_to_convert)
    return universal_path


if __name__ == "__main__":
    path_to_conv = r'C:\Users\Username\Documents\file.txt'
    convert_path_to_universal(path_to_conv)
