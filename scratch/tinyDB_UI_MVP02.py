from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextBrowser

class TitleDisplayWidget(QWidget):
    title_selected = Signal(str)  # Define a signal to emit the selected title

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Titles:")
        self.layout.addWidget(self.label)

        self.title_list = ["Title 1", "Title 2", "Title 3"]

        for title in self.title_list:
            title_label = QLabel(title)
            title_label.mousePressEvent = lambda e, title=title: self.on_title_clicked(title)
            self.layout.addWidget(title_label)

    def on_title_clicked(self, title):
        self.title_selected.emit(title)  # Emit the selected title

class TextViewerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.text_browser = QTextBrowser()
        self.layout.addWidget(self.text_browser)

    def update_text(self, text):
        self.text_browser.setPlainText(text)  # Update the text viewer with the selected text

class MainPresenter(QObject):
    def __init__(self, title_display_widget, text_viewer_widget):
        super().__init__()

        self.title_display_widget = title_display_widget
        self.text_viewer_widget = text_viewer_widget

        self.title_display_widget.title_selected.connect(self.on_title_selected)

    def on_title_selected(self, title):
        # Retrieve and set the text corresponding to the selected title
        text = get_text_from_database(title)  # Replace with your data retrieval logic
        self.text_viewer_widget.update_text(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget Communication Example")
        self.setGeometry(100, 100, 600, 400)

        title_display_widget = TitleDisplayWidget()
        text_viewer_widget = TextViewerWidget()

        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(title_display_widget)
        central_layout.addWidget(text_viewer_widget)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        main_presenter = MainPresenter(title_display_widget, text_viewer_widget)

def get_text_from_database(title):
    # Simulated databases query to retrieve text based on the selected title
    # Replace with your databases logic
    return f"Text for {title}"

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
