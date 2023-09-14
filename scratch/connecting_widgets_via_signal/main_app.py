import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from widget1 import Widget1
from widget2 import Widget2

documents = {
        1: "Document 1",
        2: "Document 2",
        3: "Document 3"
    }
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application")
        self.setGeometry(100, 100, 800, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        widget1 = Widget1(documents=documents)
        widget2 = Widget2()

        widget1.documentSelected.connect(widget2.on_document_selected)

        layout.addWidget(widget1)
        layout.addWidget(widget2)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
