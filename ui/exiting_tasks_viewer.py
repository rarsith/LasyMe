from PySide2 import QtWidgets, QtCore
from operations.tiny_ops import TinyOps
from operations.connection import Session
from ui.custom_widgets.task_entry_item import TaskEntityWDG



class ExitingTasksViewerWDG(QtWidgets.QTreeWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerWDG, self).__init__(parent)

        self.widget_width = 500
        self.create_widgets()

    def create_widgets(self):

        self.setDragEnabled(True)
        self.setDragDropMode(QtWidgets.QTreeWidget.InternalMove)
        self.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.setDisabled(False)
        self.setMinimumWidth(self.widget_width)

        self.widget_columns_names = ["Heat", "Task Title", "Status", "Prio", "Edit", "Delete"]
        self.setColumnCount(len(self.widget_columns_names))
        self.setHeaderLabels(self.widget_columns_names)

        self.setColumnWidth(0, round(self.widget_width*0.005))
        self.setColumnWidth(1, round(self.widget_width*0.50))
        self.setColumnWidth(2, round(self.widget_width*0.10))
        self.setColumnWidth(3, round(self.widget_width*0.10))
        self.setColumnWidth(4, round(self.widget_width*0.10))
        self.setColumnWidth(5, round(self.widget_width*0.05))


class ExitingTasksViewerBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ExitingTasksViewerBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.task_viewer_trw = ExitingTasksViewerWDG()
        self.by_prio_btn = QtWidgets.QPushButton("by Prio")
        self.by_status_btn = QtWidgets.QPushButton("by Status")
        self.by_heat_btn = QtWidgets.QPushButton("by Heat")
        self.by_end_date_btn = QtWidgets.QPushButton("by DDate")

        self.refresh_btn = QtWidgets.QPushButton("Refresh")

    def create_layout(self):
        buttons_layout = QtWidgets.QGridLayout()
        buttons_layout.addWidget(self.by_prio_btn, 0, 0)
        buttons_layout.addWidget(self.by_end_date_btn, 0, 1)
        buttons_layout.addWidget(self.by_heat_btn, 0, 2)
        buttons_layout.addWidget(self.by_status_btn, 0, 3)
        # buttons_layout.addStretch(1)

        task_viewer_layout = QtWidgets.QVBoxLayout()
        task_viewer_layout.addLayout(buttons_layout)
        task_viewer_layout.addWidget(self.task_viewer_trw)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(task_viewer_layout)
        main_layout.addWidget(self.refresh_btn)


class ExistingTasksViewerCore(ExitingTasksViewerBuild):
    def __init__(self, parent=None):
        super(ExistingTasksViewerCore, self).__init__(parent)

        self.populate_tasks()
        # self.create_connections()
        # self.delete_tasks()

    def populate_tasks(self):
        # root_item = QtWidgets.QTreeWidgetItem(self.task_viewer_trw, ["FUCKING ROOT"])
        tiny_ops = TinyOps()
        all_documents = tiny_ops.get_all_documents(ids=True)
        for key, value in all_documents.items():
            root_item = self.task_viewer_trw.invisibleRootItem()
            item = self.addCustomWidget(root_item, "", task_id=key)
            self.task_viewer_trw.addTopLevelItem(item)

    def create_connections(self):
        self.task_viewer_trw.itemPressed.connect(self.handle_item_pressed)

    def handle_item_pressed(self, item, column):
        # self.addCustomWidget()
        # This slot will be called when an item is moved.
        print(f"Item pressed: {item.text(0)}")

    def addCustomWidget(self, parent_item, name, task_id):
        child_item = QtWidgets.QTreeWidgetItem(parent_item, [name])

        custom_widget_container = TaskEntityWDG()
        self.task_viewer_trw.setItemWidget(child_item, 0, custom_widget_container.progress_bar)
        custom_widget_container.get_progress_bar_amount(task_id)
        self.task_viewer_trw.setItemWidget(child_item, 1, custom_widget_container.task_title_lb)
        self.task_viewer_trw.setItemWidget(child_item, 2, custom_widget_container.status_cb)
        self.task_viewer_trw.setItemWidget(child_item, 3, custom_widget_container.prio_cb)
        self.task_viewer_trw.setItemWidget(child_item, 4, custom_widget_container.edit_btn)
        self.task_viewer_trw.setItemWidget(child_item, 5, custom_widget_container.delete_btn)
        return child_item


if __name__=="__main__":
    import sys




    app = QtWidgets.QApplication(sys.argv)
    test_dialog = ExistingTasksViewerCore()
    test_dialog.show()
    sys.exit(app.exec_())
