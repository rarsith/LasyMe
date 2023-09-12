import os
import getpass
from tinydb import TinyDB

_curr_user = getpass.getuser()
db_root_path = "../database"

db_name = f'{_curr_user}_TODO_tasks_db.json'
db_full = os.path.join(db_root_path, db_name)
Session = TinyDB(db_full)


# class Session:
#     def __init__(self):
#         self.db_name = f'{_curr_user}_TODO_tasks_db.json'
#         self.db_full = os.path.join(db_root_path, self.db_name)
#         TinyDB(self.db_full)
