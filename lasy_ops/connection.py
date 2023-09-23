import os
import getpass
from pathlib import Path
from lasy_common_utils import path_utils as patils
from lasy_envars.envars import Envars
from lasy_common_utils import files_utils


current_file_path = os.path.abspath(__file__)
LasyMeRoot = os.path.dirname(os.path.split(current_file_path)[0])

lasy_databases_folder = "lasy_databases"
lasy_configuration_folder = "lasy_config"
lasy_configuration_file = "lasy_config_data.json"

config_file_path = os.path.join(LasyMeRoot, lasy_configuration_folder, lasy_configuration_file)
config_file = files_utils.open_json(config_file_path)

root_path = LasyMeRoot
universal_path = patils.convert_path_to_universal(root_path)

Envars().os_root = str(universal_path)
path_init = Path(lasy_databases_folder)

_LASY_ME_ROOT = universal_path
_CURRENT_USER = getpass.getuser()
_DB_ROOT_PATH = os.path.join(Envars().os_root, lasy_databases_folder)


TASKS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_tasks_db.json'
USERS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_users_db.json'
TAGS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_tags_db.json'


TasksDbPath = os.path.join(_DB_ROOT_PATH, TASKS_DATABASE_NAME)
UsersDbPath = os.path.join(_DB_ROOT_PATH, USERS_DATABASE_NAME)
TagsDbPath = os.path.join(_DB_ROOT_PATH, TAGS_DATABASE_NAME)
ConfigPath = os.path.join(Envars().os_root, lasy_configuration_folder)


if __name__ == "__main__":
    dd = LasyMeRoot
    print(dd)
