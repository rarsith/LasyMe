from tinydb import TinyDB, Query


class TinyDBManager:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()

    def get_table(self, table_name):
        return self.db.table(table_name)

    def insert_record(self, table_name, record):
        table = self.get_table(table_name)
        return table.insert(record)

    def get_all_records(self, table_name):
        table = self.get_table(table_name)
        return table.all()

    def get_record_by_id(self, table_name, record_id):
        table = self.get_table(table_name)
        return table.get(doc_id=record_id)

    def update_record(self, table_name, record_id, updates):
        table = self.get_table(table_name)
        return table.update(updates, doc_ids=[record_id])

    def delete_record(self, table_name, record_id):
        table = self.get_table(table_name)
        return table.remove(doc_ids=[record_id])