import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap

class CustomTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setColumnCount(3)
        self.setHeaderLabels(["Column 1", "Column 2", "Column 3"])

    def dropEvent(self, event):
        destination_item = self.itemAt(event.pos())
        source_item = self.currentItem()

        if destination_item and source_item:
            if destination_item != source_item:
                for col in range(self.columnCount()):
                    source_widget_item = source_item.child(0, col)
                    destination_widget_item = destination_item.child(0, col)

                    if source_widget_item:
                        destination_item.insertChild(0, source_widget_item.clone())
                        del source_item

                    if destination_widget_item:
                        source_item.insertChild(0, destination_widget_item.clone())
                        del destination_item

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drag and Drop Items")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.tree_widget = CustomTreeWidget()

        # Create sample widgets for columns
        widget_1 = QLabel("Widget 1")
        widget_2 = QPushButton("Widget 2")
        widget_3 = QLabel()
        pixmap = QPixmap(50, 50)
        pixmap.fill(Qt.red)
        widget_3.setPixmap(pixmap)

        # Create items with widgets
        for i in range(3):
            item = QTreeWidgetItem(self.tree_widget)
            item.setText(0, f"Item {i}")
            item.setText(1, f"Item {i}")
            item.setText(2, f"Item {i}")

            item.setFlags(item.flags() | Qt.ItemIsDragEnabled)

            self.tree_widget.setItemWidget(item, 0, widget_1)
            self.tree_widget.setItemWidget(item, 1, widget_2)
            self.tree_widget.setItemWidget(item, 2, widget_3)

        self.layout.addWidget(self.tree_widget)

def main():
    app = QApplication(sys.argv)
    main_widget = MainWidget()
    main_widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
