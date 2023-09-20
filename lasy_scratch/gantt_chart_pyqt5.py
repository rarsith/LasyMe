import sys
from PySide2.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import Qt

class GanttChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gantt Chart Example")
        self.setGeometry(100, 100, 800, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QGraphicsView for the Gantt chart
        self.gantt_view = QGraphicsView(self)
        layout.addWidget(self.gantt_view)

        # Create a QGraphicsScene to manage the chart items
        self.scene = QGraphicsScene()
        self.gantt_view.setScene(self.scene)

        # Add Gantt chart items (tasks)
        self.add_gantt_item(0, 100, "Task 1", "10:00 AM - 11:30 AM")
        self.add_gantt_item(200, 150, "Task 2", "11:45 AM - 01:15 PM")
        self.add_gantt_item(400, 80, "Task 3", "01:30 PM - 02:30 PM")

        # Add the timeline
        self.add_timeline()

    def add_gantt_item(self, x, width, label, time_interval):
        item = QGraphicsRectItem(x, 50, width, 30)
        item.setBrush(Qt.blue)
        item.setFlag(item.ItemIsMovable)
        self.scene.addItem(item)

        task_item = self.scene.addText(label)
        task_item.setPos(x + 5, 55)

        time_item = self.scene.addText(time_interval)
        time_item.setPos(x + 5, 75)

    def add_timeline(self):
        for hour in range(8, 18):
            x = 50 + (hour - 8) * 50
            hour_item = self.scene.addText(f"{hour}:00")
            hour_item.setPos(x - 10, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GanttChart()
    window.show()
    sys.exit(app.exec_())
