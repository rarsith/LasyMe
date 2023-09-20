from PySide2 import QtWidgets, QtWebEngineWidgets, QtCore

html_path = '/lasy_scratch\\interactive_gantt_chart.html'

class TaskStatisticsBuild(QtWidgets.QWidget):
    def __init__(self, html_file, parent=None):
        super(TaskStatisticsBuild, self).__init__(parent)

        self.html_file = html_file

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.web_reader_wev = QtWebEngineWidgets.QWebEngineView()
        self.web_reader_wev.setUrl(QtCore.QUrl.fromLocalFile(self.html_file))

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.web_reader_wev)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskStatisticsBuild(html_path)
    test_dialog.show()
    sys.exit(app.exec_())