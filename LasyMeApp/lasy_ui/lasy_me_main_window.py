from PySide2 import QtWidgets
from LasyMeApp.lasy_ui.to_do_ui import ToDoMeMainCore
from LasyMeApp.lasy_ui.lasy_me_configuration_manager import LasyMeConfigurationManager


class LasyMeMainWindow(QtWidgets.QMainWindow):
    WINDOW_TITLE = "Lasy Me"

    def __init__(self, parent=None):
        super(LasyMeMainWindow, self).__init__(parent)

        self.setGeometry(500, 500, 1200, 700)
        self.setWindowTitle(self.WINDOW_TITLE)

        central_widget = ToDoMeMainCore()
        self.setCentralWidget(central_widget)

        self.create_widgets()
        self.create_connections()

    def create_widgets(self):
        self.open_config_manager_wdg = LasyMeConfigurationManager()

        self.edit_menu = self.menuBar()
        # self.edit_menu.addMenu("Edit")
        self.edit_config_action = QtWidgets.QAction("Edit Configuration", self)

        self.edit_menu.addAction(self.edit_config_action)

    def create_connections(self):
        self.edit_config_action.triggered.connect(self.open_config_manager)

    def open_config_manager(self):
        self.open_config_manager_wdg.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeMainWindow()
    test_dialog.show()

    sys.exit(app.exec_())


