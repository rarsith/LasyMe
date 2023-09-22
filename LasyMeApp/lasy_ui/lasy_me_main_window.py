from PySide2 import QtWidgets
from LasyMeApp.lasy_ui.to_do_ui import ToDoMeMainCore
from LasyMeApp.lasy_common_utils import config_file_utils
from LasyMeApp.lasy_ui.lasy_me_configuration_manager import LasyMeConfigurationManager


class LasyMeMainWindow(QtWidgets.QMainWindow):
    WINDOW_TITLE = "Lasy Me"

    def __init__(self, parent=None):
        super(LasyMeMainWindow, self).__init__(parent)

        self.setGeometry(700, 400, 1200, 700)
        self.setWindowTitle(self.WINDOW_TITLE)

        central_widget = ToDoMeMainCore()
        self.setCentralWidget(central_widget)

        self.create_widgets()
        self.create_connections()
        self.check_if_custom_config()

    def create_widgets(self):
        self.open_config_manager_wdg = LasyMeConfigurationManager()
        self.open_config_manager_wdg.setGeometry(1000, 500, 500, 400)

        self.edit_menu = self.menuBar()
        # self.edit_menu.addMenu("Edit")
        self.edit_config_action = QtWidgets.QAction("Edit Configuration", self)

        self.edit_menu.addAction(self.edit_config_action)

    def create_connections(self):
        self.edit_config_action.triggered.connect(self.open_config_manager)
        self.open_config_manager_wdg.closed.connect(self.activate_main)

    def open_config_manager(self):
        self.open_config_manager_wdg.exec_()

    def check_if_custom_config(self):
        custom_config_exists = config_file_utils.custom_config_exists()
        if not custom_config_exists:
            self.setEnabled(False)
            self.open_config_manager_wdg.cancel_btn.setDisabled(True)
            self.open_config_manager_wdg.exec_()

    def activate_main(self):
        self.setEnabled(True)
        # self.config_manager.show()
        self.activateWindow()
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeMainWindow()
    test_dialog.show()
    sys.exit(app.exec_())


