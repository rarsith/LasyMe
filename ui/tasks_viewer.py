from PySide2 import QtWidgets, QtCore
from operations.tiny_ops.tasks_ops import TinyOps
from ui.custom_widgets.task_entry_item_widget import TaskEntityCore
from operations.tdb_attributes_paths import TasksAttributesPaths
from operations.tdb_attributes_definitions import TaskAttributesDefinitions
from ui.custom_widgets.task_viewer_widget import ExitingTasksViewerWDG
from operations.tdb_priorities import Priorities
from operations.tdb_statuses import Statuses
from common_utils.date_time import DateTime


class ExitingTasksViewerBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.task_viewer_trw = ExitingTasksViewerWDG()
        self.by_prio_btn = QtWidgets.QPushButton("by Prio")
        self.by_status_btn = QtWidgets.QPushButton("by Status")
        # self.by_heat_btn = QtWidgets.QPushButton("by Heat")
        self.by_end_date_btn = QtWidgets.QPushButton("by DDate")

        self.refresh_btn = QtWidgets.QPushButton("Refresh")

    def create_layout(self):
        buttons_layout = QtWidgets.QGridLayout()
        buttons_layout.addWidget(self.by_prio_btn, 0, 1)
        buttons_layout.addWidget(self.by_end_date_btn, 0, 0)
        # buttons_layout.addWidget(self.by_heat_btn, 0, 2)
        buttons_layout.addWidget(self.by_status_btn, 0, 3)
        # buttons_layout.addStretch(1)

        task_viewer_layout = QtWidgets.QVBoxLayout()
        task_viewer_layout.addLayout(buttons_layout)
        task_viewer_layout.addWidget(self.task_viewer_trw)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(task_viewer_layout)
        main_layout.addWidget(self.refresh_btn)


