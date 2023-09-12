from PySide2 import QtWidgets


class TaskPreviewPropertiesBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskPreviewPropertiesBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.priority_lb = QtWidgets.QLabel("---")
        self.duration_lb = QtWidgets.QLabel("---")
        self.start_lb = QtWidgets.QLabel("---")
        self.end_lb = QtWidgets.QLabel("---")
        self.task_title_lb = QtWidgets.QLabel("---")
        self.task_title_lb.setMinimumWidth(200)

    def create_layout(self):
        labels_layout = QtWidgets.QHBoxLayout()
        labels_layout.addWidget(self.priority_lb)
        labels_layout.addWidget(self.start_lb)
        labels_layout.addWidget(self.end_lb)
        labels_layout.addWidget(self.duration_lb)
        labels_layout.addWidget(self.task_title_lb)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(labels_layout)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskPreviewPropertiesBuild()
    test_dialog.show()
    sys.exit(app.exec_())