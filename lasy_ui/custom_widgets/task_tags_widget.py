from PySide2 import QtWidgets, QtCore

from lasy_ops.tdb_attributes_definitions import TagsAttributesDefinitions
from lasy_ops.tdb_attributes_paths import TagsAttributesPaths
from lasy_ops.tiny_ops.tags_ops import TagsOps
from lasy_ops.tiny_ops.tasks_ops import TinyOps


class TagFilterButtonWDG(QtWidgets.QPushButton):
    def __init__(self, name, parent=None):
        super(TagFilterButtonWDG, self).__init__(parent)

        self.button_name = name
        self.set_button_name()

    def set_button_name(self):
        self.setText(self.button_name)


class TasksViewerTagAssignerCore(QtWidgets.QWidget):
    assign_tag_button_info = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(TasksViewerTagAssignerCore, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.update_tags()

    def create_widgets(self):
        self.refresh_btn = QtWidgets.QPushButton("Refresh Tags List")
        self.refresh_btn.setMaximumWidth(100)

    def create_layout(self):
        self.buttons_layout = QtWidgets.QGridLayout()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addWidget(self.refresh_btn)
        self.main_layout.setContentsMargins(0,0,0,0)

    def create_connections(self):
        self.refresh_btn.clicked.connect(self.update_tags)

    def update_tags(self):
        self.tag_key_definitions = TagsAttributesDefinitions()
        self.taops = TagsOps()

        store_active = self.get_active_buttons()

        self.clear_layout()
        get_all_tags = self.taops.get_all_documents(ids=True)
        if get_all_tags:
            buttons_names = []
            for tag_id, docs in get_all_tags.items():
                tag_name = docs[self.tag_key_definitions.name]
                buttons_names.append(tag_name)

            for i, button_name in enumerate(buttons_names):
                self.button = TagFilterButtonWDG(name=button_name)
                self.button.clicked.connect(self.transmit_name)
                self.button.setCheckable(True)
                self.buttons_layout.addWidget(self.button, i // 3, i % 3)

        self.main_layout.addLayout(self.buttons_layout)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.refresh_btn)
        self.setLayout(self.main_layout)

        self.activate_tags(store_active)


    def clear_layout(self):
        while self.main_layout.count():
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget and widget != self.refresh_btn:
                widget.deleteLater()

    def activate_tags(self, buttons_names):
        self.reset_uncheck_all_buttons()
        if buttons_names:
            get_all_buttons_wdg = []
            for index in range(self.buttons_layout.count()):
                widget = self.buttons_layout.itemAt(index).widget()
                if isinstance(widget, QtWidgets.QPushButton):
                    get_all_buttons_wdg.append(widget)
            for tag_name in buttons_names:
                for button in get_all_buttons_wdg:
                    if tag_name == button.text():
                        button.setChecked(True)
        return

    def reset_uncheck_all_buttons(self):
        for index in range(self.buttons_layout.count()):
            widget = self.buttons_layout.itemAt(index).widget()
            widget.setChecked(False)

    def transmit_name(self):
        get_active_tags = self.get_active_buttons()
        self.assign_tag_button_info.emit({"assigned_tags": get_active_tags})

    def get_active_buttons(self):
        active_buttons = []
        for index in range(self.buttons_layout.count()):
            widget = self.buttons_layout.itemAt(index).widget()
            if isinstance(widget, QtWidgets.QPushButton) and widget.isChecked():
                active_buttons.append(widget.text())
        return active_buttons



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskTagsWDG()
    xx = test_dialog.get_db_tags()
    print(xx)

    test_dialog.show()
    sys.exit(app.exec_())
