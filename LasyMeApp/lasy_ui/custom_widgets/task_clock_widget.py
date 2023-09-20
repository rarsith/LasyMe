import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide2.QtCore import QTimer, QTime

class ClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.time_label_lb = QLabel()
        self.timer_tm = QTimer(self)
        self.timer_tm.timeout.connect(self.update_time)
        self.timer_tm.start(1000)  # Update time every 1000 milliseconds (1 second)

        self.update_time()  # Initial update

    def create_layout(self):
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.time_label_lb)

    def update_time(self):
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("hh:mm:ss")
        self.time_label_lb.setText(formatted_time)
