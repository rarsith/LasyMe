import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget
from tinydb import TinyDB, Query

class Model:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.table = self.db.table('my_table')

    def insert_document(self, document):
        self.table.insert(document)

    def update_document(self, doc_id, updates):
        self.table.update(updates, doc_ids=[doc_id])

    def delete_document(self, doc_id):
        self.table.remove(doc_ids=[doc_id])

class View(QMainWindow):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.setWindowTitle("TinyDB MVP Example")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.input_field = QLineEdit()
        layout.addWidget(self.input_field)

        self.insert_button = QPushButton("Insert")
        self.insert_button.clicked.connect(self.insert_document)
        layout.addWidget(self.insert_button)

        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_document)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_document)
        layout.addWidget(self.delete_button)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        central_widget.setLayout(layout)

    def insert_document(self):
        document_text = self.input_field.text()
        if document_text:
            document = {'text': document_text}
            self.presenter.insert_document(document)
            self.update_document_list()

    def update_document(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            doc_id = int(selected_item.text().split(':')[0])
            updates = {'text': self.input_field.text()}
            self.presenter.update_document(doc_id, updates)
            self.update_document_list()

    def delete_document(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            doc_id = int(selected_item.text().split(':')[0])
            self.presenter.delete_document(doc_id)
            self.update_document_list()

    def update_document_list(self):
        self.list_widget.clear()
        documents = self.presenter.get_documents()
        for doc in documents:
            self.list_widget.addItem(f"{doc.doc_id}: {doc['text']}")

class Presenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insert_document(self, document):
        self.model.insert_document(document)

    def update_document(self, doc_id, updates):
        self.model.update_document(doc_id, updates)

    def delete_document(self, doc_id):
        self.model.delete_document(doc_id)

    def get_documents(self):
        return self.model.table.all()

def main():
    db_path = 'my_database.json'
    model = Model(db_path)
    presenter = Presenter(model, None)

    app = QApplication(sys.argv)
    view = View(presenter)
    presenter.view = view
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
