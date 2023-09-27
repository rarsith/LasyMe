from tinydb import TinyDB, Query
from lasy_ops.tdb_attributes_definitions import TaskAttributesDefinitions
from lasy_ops.connection import LasyConnections
from lasy_common_utils.date_time_utils import DateTime


class TinyOps:
    def __init__(self):
        self.db = TinyDB(LasyConnections().tasks_db_full_path())
        self.table = self.db.table(LasyConnections().tasks_db_name())
        self.query = Query()

    def insert_task(self, document: dict):
        test = self.table.insert(document)
        return test

    def update_task(self, task_id, updates):
        self.table.update(updates, doc_ids=[task_id])

    def delete_task(self, task_id):
        self.table.remove(doc_ids=[task_id])

    def get_all_documents(self, ids=False):
        full_docs = {}
        all_docs = self.table.all()
        if not ids:
            return all_docs
        for doc in all_docs:
            doc_id = doc.doc_id
            full_docs[doc_id] = doc
        return full_docs

    def get_doc_by_id(self, task_id):
        result = self.table.get(doc_id=task_id)

        return result

    def get_docs_by_id(self, list_of_ids):
        retrieved_documents = {}
        for task_id in list_of_ids:
            document = self.table.get(doc_id=task_id)
            if document:
                retrieved_documents[task_id] = (document)
        return retrieved_documents

    def get_docs_by_tags(self, tag_to_search, remove=False):
        documents = self.table.search(self.query.tags.any(tag_to_search))
        if remove:
            for document in documents:
                if tag_to_search in document['tags']:
                    document['tags'].remove(tag_to_search)
                    self.update_task(document.doc_id, {'tags': document['tags']})

        return documents

    def get_docs_by_prio(self, prio_to_search):
        full_docs = {}
        documents = self.table.search(self.query.prio.any(prio_to_search))
        for document in documents:
            full_docs[document.doc_id] = document

        return full_docs

    def get_docs_by_multiple_keys(self, criteria: dict):
        full_docs = {}
        conditions = []
        if len(criteria) != 0:
            for key, value in criteria.items():
                if key == "tags":
                    condition = getattr(self.query, key).any(value)

                elif isinstance(value, list):
                    condition = getattr(self.query, key).one_of(value)

                else:
                    condition = getattr(self.query, key)==value
                conditions.append(condition)

            combined_condition = conditions[0]

            for condition in conditions[1:]:
                combined_condition = combined_condition & condition

            db = TinyDB(LasyConnections().tasks_db_full_path())
            db_table = db.table(LasyConnections().tasks_db_name())
            result = db_table.search(combined_condition)

            for document in result:
                full_docs[document.doc_id] = document

        return full_docs

    def get_tasks_by_remaining_time(self, tasks_ids: list ,reference_max):
        extracted_ids = []
        for task_id in tasks_ids:
            # get_document = self.get_doc_by_id(task_id)
            end_date = self.get_task_end_date(task_id)
            time_left_interval = DateTime().today_to_end_day(end_day=end_date)
            if time_left_interval < reference_max:
                extracted_ids.append(task_id)
        return extracted_ids

        # all_documents = self.get_all_documents(ids=True)



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

    tops = TinyOps()
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

    big_ass_doc = {"1": {"task_title": "Daily Norm module", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:47", "assigned_to": "arsithra", "start_date_interval": "2023-09-17", "end_date_interval": "2023-09-23", "hours_allocated": "90", "prio": "Critical", "status": "BLOCKED", "active": True, "task_details": ["", "Need to create the Daily module for the app to allocate portions per day"], "tags": ["LASY_ME"]}, "2": {"task_title": "Create Progress bar to illustrate the norm foe rall tasks per day", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:47", "assigned_to": "arsithra", "start_date_interval": "2023-09-17", "end_date_interval": "2023-09-23", "hours_allocated": "90", "prio": "Critical", "status": "BLOCKED", "active": True, "task_details": [], "tags": ["LASY_ME"]}, "3": {"task_title": "Create App installer", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:47", "assigned_to": "arsithra", "start_date_interval": "2023-09-17", "end_date_interval": "2023-09-30", "hours_allocated": "90", "prio": "High", "status": "BLOCKED", "active": True, "task_details": [], "tags": ["LASY_ME"]}, "4": {"task_title": "Create App COnfiguration Manager", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:47", "assigned_to": "arsithra", "start_date_interval": "2023-09-17", "end_date_interval": "2023-09-30", "hours_allocated": "90", "prio": "Low", "status": "BLOCKED", "active": True, "task_details": [], "tags": ["LASY_ME"]}, "5": {"task_title": "Create DB backup Manager", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:47", "assigned_to": "arsithra", "start_date_interval": "2023-09-17", "end_date_interval": "2023-09-30", "hours_allocated": "90", "prio": "Normal", "status": "BLOCKED", "active": True, "task_details": [], "tags": ["LASY_ME"]}, "6": {"task_title": "Send Mikkel Jobs Descri[tion to philipp", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:47", "assigned_to": "arsithra", "start_date_interval": "2023-09-15", "end_date_interval": "2023-09-19", "hours_allocated": "30", "prio": "Critical", "status": "DONE", "active": True, "task_details": [], "tags": ["department"]}, "7": {"task_title": "Get the car to the service", "parent": "root", "created_by": "arsithra", "date_created": "2023-09-17", "time_created": "18:55", "assigned_to": "arsithra", "start_date_interval": "2023-09-17", "end_date_interval": "2023-09-21", "hours_allocated": "90", "prio": "Normal", "status": "Init", "active": True, "task_details": [], "tags": ["personal"]}}

    key_to = {'tags':['LASY_ME'], 'status': ['Init'], 'prio':['Normal']}

    ids_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

    # cc = tops.get_docs_by_multiple_keys(criteria=key_to)
    cc = tops.get_all_documents(ids=True)

    # all_docum = tops.get_docs_by_tags(tag, remove=True)
    pprint.pprint(cc)
    #

    # get_all_docs = tops.get_all_documents()
    # pprint.pprint(get_all_docs)
    # doc_id = 1

    # tops.delete_task(task_id=doc_id)

    # result_value = tops.get_task_end_date(task_id=doc_id)
    # print(result_value)



