import os
import getpass
from pathlib import Path
from LasyMeApp.lasy_common_utils import path_utils as patils
from LasyMeApp.lasy_envars.envars import Envars

root_path = r"C:\Users\arsithra\PycharmProjects\LasyMe\LasyMeApp"
universal_path = patils.convert_path_to_universal(root_path)

# Set Root Path for the App
Envars().os_root = str(universal_path)
lasy_databases_folder = "lasy_databases"
lasy_configuration_folder = "lasy_config"
path_init = Path(lasy_databases_folder)


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
    dd = ConfigPath
    print(dd)
