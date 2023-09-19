from PySide2 import QtWidgets, QtCore

from operations.tdb_attributes_definitions import TagsAttributesDefinitions, TaskAttributesDefinitions
from operations.tdb_attributes_paths import TagsAttributesPaths, TasksAttributesPaths
from operations.tiny_ops.tags_ops import TagsOps
from operations.tiny_ops.tasks_ops import TinyOps

class TaskTagsWDG(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(TaskTagsWDG, self).__init__(parent)

        self.tag_key_definitions = TagsAttributesDefinitions()
        self.taops = TagsOps()
        self.tops = TinyOps()
        self.tags_attr_paths = TagsAttributesPaths(self.tag_key_definitions)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.task_tags_cb = QtWidgets.QComboBox()
        self.task_tags_cb.addItems(self.get_db_tags())
        self.task_tags_lw = QtWidgets.QListWidget()
        self.task_tags_lw.setMaximumHeight(100)

        self.clear_btn = QtWidgets.QPushButton("Clear")
        self.clear_btn.setMaximumWidth(40)

    def create_layout(self):
        list_button_layout = QtWidgets.QHBoxLayout()
        list_button_layout.addWidget(self.task_tags_cb)
        list_button_layout.addWidget(self.clear_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.task_tags_lw)
        main_layout.addLayout(list_button_layout)

    def create_connections(self):
        self.task_tags_cb.activated.connect(self.add_item_to_list_wdg)
        self.clear_btn.clicked.connect(self.clear_tags_list)

    def populate_list(self, items: list):
        already_used = self.get_assigned_tags()
        for item in items:
            if item not in already_used:
                item = QtWidgets.QListWidgetItem(item)
                self.task_tags_lw.addItem(item)

    def clear_tags_list(self):
        self.task_tags_lw.clear()

    def add_item_to_list_wdg(self, index):
        selected_item = self.task_tags_cb.currentText()
        already_used = self.get_assigned_tags()

        if selected_item not in already_used:
            item = QtWidgets.QListWidgetItem(selected_item)
            self.task_tags_lw.addItem(item)
        else:
            print ("Tag already assigned!")

    def return_tags(self):
        current_tags = self.get_assigned_tags()
        return current_tags

    def get_db_tags(self):
        all_tags = self.taops.get_all_documents()
        tag_names = [tag[self.tag_key_definitions.name] for tag in all_tags]
        return tag_names

    def refresh_tag_box(self):
        self.task_tags_cb.clear()
        self.task_tags_cb.addItems(self.get_db_tags())

    def get_assigned_tags(self):
        items = []
        for index in range(self.task_tags_lw.count()):
            item = self.task_tags_lw.item(index)
            if item:
                items.append(item.text())
        return items


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskTagsWDG()
    xx = test_dialog.get_db_tags()
    print(xx)

    test_dialog.show()
    sys.exit(app.exec_())
