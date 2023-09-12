import os
import getpass
from tinydb import TinyDB

class Session():
    def __init__(self):
        self.curr_user = getpass.getuser()
        self.db_root_path = "../database"
        self.db_name = f'{self.curr_user}_TODO_tasks_db.json'
        self.db_full = os.path.join(self.db_root_path, self.db_name)
        self.db = TinyDB(self.db_full)



if __name__ == "__main__":
    Session()







