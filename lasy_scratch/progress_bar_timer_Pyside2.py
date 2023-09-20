import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PySide2.QtCore import QTimer, QDateTime, QTime


class ProgressBarApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.update_button = QPushButton("Update Progress")
        self.update_button.clicked.connect(self.update_progress)
        self.layout.addWidget(self.update_button)


        self.start_time = QTime(16, 0, 0)
        self.end_time = QTime(16, 12, 0)  # Change this to your desired end time (e.g., 23:59:59)

        self.update_progress()

        # Create a QTimer to update the progress every hour (3600000 milliseconds)
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_progress)
        # self.timer.start(1000)  # Update every hour

    def update_progress(self):
        self.current_time = QDateTime.currentDateTime().time()
        time_left = self.current_time.secsTo(self.end_time)
        total_time = self.start_time.secsTo(self.end_time)
        progress_percentage = ((total_time - time_left) / total_time) * 100
        self.progress_bar.setValue(progress_percentage)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressBarApp()
    window.show()
    sys.exit(app.exec_())
