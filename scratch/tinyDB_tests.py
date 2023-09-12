from tinydb import TinyDB, Query
import getpass
import typing


curr_user = getpass.getuser()
db = TinyDB (f'{curr_user}_tasks_db.json')

root_schema = {
        'parent': None,
        'task_title': '',
        'user': getpass.getuser(),
        'asigned_to': '',
        'start_date_interval': '1-1-2000',
        'end_date_interval': '1-3-2000',
        'hours_allocated': '3',
        'prio': 'high',
        'status': 'high',
        'active': True,
        'task_details': ''
    }

def insert():
    db.insert(root_schema)


if __name__=="__main__":
    # db.purge()
    insert()