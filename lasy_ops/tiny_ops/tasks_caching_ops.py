from tinydb import TinyDB, Query
from lasy_ops.tdb_attributes_definitions import TaskAttributesDefinitions
from lasy_ops.connection import LasyConnections
from lasy_ops.tiny_ops.tasks_ops import TasksOps
from lasy_common_utils.date_time_utils import DateTime


class TasksCachingOps:
    def __init__(self, db_cache):

        self.db_cache = db_cache

    def get_doc_by_id(self, task_id):
        result = self.db_cache.get(task_id)
        return result

    def get_docs_by_id(self, list_of_ids):
        retrieved_documents = {}
        for tasks_id, tasks_attr_values in self.db_cache.items():
            if tasks_id in list_of_ids:
                retrieved_documents[tasks_id] = tasks_attr_values

        return retrieved_documents

    def get_docs_by_prio(self, prio_to_search):
        result = {}
        for task_id, values in self.db_cache.items():
            if prio_to_search in values["prio"]:
                result[task_id] = values

        return result

    def get_docs_by_multiple_keys(self, criteria: dict):
        filtered_documents = {}

        for ids, doc in self.db_cache.items():
            tags_match = criteria.get('tags') is None or any(tag in doc['tags'] for tag in criteria['tags'])
            status_match = any(criteria.get('status') is None or status in criteria['status'] for status in [doc['status']])
            prio_match = any(criteria.get('prio') is None or prio in criteria['prio'] for prio in [doc['prio']])

            if status_match and prio_match and tags_match:
                filtered_documents[ids]=doc

        return filtered_documents

    def get_tasks_by_remaining_time(self, tasks_ids: list, reference_max):
        extracted_ids = []
        for task_id in tasks_ids:
            # get_document = self.get_doc_by_id(task_id)
            end_date = self.get_task_end_date(task_id)
            time_left_interval = DateTime().today_to_end_day(end_day=end_date)
            if time_left_interval < reference_max:
                extracted_ids.append(task_id)
        return extracted_ids

    def get_task_parent(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().parent]

    def get_task_title(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().title]

    def get_task_created_by(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().created_by]

    def get_task_assigned_to(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().assigned_to]

    def get_task_date_created(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().date_created]

    def get_task_time_created(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().time_created]

    def get_task_start_date(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().start_date_interval]

    def get_task_end_date(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        if result:
            return result[TaskAttributesDefinitions().end_date_interval]

    def get_task_prio(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().prio]

    def get_task_status(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().status]

    def get_task_active(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().active]

    def get_task_task_details(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().task_details]

    def get_task_hours_allocated(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().hours_allocated]

    def get_task_tags(self, task_id):
        result = self.get_doc_by_id(task_id=task_id)
        return result[TaskAttributesDefinitions().tags]


if __name__ == "__main__":
    import pprint
    import os

    # os.environ["LASY_DATA_ROOT"] = 'D:\\My_Apps_Repo\\database_testing_sandbox'

    big_ass_doc ={
        "1": {
            "task_title": "TRX - DATA -> Ask Veronica about the efficiancy data",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-09-26",
            "time_created": "10:52",
            "datetime_created": "2023-09-26 10:52:09:149510",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-04",
            "hours_allocated": "30",
            "prio": "High",
            "status": "DONE",
            "active": True,
            "task_details": ["", "", "Content became Task with id: 7", "", ""],
            "tags": ["--PERSISTENT--", "TRX Management"]
        },
        "2": {
            "task_title": "TRX - Personnel -> Mikkel's Job Description",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-09-26",
            "time_created": "10:52",
            "datetime_created": "2023-09-26 10:52:35:866278",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-02",
            "hours_allocated": "30",
            "prio": "High",
            "status": "DONE",
            "active": True,
            "task_details": ["", "Folow up with Philipp H", ""],
            "tags": ["CG Department", "management meeting", "TRX Management"]
        },
        "3": {
            "task_title": "TRX - CG -> RND projects for the Downtime Period",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-09-26",
            "time_created": "10:53",
            "datetime_created": "2023-09-26 10:53:00:168745",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-06",
            "hours_allocated": "30",
            "prio": "Critical",
            "status": "InProgress",
            "active": True,
            "task_details": ["", "- Start 27thSep", "- finish next week 4thOct", ""],
            "tags": ["Strategies", "CG Department", "TRX Management", "--PERSISTENT--", "Holger Voss"]
        },
        "4": {
            "task_title": "TRX -> FaceWare Project Prep",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-09-26",
            "time_created": "10:53",
            "datetime_created": "2023-09-26 10:53:53:187726",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-06",
            "hours_allocated": "30",
            "prio": "Critical",
            "status": "InProgress",
            "active": True,
            "task_details": ["", "- Have David creating a bidding document", "- Breakdown the steps for faceware.....", "", "Content became Task with id: 16"],
            "tags": ["--PERSISTENT--", "project_", "FaceWare"]
        },
        "5": {
            "task_title": "PROJ -  ESSEX ->  concept from Max",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-09-26",
            "time_created": "10:54",
            "datetime_created": "2023-09-26 10:54:31:615174",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-02",
            "hours_allocated": "30",
            "prio": "High",
            "status": "DONE",
            "active": True,
            "task_details": ["", "Content became Task with id: 8", "Content became Task with id: 8", "Content became Task with id: 8", "Content became Task with id: 8", "", "", "Content became Task with id: 8", "Content became Task with id: 8", "Content became Task with id: 8", "", "", ""],
            "tags": ["management meeting", "Strategies", "management meeting", "Strategies", "Sales"]
        },
        "6": {
            "task_title": "new Test Task",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "16:36",
            "datetime_created": "2023-10-03 16:36:40:904312",
            "assigned_to": "",
            "start_date_interval": "2023-10-03",
            "end_date_interval": "2023-10-04",
            "hours_allocated": "",
            "prio": "Normal",
            "status": "Init",
            "active": True,
            "task_details": ["", "bla bla"],
            "tags": ["From IE", "--PERSISTENT--"]
        },
        "11": {
            "task_title": "Split --> PROJ -  ESSEX ->  concept from Max",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "18:28",
            "datetime_created": "2023-10-03 18:28:01:788384",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-02",
            "hours_allocated": "",
            "prio": "High",
            "status": "InProgress",
            "active": True,
            "task_details": ["Content became Task with id: 8", "Content became Task with id: 8", "Content became Task with id: 8"],
            "tags": ["management meeting", "Strategies", "management meeting", "Strategies", "Sales"]
        },
        "12": {
            "task_title": "New Tags",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "20:20",
            "datetime_created": "2023-10-03 20:20:42:179003",
            "assigned_to": "",
            "start_date_interval": "2023-10-03",
            "end_date_interval": "2023-10-03",
            "hours_allocated": "",
            "prio": "Critical",
            "status": "DONE",
            "active": True,
            "task_details": ["", "Check if working"],
            "tags": ["CG Department", "personal", "project_", "From IE"]
        },
        "13": {
            "task_title": "Another New Task",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "20:21",
            "datetime_created": "2023-10-03 20:21:23:965008",
            "assigned_to": "",
            "start_date_interval": "2023-10-03",
            "end_date_interval": "2023-10-04",
            "hours_allocated": "",
            "prio": "High",
            "status": "DONE",
            "active": True,
            "task_details": ["", "Tags"],
            "tags": ["CG Department", "personal", "management meeting"]
        },
        "14": {
            "task_title": "Another new Task for Tags",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "20:22",
            "datetime_created": "2023-10-03 20:22:20:963741",
            "assigned_to": "",
            "start_date_interval": "2023-10-03",
            "end_date_interval": "2023-10-03",
            "hours_allocated": "",
            "prio": "Critical",
            "status": "Init",
            "active": True,
            "task_details": [],
            "tags": ["personal", "project_", "For Cinesite", "FaceWare", "From CS", "--PERSISTENT--", "Strategies", "Pipeline", "Holger Voss", "Sales"]
        },
        "15": {
            "task_title": "dfgsdfgsdfgsdfg",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "20:23",
            "datetime_created": "2023-10-03 20:23:06:395135",
            "assigned_to": "",
            "start_date_interval": "2023-10-03",
            "end_date_interval": "2023-10-03",
            "hours_allocated": "",
            "prio": "Critical",
            "status": "Init",
            "active": True,
            "task_details": [],
            "tags": ["CG Department", "management meeting", "project_", "For Cinesite", "FaceWare", "From CS", "CS Pipeline", "--PERSISTENT--", "TRX Management"]
        },
        "16": {
            "task_title": "Split --> TRX -> FaceWare Project Prep",
            "parent": "root",
            "created_by": "arsithra",
            "date_created": "2023-10-03",
            "time_created": "20:23",
            "datetime_created": "2023-10-03 20:23:51:505066",
            "assigned_to": "",
            "start_date_interval": "2023-09-26",
            "end_date_interval": "2023-10-06",
            "hours_allocated": "",
            "prio": "Critical",
            "status": "InProgress",
            "active": True,
            "task_details": ["- Have David creating a bidding document", "- Breakdown the steps for faceware....."],
            "tags": ["--PERSISTENT--", "project_", "FaceWare"]
        }
    }




    tops = TasksCachingOps(big_ass_doc)
    # print(tops)
    # attr_def = TaskAttributesDefinitions()
    # tiny_attr = TinyAttributesPaths(attr_def)
    #
    # gen_task_schema = TaskSchema(attr_def)
    # gen_task_schema.task_details = "Here is a sample for Task Details..."
    #
    # new_task = gen_task_schema.to_dict()

    # new_id = tops.insert_task(new_task)
    # print(new_id)

    # tops.update_task(new_id, tiny_attr.assigned_to(value="hellooRA"))
    # docs_ids = [4, 6, 7, 2, 3, 8, 9, 10, 5]

    # tag = "important things"

    all_tasks_ids = list(big_ass_doc.keys())

    key_to = {'status': ['DONE'], 'prio':['High'], 'tags':['Sales']}

    # ids_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    ids_list = [1, 2]

    # cc = tops.get_docs_by_multiple_keys(criteria=key_to)
    cc = tops.get_docs_by_id(ids_list)

    # all_docum = tops.get_docs_by_tags(tag, remove=True)
    pprint.pprint(cc)
    #

    # get_all_docs = tops.get_all_documents()
    # pprint.pprint(get_all_docs)
    # doc_id = 1

    # tops.delete_task(task_id=doc_id)

    # result_value = tops.get_task_end_date(task_id=doc_id)
    # print(result_value)



