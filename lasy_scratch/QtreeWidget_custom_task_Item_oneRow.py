from PySide2 import QtWidgets


class TaskEntityWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskEntityWDG, self).__init__(parent)

        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        self.progress_bar = QtWidgets.QProgressBar()
        self.progress_bar.setMaximumHeight(5)
        self.progress_bar.setValue(95)
        self.progress_bar.setTextVisible(False)

        self.task_title_lb = QtWidgets.QLabel("This is a sample Task Title Text......................XXXXXXXX")

        self.status_cb = QtWidgets.QComboBox()
        self.status_cb.addItems(["Done", "Blocked", "In Progress"])
        # self.status_cb.setFixedSize(100, 20)

        self.prio_cb = QtWidgets.QComboBox()
        self.prio_cb.addItems(["Normal", "Medium", "High", "Critical"])
        # self.prio_cb.setFixedSize(60, 20)

        self.edit_btn = QtWidgets.QPushButton("Edit")
        # self.edit_btn.setFixedSize(40, 20)

        self.delete_btn = QtWidgets.QPushButton("X")
        # self.delete_btn.setFixedSize(20, 20)

        self.heat_bar_lb = QtWidgets.QLabel()
        # self.heat_bar_lb.setFixedSize(20, 20)

        self.heat_bar_lb.setStyleSheet("background-color: lightgreen")

    def layout_widgets(self):
        statuses_layout = QtWidgets.QGridLayout()
        statuses_layout.addWidget(self.status_cb, 0, 1)
        statuses_layout.addWidget(self.prio_cb, 0, 2)
        statuses_layout.addWidget(self.edit_btn, 0, 3)
        statuses_layout.addWidget(self.delete_btn, 0, 4)

        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.VLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        separator_02 = QtWidgets.QFrame()
        separator_02.setFrameShape(QtWidgets.QFrame.VLine)
        separator_02.setFrameShadow(QtWidgets.QFrame.Sunken)

        main_layout = QtWidgets.QGridLayout(self)
        # main_layout.setSpacing(0)
        main_layout.addWidget(self.heat_bar_lb, 0, 0)
        # main_layout.addWidget(separator)
        main_layout.addWidget(self.task_title_lb, 0, 1)
        main_layout.setRowStretch(0, 1)
        # main_layout.addWidget(separator_02)
        main_layout.addLayout(statuses_layout, 0, 2)
        main_layout.addWidget(self.progress_bar, 1, 0, 1, 9) # (widget, row, column, rowSpan, colSpan)


if __name__=="__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskEntityWDG()
    test_dialog.show()
    sys.exit(app.exec_())