from PySide2 import QtWidgets


class TaskTagManagerBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskTagManagerBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.tag_viewer_lw = QtWidgets.QListWidget()
        self.tag_input_le = QtWidgets.QLineEdit()
        self.tag_input_le.setPlaceholderText("New Tag Name")
        self.create_tag_btn = QtWidgets.QPushButton("Create")
        self.delete_tag_btn = QtWidgets.QPushButton("Delete")
        self.export_tags_btn = QtWidgets.QPushButton("Export...")
        self.import_tags_btn = QtWidgets.QPushButton("Import...")

    def create_layout(self):
        buttons_layout = QtWidgets.QGridLayout()
        buttons_layout.addWidget(self.create_tag_btn, 0, 0, 1, 2)
        buttons_layout.addWidget(self.delete_tag_btn, 1, 0, 1, 2)
        buttons_layout.addWidget(self.export_tags_btn, 2, 0)
        buttons_layout.addWidget(self.import_tags_btn, 2, 1)

        viewer_and_input_layout = QtWidgets.QVBoxLayout()
        viewer_and_input_layout.addWidget(self.tag_viewer_lw)
        viewer_and_input_layout.addWidget(self.tag_input_le)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(viewer_and_input_layout)
        main_layout.addLayout(buttons_layout)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskTagManagerBuild()
    test_dialog.show()
    sys.exit(app.exec_())