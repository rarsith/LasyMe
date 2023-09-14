import os
import getpass
from tinydb import TinyDB

_CURRENT_USER = getpass.getuser()
_DB_ROOT_PATH = "C:\\Users\\arsithra\\PycharmProjects\\LasyMe\\databases"

TASKS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_tasks_db.json'
USERS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_users_db.json'
TAGS_DATABASE_NAME = f'{_CURRENT_USER}_TODO_tags_db.json'

TasksDbPath = os.path.join(_DB_ROOT_PATH, TASKS_DATABASE_NAME)
UsersDbPath = os.path.join(_DB_ROOT_PATH, USERS_DATABASE_NAME)
TagsDbPath = os.path.join(_DB_ROOT_PATH, TAGS_DATABASE_NAME)


if __name__ == "__main__":
    dd = TasksDbPath().path()
    print (dd)