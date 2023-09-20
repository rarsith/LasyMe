import sys
from PySide2 import QtWidgets
from lasy_me_ui.lasy_me_main_window import LasyMeMainWindow


def main():

    qss_style_file = "lasy_me_ui/stylesheets/dark_orange/dark_orange_style.qss"

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeMainWindow()
    test_dialog.show()

    with open(qss_style_file, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
