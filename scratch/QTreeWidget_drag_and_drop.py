import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PySide2.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setGeometry(100, 100, 300, 300)

        # Enable drag-and-drop for the QTreeWidget
        self.tree_widget.setDragEnabled(True)
        self.tree_widget.setDragDropMode(QTreeWidget.InternalMove)

        # Create some sample items
        item1 = QTreeWidgetItem(self.tree_widget, ["Item 1"])
        item2 = QTreeWidgetItem(self.tree_widget, ["Item 2"])
        item3 = QTreeWidgetItem(self.tree_widget, ["Item 3"])
        item4 = QTreeWidgetItem(self.tree_widget, ["Item 4"])

        # Allow items to be dropped onto other items (for parenting)
        self.tree_widget.setDefaultDropAction(Qt.MoveAction)

        # Connect the itemPressed signal to a slot
        self.tree_widget.itemPressed.connect(self.handle_item_pressed)

    def handle_item_pressed(self, item, column):
        # This slot will be called when an item is moved.
        print(f"Item pressed: {item.text(0)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
