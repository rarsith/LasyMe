from PySide2 import QtWidgets, QtCore
from LasyMeApp.lasy_ops.tiny_ops.tags_ops import TagsOps
from LasyMeApp.lasy_ops.tiny_ops.tasks_ops import TinyOps
from LasyMeApp.lasy_ops.schemas.tags_schema import TagsSchema
from LasyMeApp.lasy_ops.tdb_attributes_definitions import TagsAttributesDefinitions


class TaskTagManagerBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskTagManagerBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.tag_viewer_lw = QtWidgets.QListWidget()
        self.tag_viewer_lw.setFocusPolicy(QtCore.Qt.NoFocus)

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


class TaskTagManagerCore(TaskTagManagerBuild):
    def __init__(self, parent=None):
        super(TaskTagManagerCore, self).__init__(parent)

        self.tag_key_definitions = TagsAttributesDefinitions()
        self.tag_schema = TagsSchema(self.tag_key_definitions)
        self.taops = TagsOps()
        self.tops = TinyOps()

        self.populate_tag_view()
        self.create_connections()

    def create_connections(self):
        self.tag_viewer_lw.itemClicked.connect(self.get_tag_id)
        self.create_tag_btn.clicked.connect(self.create_new_tag)
        self.delete_tag_btn.clicked.connect(self.delete_selected_tag)
        self.export_tags_btn.clicked.connect(self.export_tags)
        self.import_tags_btn.clicked.connect(self.import_tags)

    def create_new_tag(self):
        self.set_tag_name()
        exitings_tags = self.get_current_items()
        complete_doc = self.tag_schema.to_dict()
        has_content = self.tag_input_le.text()
        if not has_content.strip():
            print("No Tag Name specified. Please enter name")
            return
        elif has_content in exitings_tags:
            print("Tag already exists, choose another name")
            return

        else:
            self.taops.insert_tag(complete_doc)
            self.tag_input_le.clear()
            self.refresh_all()

    def get_current_items(self):
        items_names = []
        for index in range(self.tag_viewer_lw.count()):
            item = self.tag_viewer_lw.item(index)
            item_name = item.text()
            items_names.append(item_name)
        return items_names

    def set_tag_name(self):
        get_tag_name = self.tag_input_le.text()
        self.tag_schema.tag_name = get_tag_name

    def delete_selected_tag(self):
        tag_id = self.tag_viewer_lw.currentItem().data(1)
        get_tag_name = self.taops.get_tag_by_id(tag_id)
        self.taops.delete_tag(tag_id)
        self.tops.get_docs_by_tags(get_tag_name["name"], remove=True)

        self.refresh_all()


    def export_tags(self):
        pass

    def import_tags(self):
        pass

    def populate_tag_view(self):
        get_all_tags = self.taops.get_all_documents(ids=True)
        if get_all_tags:
            for tag_id, docs in get_all_tags.items():
                tag_name = docs[self.tag_key_definitions.name]
                list_item = QtWidgets.QListWidgetItem(tag_name)
                list_item.setData(1, tag_id)
                self.tag_viewer_lw.addItem(list_item)
        else:
            pass

    def refresh_all(self):
        self.tag_viewer_lw.clear()
        self.populate_tag_view()

    def get_tag_id(self):
        current_item = self.tag_viewer_lw.currentItem().data(1)
        return current_item




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskTagManagerCore()
    test_dialog.show()
    sys.exit(app.exec_())