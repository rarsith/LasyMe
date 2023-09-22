import sys
from PySide2 import QtWidgets
from LasyMeApp.lasy_common_utils import config_file_utils
from LasyMeApp.lasy_ui.lasy_me_main_window import LasyMeMainWindow
from LasyMeApp.lasy_ui.lasy_me_configuration_manager import LasyMeConfigurationManager


qss_style_file = "lasy_ui/stylesheets/dark_orange/dark_orange_style.qss"

def main():
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeMainWindow()

    test_dialog.show()

    with open(qss_style_file, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
