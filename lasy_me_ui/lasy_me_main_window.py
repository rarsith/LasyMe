from PySide2 import QtWidgets

from lasy_me_ui.to_do_ui import ToDoMeMainCore


class LasyMeMainWindow(QtWidgets.QMainWindow):
    WINDOW_TITLE = "Lasy Me"

    def __init__(self, parent=None):
        super(LasyMeMainWindow, self).__init__(parent)

        self.setGeometry(500, 500, 1200, 700)
        self.setWindowTitle(self.WINDOW_TITLE)

        central_widget = ToDoMeMainCore()
        self.setCentralWidget(central_widget)
