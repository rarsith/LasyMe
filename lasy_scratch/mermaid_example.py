import sys
from PySide2.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLineEdit,
)
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl

class GanttChartApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gantt Chart App")
        self.setGeometry(100, 100, 800, 600)

        self.tasks = []  # List to store tasks

        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.web_view = QWebEngineView()
        self.layout.addWidget(self.web_view)

        # Add task form
        self.task_name_input = QLineEdit(self)
        self.start_date_input = QLineEdit(self)
        self.end_date_input = QLineEdit(self)
        add_task_button = QPushButton("Add Task", self)
        add_task_button.clicked.connect(self.add_task)

        self.layout.addWidget(self.task_name_input)
        self.layout.addWidget(self.start_date_input)
        self.layout.addWidget(self.end_date_input)
        self.layout.addWidget(add_task_button)

        self.load_gantt_chart()

    def load_gantt_chart(self):
        # Create Mermaid Gantt chart code
        mermaid_code = "gantt\n  dateFormat YYYY-MM-DD\n  title My Gantt Chart"
        for task in self.tasks:
            mermaid_code += f"\n  section {task['name']}\n  {task['name']}: task, {task['start_date']}, {task['end_date']}"

        # Load the Mermaid Gantt chart into the web view
        html_template = """
        <html>
        <head>
          <script type="module" src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs"></script>
        </head>
        <body>
          <div class="mermaid" id="mermaid-gantt"></div>
          <script>
            mermaid.initialize({ startOnLoad: true });
            mermaid.render('mermaid-gantt', `""" + mermaid_code + """`);
          </script>
        </body>
        </html>
        """
        self.web_view.setHtml(html_template)
        self.web_view.show()

    def add_task(self):
        task_name = self.task_name_input.text()
        start_date = self.start_date_input.text()
        end_date = self.end_date_input.text()

        if task_name and start_date and end_date:
            task = {
                'name': task_name,
                'start_date': start_date,
                'end_date': end_date
            }
            self.tasks.append(task)
            self.task_name_input.clear()
            self.start_date_input.clear()
            self.end_date_input.clear()
            self.load_gantt_chart()

def main():
    app = QApplication(sys.argv)
    window = GanttChartApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
