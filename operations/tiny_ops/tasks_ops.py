from operations.tdb_attributes_definitions import TaskAttributesDefinitions
from operations.connection import TasksDbPath, TASKS_DATABASE_NAME
from operations.tdb_manager import TinyDBManager


class TinyOps:
    def __init__(self):
        self.db = TinyDBManager(TasksDbPath)
        self.table = self.db.get_table(TASKS_DATABASE_NAME)

    def insert_task(self, document: dict):
        test = self.table.insert(document)
        return test

    def update_task(self, task_id, updates):
        self.table.update(updates, doc_ids=[task_id])

    def delete_task(self, task_id):
        self.table.remove(doc_ids=[task_id])

    def get_all_documents(self, ids=False):
        full_docs= {}
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

    # all_docum = tops.get_all_documents(ids=True)
    # pprint.pprint(all_docum)
    #
    doc_id = 1

    # tops.delete_task(task_id=doc_id)

    result_value = tops.get_task_end_date(task_id=doc_id)
    print(result_value)



