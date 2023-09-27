import os
from PySide2 import QtWidgets
from lasy_ui.to_do_ui import ToDoMeMainCore
from lasy_ui.lasy_me_configuration_manager import LasyMeConfigurationManager
from lasy_ops.connection import LasyConnections


class LasyMeMainWindow(QtWidgets.QMainWindow):
    WINDOW_TITLE = "Lasy Me"

    def __init__(self, parent=None):
        super(LasyMeMainWindow, self).__init__(parent)

        self.setGeometry(700, 400, 1200, 700)
        self.setWindowTitle(self.WINDOW_TITLE)

        self.create_widgets()
        self.create_connections()
        self.check_if_folders_exist()
        central_widget = ToDoMeMainCore()
        self.setCentralWidget(central_widget)

    def create_widgets(self):
        self.edit_menu = self.menuBar()
        self.edit_config_action = QtWidgets.QAction("Edit Configuration", self)
        self.edit_menu.addAction(self.edit_config_action)

    def create_connections(self):
        self.edit_config_action.triggered.connect(self.open_config_manager)

    def open_config_manager(self):
        self.open_config_manager_wdg = LasyMeConfigurationManager()
        self.open_config_manager_wdg.setGeometry(1000, 500, 500, 400)
        self.open_config_manager_wdg.show()

    def check_if_folders_exist(self):
        get_root = os.environ.get("LASY_DATA_ROOT")
        print(get_root)
        LasyConnections().create_implicit_structure(get_root)

    def activate_main(self):
        self.setEnabled(True)
        self.activateWindow()
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeMainWindow()
    test_dialog.show()
    sys.exit(app.exec_())


