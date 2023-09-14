import sys
from PySide2.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtCore import Signal

class Widget1(QTreeWidget):
    documentSelected = Signal(int)

    def __init__(self, documents):
        super().__init__()
        self.setHeaderLabels(["Document ID", "Document Name"])
        self.itemClicked.connect(self.on_item_clicked)

        for document_id, document_name in documents.items():
            item = QTreeWidgetItem([str(document_id), document_name])
            self.addTopLevelItem(item)

    def on_item_clicked(self, item, column):
        document_id = int(item.text(0))
        self.documentSelected.emit(document_id)

def main():
    documents = {
        1: "Document 1",
        2: "Document 2",
        3: "Document 3"
    }

    app = QApplication(sys.argv)
    window = QMainWindow()
    central_widget = QWidget(window)
    layout = QVBoxLayout(central_widget)

    widget1 = Widget1(documents)
    layout.addWidget(widget1)

    window.setCentralWidget(central_widget)
    window.setWindowTitle("Widget1")
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
