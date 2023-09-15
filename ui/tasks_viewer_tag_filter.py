from PySide2 import QtWidgets
from operations.tiny_ops.tags_ops import TagsOps
from operations.schemas.tags_schema import TagsSchema
from operations.tdb_attributes_definitions import TagsAttributesDefinitions


class TagFilterButtonWDG(QtWidgets.QPushButton):
    def __init__(self, name, parent=None):
        super(TagFilterButtonWDG, self).__init__(parent)

        self.button_name = name
        self.set_button_name()

    def set_button_name(self):
        self.setText(self.button_name)


class TasksViewerTagFilterBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TasksViewerTagFilterBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.refresh_btn = QtWidgets.QPushButton("Refresh Tags List")
        self.refresh_btn.setMaximumWidth(100)

    def create_layout(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.refresh_btn)
        self.main_layout.setContentsMargins(0,0,0,0)


class TasksViewerTagFilterCore(TasksViewerTagFilterBuild):
    def __init__(self, parent=None):
        super(TasksViewerTagFilterCore, self).__init__(parent)

        self.tag_key_definitions = TagsAttributesDefinitions()
        self.tag_schema = TagsSchema(self.tag_key_definitions)
        self.taops = TagsOps()

        self.create_connections()
        self.update_tags()

    def create_connections(self):
        self.refresh_btn.clicked.connect(self.update_tags)

    def update_tags(self):
        self.clear_layout()
        get_all_tags = self.taops.get_all_documents(ids=True)
        if get_all_tags:
            for tag_id, docs in get_all_tags.items():
                tag_name = docs[self.tag_key_definitions.name]
                button = TagFilterButtonWDG(name=tag_name)
                self.main_layout.addWidget(button)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.refresh_btn)
        self.setLayout(self.main_layout)

    def clear_layout(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget and widget != self.refresh_btn:
                widget.deleteLater()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TasksViewerTagFilterCore()
    test_dialog.show()
    sys.exit(app.exec_())