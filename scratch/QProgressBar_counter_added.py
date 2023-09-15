import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication, QMainWindow, QTableView, QStyledItemDelegate, QProgressBar

class NumberDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        value = index.data(Qt.DisplayRole)
        progressBar = QProgressBar()
        progressBar.setRange(0, 100)
        progressBar.setValue(value)

        # Paint the progress bar
        progressBar.paint(painter, option.rect, Qt.AlignCenter)

        # Paint the value text on top of the progress bar
        text_rect = option.rect.adjusted(0, 0, 0, -20)  # Adjust the rect for the text
        painter.drawText(text_rect, Qt.AlignCenter, str(value))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 400, 300)

        # Create a table view
        self.tableView = QTableView(self)
        self.setCentralWidget(self.tableView)

        # Create a model with a single column
        model = QStandardItemModel()
        model.setColumnCount(1)

        # Add data to the model
        for i in range(10):
            item = QStandardItem()
            item.setData(i * 10, Qt.DisplayRole)  # Set the progress value
            model.appendRow(item)

        self.tableView.setModel(model)
        self.tableView.setItemDelegate(NumberDelegate())  # Set the custom delegate

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
