from tinydb import TinyDB
from lasy_ops.connection import LasyConnections


class TagsOps:
    def __init__(self):
        self.db = TinyDB(LasyConnections().tags_db_full_path())
        self.table = self.db.table(LasyConnections().tags_db_name())

    def insert_tag(self, document):
        test = self.table.insert(document)
        return test

    def update_tag(self, task_id, updates):
        self.table.update(updates, doc_ids=[task_id])

    def delete_tag(self, task_id):
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

    def get_tag_by_id(self, task_id):
        result = self.table.get(doc_id=task_id)

        return result


if __name__ == "__main__":
    cc = TagsOps()
    docs = cc.get_all_documents()
    print(docs)