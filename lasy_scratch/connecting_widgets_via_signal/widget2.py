import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide2.QtCore import Slot

class Widget2(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("No document selected", self)
        self.layout.addWidget(self.label)

    @Slot(int)
    def on_document_selected(self, document_id):
        # Simulate loading data based on the document ID
        data = {1: {"Attribute1": "Value1", "Attribute2": "Value2"}}

        if document_id in data:
            selected_data = data[document_id]
            self.label.setText(f"Document {document_id} attributes:")
            for attribute, value in selected_data.items():
                self.layout.addWidget(QLabel(f"{attribute}: {value}", self))
        else:
            self.label.setText("Invalid document ID")

def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    central_widget = Widget2()
    window.setCentralWidget(central_widget)
    window.setWindowTitle("Widget2")
    window.setGeometry(500, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
