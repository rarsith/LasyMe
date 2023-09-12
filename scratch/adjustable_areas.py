import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSplitter, QTextEdit, QAction, QMenu, \
    QMenuBar
from PySide2.QtCore import Qt, QSettings


class AdjustableLayoutWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Adjustable Layout Example")
        self.setGeometry(100, 100, 800, 600)

        # Create the main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # Create the top and bottom splitters
        self.top_splitter = QSplitter(self)
        self.bottom_splitter = QSplitter(self)

        # Create QTextEdit widgets for each section
        self.text_edit1 = QTextEdit()
        self.text_edit2 = QTextEdit()
        self.text_edit3 = QTextEdit()
        self.text_edit4 = QTextEdit()

        # Add the QTextEdit widgets to the top splitter
        self.top_splitter.addWidget(self.text_edit1)
        self.top_splitter.addWidget(self.text_edit2)

        # Add the QTextEdit widgets to the bottom splitter
        self.bottom_splitter.addWidget(self.text_edit3)
        self.bottom_splitter.addWidget(self.text_edit4)

        # Create an additional horizontal splitter within the top splitter
        self.horizontal_splitter = QSplitter(Qt.Horizontal)
        self.horizontal_splitter.addWidget(self.top_splitter)

        # Load the saved splitter sizes
        self.load_layout()

        # Add the horizontal splitter with the top splitter to the main splitter
        main_splitter = QSplitter(self)
        main_splitter.setOrientation(Qt.Vertical)
        main_splitter.addWidget(self.horizontal_splitter)
        main_splitter.addWidget(self.bottom_splitter)

        # Set the main layout for the main widget
        main_layout.addWidget(main_splitter)
        main_widget.setLayout(main_layout)

        # Set the central widget
        self.setCentralWidget(main_widget)

        # Create a "Save Layout" action
        save_layout_action = QAction("Save Layout", self)
        save_layout_action.triggered.connect(self.save_layout)

        # Create a "File" menu and add the "Save Layout" action
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(save_layout_action)

    def save_layout(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
        settings_file_path = os.path.join(script_directory, "settings.ini")  # Specify the settings file path

        settings = QSettings(settings_file_path, QSettings.IniFormat)  # Use IniFormat for .ini files

        # Save sizes of all three splitters
        top_sizes = [int(size) for size in self.top_splitter.sizes()]
        bottom_sizes = [int(size) for size in self.bottom_splitter.sizes()]
        horizontal_sizes = [int(size) for size in self.horizontal_splitter.sizes()]

        settings.setValue("top_splitter_sizes", top_sizes)
        settings.setValue("bottom_splitter_sizes", bottom_sizes)
        settings.setValue("horizontal_splitter_sizes", horizontal_sizes)

    def load_layout(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        settings_file_path = os.path.join(script_directory, "settings.ini")

        settings = QSettings(settings_file_path, QSettings.IniFormat)

        # Load sizes of all three splitters
        top_sizes = settings.value("top_splitter_sizes")
        bottom_sizes = settings.value("bottom_splitter_sizes")
        horizontal_sizes = settings.value("horizontal_splitter_sizes")

        if top_sizes:
            self.top_splitter.setSizes([int(size) for size in top_sizes])
        if bottom_sizes:
            self.bottom_splitter.setSizes([int(size) for size in bottom_sizes])
        if horizontal_sizes:
            self.horizontal_splitter.setSizes([int(size) for size in horizontal_sizes])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdjustableLayoutWindow()
    window.show()
    sys.exit(app.exec_())
