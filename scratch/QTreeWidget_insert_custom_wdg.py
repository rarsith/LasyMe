import sys
from PySide2 import QtWidgets
from scratch.QtreeWidget_custom_task_Item_oneRow import TaskEntityWDG


class TaskDetailsWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskDetailsWDG, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.text_reader_pte = QtWidgets.QPlainTextEdit()


    def create_layout(self):
        pass


class TreeWidgetExample(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Widget in QTreeWidget Example")
        self.setGeometry(100, 100, 600, 400)

        self.tree_widget = QtWidgets.QTreeWidget(self)
        self.tree_widget.setHeaderLabels(["Column 0"])
        self.setCentralWidget(self.tree_widget)

        root_item = QtWidgets.QTreeWidgetItem(self.tree_widget, [""])

        xx = self.addCustomWidget(root_item, "")
        cc = self.addCustomWidget(xx, "")
        self.addCustomWidget(xx, "")
        self.addCustomWidget(xx, "")
        self.addCustomWidget(xx, "")
        self.addCustomWidget(cc, "")
        self.addCustomWidget(cc, "")
        self.addCustomWidget(cc, "")
        self.addCustomWidget(root_item, "")

        self.tree_widget.expandAll()

    def addCustomWidget(self, parent_item, name):
        child_item = QtWidgets.QTreeWidgetItem(parent_item, [name])

        # Create a custom widget container for column 0
        custom_widget_container = TaskEntityWDG()
        self.tree_widget.setItemWidget(child_item, 0, custom_widget_container)
        print(child_item)
        return child_item


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = TreeWidgetExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
