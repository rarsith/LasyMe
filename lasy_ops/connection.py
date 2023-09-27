import os
import getpass
from lasy_common_utils import files_utils
from lasy_common_utils import path_utils
from pathlib import Path


# current_file_path = os.path.abspath(__file__)
# LasyMeRoot = os.path.dirname(os.path.split(current_file_path)[0])
#
# lasy_databases_folder = "lasy_databases"
# lasy_configuration_folder = "lasy_config"
# lasy_configuration_file = "lasy_config_data.json"
#
# config_file_path = os.path.join(LasyMeRoot, lasy_configuration_folder, lasy_configuration_file)
# config_file = files_utils.open_json(config_file_path)
#
# root_path = LasyMeRoot
# universal_path = patils.convert_path_to_universal(root_path)
#
# Envars().os_root = str(universal_path)
# path_init = Path(lasy_databases_folder)
#
# _LASY_ME_ROOT = universal_path
# _CURRENT_USER = getpass.getuser()
# _DB_ROOT_PATH = os.path.join(Envars().os_root, lasy_databases_folder)


# TASKS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_tasks_db.json'
# USERS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_users_db.json'
# TAGS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_tags_db.json'
# CONFIG_FILE_NAME = "lasy_config_data.json"


# TasksDbPath = os.path.join(_DB_ROOT_PATH, TASKS_DATABASE_NAME)
# UsersDbPath = os.path.join(_DB_ROOT_PATH, USERS_DATABASE_NAME)
# TagsDbPath = os.path.join(_DB_ROOT_PATH, TAGS_DATABASE_NAME)
# ConfigPath = os.path.join(Envars().os_root, lasy_configuration_folder)
# ConfigFilePath = os.path.join(ConfigPath, CONFIG_FILE_NAME)


class LasyConnections:
    def __init__(self):
        self.first_time_run = "first_run.spec"
        self.lasy_me_container = "lasy_me_data"
        self.lasy_databases_folder = "lasy_databases"
        self.lasy_configuration_folder = "lasy_config"
        self.lasy_default_configuration_folder = "config_defaults"
        self.lasy_configuration_file = "lasy_config_data.json"
        self.lasy_default_configuration_file = "lasy_default_config_data.json"

        self.current_file_path = os.path.abspath(__file__)
        self.lasy_root_path = os.path.dirname(os.path.split(self.current_file_path)[0])
        self.current_user = getpass.getuser()
        # self.user_set_path = self.get_user_set_db_path()

        self.lasy_data_envar = os.environ.get("LASY_DATA_ROOT")

    def get_config_file_content(self):
        custom_exists = os.path.exists(self.config_file_full_path())
        if custom_exists:
            config_file = files_utils.open_json(self.config_file_full_path())

            return config_file
        else:
            config_file = files_utils.open_json(self.default_config_full_path())

            return config_file

    def tasks_db_name(self):
        TASKS_DATABASE_NAME = f'{self.current_user}_TODO_tasks_db.json'
        return TASKS_DATABASE_NAME

    def users_db_name(self):
        USERS_DATABASE_NAME = f'{self.current_user}_TODO_users_db.json'
        return USERS_DATABASE_NAME

    def tags_db_name(self):
        TAGS_DATABASE_NAME = f'{self.current_user}_TODO_tags_db.json'
        return TAGS_DATABASE_NAME

    def tasks_db_full_path(self):
        tasks_db_name = self.tasks_db_name()
        tasks_db_path = os.path.join(self.lasy_data_envar, self.lasy_me_container, self.lasy_databases_folder, tasks_db_name)
        return tasks_db_path

    def users_db_full_path(self):
        users_db_name = self.users_db_name()
        users_db_path = os.path.join(self.lasy_data_envar, self.lasy_me_container, self.lasy_databases_folder, users_db_name)
        return users_db_path

    def tags_db_full_path(self):
        tags_db_name = self.tags_db_name()
        tags_db_path = os.path.join(self.lasy_data_envar, self.lasy_me_container, self.lasy_databases_folder, tags_db_name)
        return tags_db_path

    def default_config_full_path(self):
        config_file_full = os.path.join(self.lasy_data_envar,
                                        self.lasy_me_container,
                                        self.lasy_configuration_folder,
                                        self.lasy_default_configuration_folder,
                                        self.lasy_default_configuration_file)
        print(config_file_full)
        return config_file_full

    def default_config_path(self):
        config_file_full = os.path.join(self.lasy_data_envar,
                                        self.lasy_me_container,
                                        self.lasy_configuration_folder,
                                        self.lasy_default_configuration_folder
                                        )
        return config_file_full

    def config_file_full_path(self):
        config_file_full = os.path.join(self.lasy_data_envar,
                                        self.lasy_me_container,
                                        self.lasy_configuration_folder,
                                        self.lasy_configuration_file)
        return config_file_full

    def config_dir_path(self):
        config_file_path = os.path.join(self.lasy_data_envar,
                                        self.lasy_me_container,
                                        self.lasy_configuration_folder
                                        )
        return config_file_path

    def create_implicit_structure(self, root_path):
        create_lasy_databases = Path(root_path) / self.lasy_me_container / self.lasy_databases_folder
        create_lasy_configs = Path(root_path) / self.lasy_me_container / self.lasy_configuration_folder
        create_lasy_default_configs = Path(root_path) / self.lasy_me_container / self.lasy_configuration_folder / self.lasy_default_configuration_folder
        create_lasy_databases.mkdir(parents=True, exist_ok=True)
        create_lasy_configs.mkdir(parents=True, exist_ok=True)
        create_lasy_default_configs.mkdir(parents=True, exist_ok=True)

    def first_run_test(self, create=False):
        if not create:
            first_run_file_path = Path(self.lasy_root_path) / self.first_time_run
            return first_run_file_path.is_file()
        files_utils.create_file(self.lasy_root_path, self.first_time_run)




if __name__ == "__main__":
    dd = LasyConnections()
    # config_file = dd.get_user_set_db_path()
    # dd.create_implicit_structure(config_file)
    # print(config_file)
