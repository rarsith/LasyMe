import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCalendarWidget, QLabel, QLineEdit, QPushButton, QFormLayout, QTextEdit, QGridLayout
from PySide2.QtCore import Qt

class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar App")

        self.calendar = QCalendarWidget(self)
        self.calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendar.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.show_selected_date)

        self.date_label = QLabel(self)
        self.event_description = QTextEdit(self)
        self.add_event_button = QPushButton("Add Event", self)
        self.add_event_button.clicked.connect(self.add_event)

        self.events_by_date = {}  # Dictionary to store events by date

        layout = QGridLayout()
        layout.addWidget(self.calendar, 0, 0, 2, 1)
        layout.addWidget(self.date_label, 0, 1)
        layout.addWidget(self.event_description, 1, 1)
        layout.addWidget(self.add_event_button, 2, 0, 1, 2)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_selected_date(self):
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(f"Selected Date: {selected_date.toString('yyyy-MM-dd')}")

        if selected_date in self.events_by_date:
            events = "\n".join(self.events_by_date[selected_date])
            self.event_description.setPlainText(events)
        else:
            self.event_description.clear()

    def add_event(self):
        selected_date = self.calendar.selectedDate()
        event_date = selected_date.toString('yyyy-MM-dd')
        event_description = self.event_description.toPlainText()

        if selected_date not in self.events_by_date:
            self.events_by_date[selected_date] = []

        self.events_by_date[selected_date].append(event_description)
        self.event_description.clear()

        self.show_selected_date()  # Update the displayed events

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarApp()
    window.show()
    sys.exit(app.exec_())