class ExistingTasksViewerCore(ExitingTasksViewerBuild):
    task_document_retrieval = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(ExistingTasksViewerCore, self).__init__(parent)

        self.tiny_ops = TinyOps()
        self.tiny_attr_definitions = TaskAttributesDefinitions()
        self.tiny_attr_paths = TasksAttributesPaths(self.tiny_attr_definitions)

        # self.populate_tasks_custom()
        self.populate_tasks()
        self.create_connections()
        # self.delete_tasks()


    def populate_tasks_custom(self, key_to_sort):
        self.task_viewer_trw.clear()
        all_documents = self.tiny_ops.get_all_documents(ids=True)
        sorted_tasks = dict(sorted(all_documents.items(), key=lambda item: item[1][key_to_sort]))
        for key, value in sorted_tasks.items():
            if value["parent"] == "root":
                root_item = self.task_viewer_trw.invisibleRootItem()
                self.add_custom_widget(root_item, task_id=key)

            self.task_viewer_trw.expandAll()

    def populate_tasks_to_list(self, key_to_sort, order_ref=[]):
        self.task_viewer_trw.clear()

        all_documents = self.tiny_ops.get_all_documents(ids=True)
        sorted_tasks = dict(sorted(all_documents.items(), key=lambda item: order_ref.index(item[1][key_to_sort])))
        for key, value in sorted_tasks.items():
            if value["parent"] == "root":
                root_item = self.task_viewer_trw.invisibleRootItem()
                self.add_custom_widget(root_item, task_id=key)

            self.task_viewer_trw.expandAll()


    def populate_tasks(self):
        self.task_viewer_trw.clear()
        all_documents = self.tiny_ops.get_all_documents(ids=True)
        for key, value in all_documents.items():
            print({key:value})
            if value["parent"] == "root":
                root_item = self.task_viewer_trw.invisibleRootItem()
                self.add_custom_widget(root_item, task_id=key)

            self.task_viewer_trw.expandAll()
        self.sort_by_end_date()

    def create_connections(self):
        self.task_viewer_trw.itemPressed.connect(self.retrieve_task_doc)
        self.refresh_btn.clicked.connect(self.refresh_all)
        self.by_end_date_btn.clicked.connect(self.sort_by_end_date)
        self.by_prio_btn.clicked.connect(self.sort_by_prio)
        self.by_status_btn.clicked.connect(self.sort_by_status)

    def sort_by_end_date(self):
        self.populate_tasks_custom(self.tiny_attr_definitions.end_date_interval)

    def sort_by_prio(self):
        priority_order = Priorities().all_priorities
        self.populate_tasks_to_list(key_to_sort=self.tiny_attr_definitions.prio, order_ref=priority_order)

    def sort_by_status(self):
        statuses_order = Statuses().all_statuses
        self.populate_tasks_to_list(key_to_sort=self.tiny_attr_definitions.status, order_ref=statuses_order)


    def retrieve_task_doc(self, item, column):
        if item is not None:
            text = item.text(6)
            task_doc = self.tiny_ops.get_doc_by_id(int(text))
            complete_task_emit = {}
            complete_task_emit["task_id_emit"] = text
            complete_task_emit["task_emit"] = task_doc
            self.task_document_retrieval.emit(complete_task_emit)
            return task_doc

    def add_custom_widget(self, parent_item, task_id):
        child_item = QtWidgets.QTreeWidgetItem(parent_item)

        custom_widget_container = TaskEntityCore()
        custom_widget_container.get_progress_bar_amount(task_id)
        custom_widget_container.get_task_title(task_id)
        custom_widget_container.get_task_status(task_id)
        custom_widget_container.get_task_prio(task_id)

        custom_widget_container.delete_btn.clicked.connect(self.delete_task)
        custom_widget_container.prio_cb.activated.connect(self.update_task_prio)
        custom_widget_container.status_cb.activated.connect(self.update_task_status)

        self.task_viewer_trw.setItemWidget(child_item, 0, custom_widget_container.prog_bar)
        self.task_viewer_trw.setItemWidget(child_item, 1, custom_widget_container.task_title_lb)
        self.task_viewer_trw.setItemWidget(child_item, 2, custom_widget_container.status_cb)
        self.task_viewer_trw.setItemWidget(child_item, 3, custom_widget_container.prio_cb)
        self.task_viewer_trw.setItemWidget(child_item, 4, custom_widget_container.delete_btn)

        child_item.setText(6, str(task_id))
        return child_item

    def handle_item_dropped(self, parent_item, dropped_index, item):
        if parent_item is not None:
            # Retrieve the text from a specific column (e.g., column 2)
            specific_column_text = item.text(6)

            # Determine the row where the item is dropped
            dropped_row = self.tree_widget.indexOfTopLevelItem(parent_item)

            print(f"Text from column 6 of the dropped item: {specific_column_text}")
            print(f"Item dropped onto row {dropped_row}")


    def refresh_all(self):
        self.task_viewer_trw.clear()
        self.populate_tasks()

    def update_task_status(self):
        sender_button = self.sender()
        row = self.task_viewer_trw.indexAt(sender_button.pos()).row()
        column = self.task_viewer_trw.indexAt(sender_button.pos()).column()
        index = self.task_viewer_trw.model().index(row, column)
        item = self.task_viewer_trw.itemFromIndex(index)

        value_selected = sender_button.currentText()
        task_id = item.text(6)
        self.tiny_ops.update_task(int(task_id), self.tiny_attr_paths.status(value_selected))

    def update_task_prio(self):
        sender_button = self.sender()
        row = self.task_viewer_trw.indexAt(sender_button.pos()).row()
        column = self.task_viewer_trw.indexAt(sender_button.pos()).column()
        index = self.task_viewer_trw.model().index(row, column)
        item = self.task_viewer_trw.itemFromIndex(index)

        value_selected = sender_button.currentText()
        task_id = item.text(6)
        self.tiny_ops.update_task(int(task_id), self.tiny_attr_paths.priority(value_selected))

    def delete_task(self):
        sender_button = self.sender()
        row = self.task_viewer_trw.indexAt(sender_button.pos()).row()
        column = self.task_viewer_trw.indexAt(sender_button.pos()).column()
        index = self.task_viewer_trw.model().index(row, column)
        item = self.task_viewer_trw.itemFromIndex(index)

        task_id = item.text(6)
        self.tiny_ops.delete_task(int(task_id))
        self.refresh_all()



if __name__=="__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = ExistingTasksViewerCore()
    test_dialog.show()
    sys.exit(app.exec_())
