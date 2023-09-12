import json
import os
import sys
from PySide2 import QtWidgets, QtCore

class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.subtasks = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

class ToDoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.TASKS_DIR = '../tasks'
        if not os.path.exists(self.TASKS_DIR):
            os.makedirs(self.TASKS_DIR)

        self.init_ui()

    def init_ui(self):
        # Input Elements
        self.task_input = QtWidgets.QLineEdit(self)
        self.priority_input = QtWidgets.QComboBox(self)
        self.priority_input.addItems(['Low', 'Medium', 'High'])
        self.due_date_input = QtWidgets.QDateEdit(self)

        # Button for Creating Task
        self.create_button = QtWidgets.QPushButton("Create Task", self)
        self.create_button.clicked.connect(self.create_task_button_clicked)

        # List Widget to Display Tasks
        self.task_list_widget = QtWidgets.QListWidget(self)

        # Layout Setup
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("Enter Task:"))
        layout.addWidget(self.task_input)
        layout.addWidget(QtWidgets.QLabel("Priority:"))
        layout.addWidget(self.priority_input)
        layout.addWidget(QtWidgets.QLabel("Due Date:"))
        layout.addWidget(self.due_date_input)
        layout.addWidget(self.create_button)
        layout.addWidget(QtWidgets.QLabel("Existing Tasks:"))
        layout.addWidget(self.task_list_widget)

        self.setLayout(layout)

    def create_task_button_clicked(self):
        task_title = self.task_input.text()
        priority = self.priority_input.currentText()
        due_date = self.due_date_input.date().toString("yyyy-MM-dd")
        description = ""  # You can add more UI elements for description if needed

        task = Task(task_title, description, priority, due_date)
        self.create_task(task)
        self.task_input.clear()
        self.update_task_list()

    def update_task_list(self):
        self.task_list_widget.clear()
        task_files = [f for f in os.listdir(self.TASKS_DIR) if f.endswith(".json")]
        for task_file in task_files:
            task_title = os.path.splitext(task_file)[0]
            self.task_list_widget.addItem(task_title)

    # Implement other functions similarly

    def main(self):
        self.setWindowTitle("To-Do Helper")
        self.setGeometry(100, 100, 800, 600)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.main()
    sys.exit(app.exec_())