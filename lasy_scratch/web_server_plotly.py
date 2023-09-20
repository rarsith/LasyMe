import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl

class GanttChartApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gantt Chart in PySide2')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QWebEngineView widget
        webview = QWebEngineView(self)

        # Load the HTML chart file using the full file path
        webview.setUrl(QUrl.fromLocalFile('C:\\Users\\arsithra\\PycharmProjects\\LasyMe\\lasy_scratch\\interactive_gantt_chart.html'))  # Replace with the actual file path

        layout.addWidget(webview)

def main():
    app = QApplication(sys.argv)
    main_window = GanttChartApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
