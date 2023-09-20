import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QVBoxLayout
from PySide2.QtGui import QColor, QPalette, QPainter
from PySide2.QtCore import Qt

class GanttChart(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a central widget and a layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Create a QTableWidget
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(3)  # Set the number of rows (tasks)
        self.table_widget.setColumnCount(10)  # Set the number of columns (time units)

        # Set column labels (time units)
        time_units = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10"]
        self.table_widget.setHorizontalHeaderLabels(time_units)

        # Add some sample task data (start and end times)
        self.add_task(0, "Task 1", 1, 4)  # Task 1 starts on Day 1 and ends on Day 4
        self.add_task(1, "Task 2", 3, 7)  # Task 2 starts on Day 3 and ends on Day 7
        self.add_task(2, "Task 3", 5, 9)  # Task 3 starts on Day 5 and ends on Day 9

        # Add the QTableWidget to the layout
        layout.addWidget(self.table_widget)

        # Set the central widget
        self.setCentralWidget(central_widget)

        # Set window properties
        self.setWindowTitle("Gantt Chart Example with Draggable Lines")
        self.setGeometry(100, 100, 800, 400)

    def add_task(self, row, task_name, start_day, end_day):
        # Create a custom widget for the cell (representing the chart line)
        widget = ChartLineWidget(start_day, end_day)

        # Create a label for the task name
        label = QTableWidgetItem(task_name)

        # Set the background color of the cell
        widget.setAutoFillBackground(True)
        palette = widget.palette()
        palette.setColor(QPalette.Window, QColor(100, 100, 255))  # Blue color
        widget.setPalette(palette)

        # Add the custom widget to the cell
        self.table_widget.setCellWidget(row, start_day - 1, widget)  # Adjust for 0-based indexing
        self.table_widget.setItem(row, 0, label)  # Add the task name to the first column

class ChartLineWidget(QWidget):
    def __init__(self, start_day, end_day):
        super().__init__()

        # Store start and end days
        self.start_day = start_day
        self.end_day = end_day

        # Set background color and border for the chart line
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(100, 100, 255))  # Blue color
        self.setPalette(palette)
        self.setStyleSheet("border: 1px solid black;")

        # Enable mouse tracking to track mouse events
        self.setMouseTracking(True)

    def paintEvent(self, event):
        # Custom paint event to display the start and end day as text
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawText(self.rect(), Qt.AlignLeft, str(self.start_day))
        painter.drawText(self.rect(), Qt.AlignRight, str(self.end_day))

    def mousePressEvent(self, event):
        # Store the starting position for dragging
        self.start_pos = event.pos()

    def mouseMoveEvent(self, event):
        # Calculate the distance moved
        delta = event.pos() - self.start_pos

        # Update the start and end day based on the mouse movement
        self.start_day += delta.x()
        self.end_day += delta.x()

        # Update the starting position for the next move
        self.start_pos = event.pos()

        # Ensure the chart line does not go out of bounds
        if self.start_day < 1:
            self.start_day = 1
            self.end_day = self.start_day + (self.width() / 10) - 1  # Adjust for column width
        if self.end_day > 10:
            self.end_day = 10
            self.start_day = self.end_day - (self.width() / 10) + 1  # Adjust for column width

        # Update the widget
        self.update()

def main():
    app = QApplication(sys.argv)
    window = GanttChart()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
