from PySide2 import QtWidgets, QtCore


class InputTaskBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InputTaskBuild, self).__init__(parent)

        self.setMaximumHeight(170)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.task_input_ptx = QtWidgets.QPlainTextEdit()

        self.end_date = QtWidgets.QDateEdit(calendarPopup=True)
        self.end_date.setDateTime(QtCore.QDateTime.currentDateTime())


        self.thirty_min_btn = QtWidgets.QPushButton("30")
        self.sixty_min_btn = QtWidgets.QPushButton("60")
        self.ninety_min_btn = QtWidgets.QPushButton("90")

        self.low_prio_btn = QtWidgets.QPushButton("Low")

        self.normal_prio_btn = QtWidgets.QPushButton("Normal")
        self.med_prio_btn = QtWidgets.QPushButton("Medium")
        self.high_prio_btn = QtWidgets.QPushButton("High")
        self.critical_prio_btn = QtWidgets.QPushButton("Critical")

        self.set_parent_btn = QtWidgets.QPushButton("Set Parent...")

        self.create_task_btn = QtWidgets.QPushButton("Create")

    def create_layout(self):
        calendar_layout = QtWidgets.QFormLayout()
        calendar_layout.addRow("End Date", self.end_date)

        execution_buttons_layout = QtWidgets.QHBoxLayout()
        execution_buttons_layout.addWidget(self.thirty_min_btn)
        execution_buttons_layout.addWidget(self.sixty_min_btn)
        execution_buttons_layout.addWidget(self.ninety_min_btn)

        prio_buttons_layout = QtWidgets.QGridLayout()
        prio_buttons_layout.addWidget(self.normal_prio_btn, 0, 0)
        prio_buttons_layout.addWidget(self.med_prio_btn, 0, 1)
        prio_buttons_layout.addWidget(self.low_prio_btn, 0, 2)
        prio_buttons_layout.addWidget(self.high_prio_btn, 1, 0)
        prio_buttons_layout.addWidget(self.critical_prio_btn, 1, 1, 1, 2) # (widget, row, column, rowSpan, colSpan)
        prio_buttons_layout.addWidget(self.set_parent_btn, 2, 0, 1, 3) # (widget, row, column, rowSpan, colSpan)

        buttons_layout = QtWidgets.QVBoxLayout()
        buttons_layout.addLayout(calendar_layout)
        buttons_layout.addLayout(execution_buttons_layout)
        buttons_layout.addStretch(1)
        buttons_layout.addLayout(prio_buttons_layout)

        task_input_layout = QtWidgets.QHBoxLayout()
        task_input_layout.addWidget(self.task_input_ptx)
        task_input_layout.addLayout(buttons_layout)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(task_input_layout)
        main_layout.addWidget(self.create_task_btn)

    def create_connections(self):
        pass
        self.create_task_btn.clicked.connect(self.create_task_entry)

    def create_task_entry(self, parent_item, name, widget: QtWidgets.QTreeWidget):
        child_item = QtWidgets.QTreeWidgetItem(parent_item, [name])

        widget.setItemWidget(child_item, 0, self.progress_bar)
        widget.setItemWidget(child_item, 1, self.task_title_lb)
        widget.setItemWidget(child_item, 2, self.status_cb)
        widget.setItemWidget(child_item, 3, self.prio_cb)
        widget.setItemWidget(child_item, 4, self.edit_btn)
        widget.setItemWidget(child_item, 5, self.delete_btn)

        return child_item


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = InputTaskBuild()
    test_dialog.show()
    sys.exit(app.exec_())