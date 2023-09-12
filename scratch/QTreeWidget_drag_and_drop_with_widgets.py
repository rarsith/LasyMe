import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QWidget, QVBoxLayout, QPushButton
from PySide2.QtCore import Qt, QMimeData
from PySide2.QtGui import QDrag, QPixmap

class CustomTreeWidget(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def startDrag(self, supportedActions):
        item = self.currentItem()
        if item:
            drag = QDrag(self)
            mime_data = QMimeData()
            mime_data.setText(item.text(0))  # You can set the data you want to transfer here
            drag.setMimeData(mime_data)

            # Create a pixmap of the item to display during drag
            pixmap = QPixmap(item.sizeHint(0))
            item.render(pixmap)

            drag.setPixmap(pixmap)
            drag.setHotSpot(pixmap.rect().center())
            drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            item_text = event.mimeData().text()
            new_item = QTreeWidgetItem([item_text])

            # Customize the new item's properties if needed
            # For example, you can set widgets in each column here

            self.addTopLevelItem(new_item)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drag and Drop Example")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        self.tree_widget1 = CustomTreeWidget()
        self.tree_widget2 = CustomTreeWidget()

        layout.addWidget(self.tree_widget1)
        layout.addWidget(self.tree_widget2)

        button = QPushButton("Add Item")
        button.clicked.connect(self.add_item)

        layout.addWidget(button)

        self.setCentralWidget(central_widget)

    def add_item(self):
        item_text = "New Item"
        new_item = QTreeWidgetItem([item_text])
        # Customize the new item's properties and widgets per column if needed

        self.tree_widget1.addTopLevelItem(new_item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
