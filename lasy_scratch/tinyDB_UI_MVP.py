import sys
import getpass
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLineEdit, QListWidget, QTextBrowser
from tinydb import TinyDB, Query

# Create or open the TinyDB lasy_databases
db = TinyDB('task_database.json')
task_table = db.table('tasks')


class TaskModel:
    def __init__(self, title, text, created_by):
        self.title = title
        self.text = text
        self.created_by = created_by


class TaskView(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Task creation widget
        self.create_layout = QHBoxLayout()
        self.title_edit = QLineEdit()
        self.text_edit = QLineEdit()
        self.create_button = QPushButton("Create")
        self.create_layout.addWidget(self.title_edit)
        self.create_layout.addWidget(self.text_edit)
        self.create_layout.addWidget(self.create_button)
        self.layout.addLayout(self.create_layout)

        # Task list widget
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Task text viewer widget
        self.text_viewer = QTextBrowser()
        self.layout.addWidget(self.text_viewer)

        # Delete button
        self.delete_button = QPushButton("Delete")
        self.layout.addWidget(self.delete_button)


class TaskPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.create_button.clicked.connect(self.create_task)
        self.view.task_list.itemSelectionChanged.connect(self.load_task_text)
        self.view.delete_button.clicked.connect(self.delete_task)

        self.load_tasks()

    def create_task(self):
        title = self.view.title_edit.text()
        text = self.view.text_edit.text()
        created_by = getpass.getuser()

        if title and text:
            self.model = TaskModel(title, text, created_by)
            self.save_task()
            self.load_tasks()
            self.view.title_edit.clear()
            self.view.text_edit.clear()

    def save_task(self):
        task_table.insert({
            'title': self.model.title,
            'text': self.model.text,
            'created_by': self.model.created_by
        })

    def load_tasks(self):
        self.view.task_list.clear()
        tasks = task_table.all()
        for task in tasks:
            title = task['title']
            self.view.task_list.addItem(title)

    def load_task_text(self):
        selected_item = self.view.task_list.currentItem()
        if selected_item:
            selected_title = selected_item.text()
            task = task_table.search(Query().title == selected_title)
            if task:
                text = task[0]['text']
                self.view.text_viewer.setPlainText(text)

    def delete_task(self):
        selected_item = self.view.task_list.currentItem()
        if selected_item:
            selected_title = selected_item.text()
            task_table.remove(Query().title == selected_title)
            self.load_tasks()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Viewer")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = TaskView()
        self.setCentralWidget(self.central_widget)

        self.presenter = TaskPresenter(None, self.central_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
