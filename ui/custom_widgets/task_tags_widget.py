from PySide2 import QtWidgets


class TaskTagsWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskTagsWDG, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.task_tags_cb = QtWidgets.QComboBox()
        self.task_tags_cb.addItems(["Item 1", "Item 2", "Item 3"])
        self.task_tags_le = QtWidgets.QLineEdit()

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.task_tags_le)
        main_layout.addWidget(self.task_tags_cb)

    def create_connections(self):
        self.task_tags_cb.currentIndexChanged.connect(self.add_item_to_line_edit)


    def add_item_to_line_edit(self, index):
        selected_item = self.task_tags_cb.currentText()
        current_text = self.task_tags_le.text()
        if current_text:
            self.task_tags_le.setText(current_text + ", " + selected_item)
        else:
            self.task_tags_le.setText(selected_item)

    def return_tags(self):
        current_tags =  self.task_tags_le.text()
        return current_tags
