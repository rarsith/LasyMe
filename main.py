import os
import sys
from PySide2 import QtWidgets
from lasy_ops.connection import LasyConnections
from lasy_ui.lasy_me_main_window import LasyMeMainWindow

root_app = LasyConnections().lasy_root_path
qss_style_file = "lasy_ui/stylesheets/dark_orange/dark_orange_style.qss"
full_qss_path = os.path.join(root_app, qss_style_file)

def main():
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeMainWindow()
    test_dialog.show()
    with open(full_qss_path, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())


if __name__ == "__main__":
    os.environ["LASY_DATA_ROOT"] = 'C:\\Users\\arsithra\\PycharmProjects\\LasyMe'
    main()
