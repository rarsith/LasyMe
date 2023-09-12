from PySide2 import QtWidgets


class TaskPropertiesEditorBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskPropertiesEditorBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.text_viewer_ptx = QtWidgets.QPlainTextEdit()
        self.save_btn = QtWidgets.QPushButton("Update")

        self.assigned_to_cb = QtWidgets.QComboBox()
        self.start_date_interval_dte = QtWidgets.QDateEdit(calendarPopup=True)
        self.end_date_interval_dte = QtWidgets.QDateEdit(calendarPopup=True)
        self.set_tags_cb = QtWidgets.QComboBox()
        self.update_btn = QtWidgets.QPushButton("Update")

        self.start_lb = QtWidgets.QLabel("Start")
        self.end_lb = QtWidgets.QLabel("End")

        self.assigned_to_lb = QtWidgets.QLabel("User")
        self.tags_lb = QtWidgets.QLabel("Tags")

    def create_layout(self):
        win_layout = QtWidgets.QVBoxLayout()
        win_layout.addWidget(self.text_viewer_ptx)
        win_layout.addWidget(self.save_btn)

        start_date_layout = QtWidgets.QVBoxLayout()
        start_date_layout.addWidget(self.start_lb)
        start_date_layout.addWidget(self.start_date_interval_dte)

        end_date_layout = QtWidgets.QVBoxLayout()
        end_date_layout.addWidget(self.end_lb)
        end_date_layout.addWidget(self.end_date_interval_dte)

        dates_layout = QtWidgets.QHBoxLayout()
        dates_layout.addLayout(start_date_layout)
        dates_layout.addLayout(end_date_layout)

        misc_layout = QtWidgets.QFormLayout()
        misc_layout.addRow("User", self.assigned_to_cb)
        misc_layout.addRow("Tags", self.set_tags_cb)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(win_layout)
        main_layout.addLayout(dates_layout)
        main_layout.addLayout(misc_layout)
        main_layout.addWidget(self.update_btn)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskPropertiesEditorBuild()
    test_dialog.show()
    sys.exit(app.exec_())
