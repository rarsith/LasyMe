import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget, QPushButton
from PySide2.QtCore import Qt

class ProgressBarWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Colored QProgressBar Example")
        self.setGeometry(100, 100, 400, 200)

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QProgressBar widget
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        # Set the range for the progress bar (0 to 100 in this example)
        self.progress_bar.setRange(0, 100)

        # Create a button to update the progress
        update_button = QPushButton("Update Progress", self)
        update_button.clicked.connect(self.update_progress)
        layout.addWidget(update_button)

    def update_progress(self):
        # Update the progress bar's value (in this example, it's updated by 10 units)
        current_value = self.progress_bar.value()
        new_value = current_value + 10
        self.progress_bar.setValue(new_value)

        # Customize the color based on the current value
        self.set_progress_color(new_value)

    def set_progress_color(self, value):
        palette = self.progress_bar.palette()

        if value <= 30:
            # Set color to green for values up to 30
            palette.setColor(QPalette.Highlight, Qt.green)
        elif value <= 70:
            # Set color to yellow for values between 31 and 70
            palette.setColor(QPalette.Highlight, Qt.yellow)
        else:
            # Set color to red for values above 70
            palette.setColor(QPalette.Highlight, Qt.red)

        self.progress_bar.setPalette(palette)

def main():
    app = QApplication(sys.argv)
    window = ProgressBarWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
