import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide2.QtCore import QTimer, QTime

class ClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.time_label = QLabel()
        layout.addWidget(self.time_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update time every 1000 milliseconds (1 second)

        self.setLayout(layout)
        self.update_time()  # Initial update

    def update_time(self):
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("hh:mm:ss")
        self.time_label.setText(formatted_time)

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    clock_widget = ClockWidget()
    window.setCentralWidget(clock_widget)
    window.setWindowTitle("Clock Widget")
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
