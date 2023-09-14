from PySide2 import QtWidgets, QtCore, QtGui


class TaskPreviewPropertiesBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskPreviewPropertiesBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.priority_lb = QtWidgets.QLabel("---")
        self.priority_lb.adjustSize()

        self.duration_lb = QtWidgets.QLabel("---")
        self.duration_lb.adjustSize()

        self.start_lb = QtWidgets.QLabel("---")
        self.start_lb.adjustSize()

        self.end_lb = QtWidgets.QLabel("---")
        self.end_lb.adjustSize()

        self.task_title_le = QtWidgets.QLineEdit()
        self.task_title_le.setPlaceholderText("Task Title: ")
        self.task_title_le.setDisabled(True)
        self.task_title_le.setMinimumWidth(200)

    def create_layout(self):
        separator01 = QtWidgets.QFrame()
        separator01.setFrameShape(QtWidgets.QFrame.VLine)
        separator01.setFrameShadow(QtWidgets.QFrame.Sunken)

        separator02 = QtWidgets.QFrame()
        separator02.setFrameShape(QtWidgets.QFrame.VLine)
        separator02.setFrameShadow(QtWidgets.QFrame.Sunken)

        separator03 = QtWidgets.QFrame()
        separator03.setFrameShape(QtWidgets.QFrame.VLine)
        separator03.setFrameShadow(QtWidgets.QFrame.Sunken)

        labels_layout = QtWidgets.QHBoxLayout()
        labels_layout.addWidget(self.priority_lb)
        labels_layout.addWidget(separator01)
        labels_layout.addWidget(self.start_lb)
        labels_layout.addWidget(separator02)
        labels_layout.addWidget(self.end_lb)
        labels_layout.addWidget(separator03)
        labels_layout.addWidget(self.duration_lb)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.task_title_le)
        main_layout.addLayout(labels_layout)


class TaskPreviewPropertiesCore(TaskPreviewPropertiesBuild):
    def __init__(self, parent=None):
        super(TaskPreviewPropertiesCore, self).__init__(parent)

    def update_task_title_wdg(self, value):
        self.task_title_le.clear()
        self.task_title_le.setText("Task Title: {}".format(value))

    def update_priority_wdg(self, value):
        self.priority_lb.clear()
        self.priority_lb.setText("{}".format(value))

    def update_duration_wdg(self, value):
        self.duration_lb.clear()
        self.duration_lb.setText("{} min".format(value))

    def update_start_wdg(self, value):
        self.start_lb.clear()
        self.start_lb.setText("{}".format(value))

    def update_end_wdg(self, value):
        self.end_lb.clear()
        self.end_lb.setText("{}".format(value))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskPreviewPropertiesCore()
    test_dialog.update_task_title_wdg("This is the title")
    test_dialog.update_priority_wdg("CRITICAL")
    test_dialog.update_duration_wdg("60")
    test_dialog.update_start_wdg("2023-09-13")
    test_dialog.update_end_wdg("2023-09-15")
    test_dialog.show()
    sys.exit(app.exec_())