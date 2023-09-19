import sys
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore


class TaskDailyAllocationWDG(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super(TaskDailyAllocationWDG, self).__init__(parent)

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QtGui.QPainter(self)
        palette = self.palette()
        total_chunks = sum(chunk for chunk, _ in self.window().chunk_data)
        chunk_height = self.height() / total_chunks

        current_position = 0
        for chunk, color in self.window().chunk_data:
            chunk_height_pixels = int(chunk * chunk_height)
            chunk_rect = QtCore.QRectF(0, current_position * chunk_height, self.width(), chunk_height_pixels)

            palette.setColor(QtGui.QPalette.Highlight, color)
            painter.fillRect(chunk_rect, palette.brush(QtGui.QPalette.Highlight))

            current_position += chunk

class TaskDailyAllocationBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskDailyAllocationBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.progress_bar = TaskDailyAllocationWDG()
        self.progress_bar.setOrientation(QtCore.Qt.Vertical)

    def create_layout(self):
        frame = QtWidgets.QFrame()
        frame.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Plain)
        frame.setLineWidth(1)

        layout = QtWidgets.QVBoxLayout(frame)
        layout.addWidget(self.progress_bar)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(frame)

        # List of integers representing chunks and their corresponding colors
        self.chunk_data = [(10, QtGui.QColor(0, 124, 0)),  # (chunk, color)
                           (20, QtGui.QColor(255, 165, 0)),
                           (15, QtGui.QColor(255, 0, 0)),
                           (10, QtGui.QColor(0, 0, 255)),
                           (5, QtGui.QColor(0, 0, 124))]

        # Initialize the progress bar with chunks
        self.initialize_progress_bar()

    def initialize_progress_bar(self):
        total_chunks = sum(chunk for chunk, _ in self.chunk_data)
        print(total_chunks)

        # Set the range and initial value of the progress bar
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(total_chunks)
        self.progress_bar.setValue(0)

        # Start processing the chunks
        self.process_chunks()

    def process_chunks(self):
        for chunk, _ in self.chunk_data:
            self.progress_bar.setValue(self.progress_bar.value() + chunk)
            QtWidgets.QApplication.processEvents()  # Allow the UI to update


class Testing(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Testing, self).__init__(parent)

        self.progg = TaskDailyAllocationBuild()

        self.main_layout = QtWidgets.QHBoxLayout(self)

        self.update_tags()

    def update_tags(self):
        self.clear_layout()
        test_list = 5
        for tag_id in range(0, test_list):
            self.main_layout.addWidget(self.progg)

    def clear_layout(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget and widget != self.refresh_btn:
                widget.deleteLater()

if __name__ == "__main__":
    chunk_data = [(10, QtGui.QColor(0, 124, 0)),  # (chunk, color)
                  (20, QtGui.QColor(255, 165, 0)),
                  (15, QtGui.QColor(255, 0, 0)),
                  (10, QtGui.QColor(0, 0, 255)),
                  (5, QtGui.QColor(0, 0, 124))]


    app = QtWidgets.QApplication(sys.argv)
    window = Testing()
    window.show()
    sys.exit(app.exec_())
