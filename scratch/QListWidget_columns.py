import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QLabel, QVBoxLayout, QWidget

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QListWidget with Hidden Data")
        self.setGeometry(100, 100, 400, 300)

        listWidget = QListWidget(self)

        # Add Items with Hidden Data
        item1 = QListWidgetItem()
        item1.setText("Column 1\tColumn 2\tColumn 3")
        item1.setData(1, "Some hidden data for item 1")  # Store hidden data with a key of 1
        listWidget.addItem(item1)

        item2 = QListWidgetItem()
        item2.setText("Another row\tWith hidden data")
        item2.setData(1, "Hidden data for item 2")  # Store hidden data with a key of 1
        listWidget.addItem(item2)

        # Accessing Hidden Data
        hidden_data_item1 = listWidget.item(0).data(1)  # Retrieve hidden data for item 1
        hidden_data_item2 = listWidget.item(1).data(1)  # Retrieve hidden data for item 2

        print("Hidden Data for Item 1:", hidden_data_item1)
        print("Hidden Data for Item 2:", hidden_data_item2)

        self.setCentralWidget(listWidget)

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
