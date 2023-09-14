import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QAction, QVBoxLayout, QWidget, QPushButton, QFileDialog, QInputDialog, QLineEdit
from PySide2.QtGui import QFont, QTextCursor, QTextCharFormat, QTextBlockFormat, QTextDocument
from PySide2.QtCore import Qt, QRegExp
import re

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor Example")
        self.setGeometry(100, 100, 800, 600)

        # Create the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout for the central widget
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QPlainTextEdit widget
        self.text_edit = QPlainTextEdit(self)
        layout.addWidget(self.text_edit)

        # Set a monospaced font for code-like text
        font = QFont("Courier New", 12)
        self.text_edit.setFont(font)

        # Create actions for the toolbar
        self.create_actions()
        self.create_toolbar()

        # Initialize some example text
        self.text_edit.setPlainText("Hello, World!\nThis is a QPlainTextEdit.")

    def create_actions(self):
        # Create actions for the toolbar
        self.cut_action = QAction("Cut", self)
        self.copy_action = QAction("Copy", self)
        self.paste_action = QAction("Paste", self)
        self.undo_action = QAction("Undo", self)
        self.redo_action = QAction("Redo", self)
        self.clear_action = QAction("Clear", self)
        self.search_action = QAction("Search", self)
        self.replace_action = QAction("Replace", self)

        # Connect actions to functions
        self.cut_action.triggered.connect(self.text_edit.cut)
        self.copy_action.triggered.connect(self.text_edit.copy)
        self.paste_action.triggered.connect(self.text_edit.paste)
        self.undo_action.triggered.connect(self.text_edit.undo)
        self.redo_action.triggered.connect(self.text_edit.redo)
        self.clear_action.triggered.connect(self.text_edit.clear)
        self.search_action.triggered.connect(self.search_text)
        self.replace_action.triggered.connect(self.replace_text)

    def create_toolbar(self):
        # Create a toolbar for the actions
        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(self.cut_action)
        toolbar.addAction(self.copy_action)
        toolbar.addAction(self.paste_action)
        toolbar.addSeparator()
        toolbar.addAction(self.undo_action)
        toolbar.addAction(self.redo_action)
        toolbar.addSeparator()
        toolbar.addAction(self.clear_action)
        toolbar.addSeparator()
        toolbar.addAction(self.search_action)
        toolbar.addAction(self.replace_action)

    def search_text(self):
        # Search for text and highlight matches
        search_text, ok = QInputDialog.getText(self, "Search Text", "Enter text to search:")
        if ok and search_text:
            cursor = self.text_edit.textCursor()
            cursor.movePosition(QTextCursor.Start)

            format = QTextCharFormat()
            format.setBackground(Qt.yellow)
            regex = QRegExp(search_text)
            regex.setCaseSensitivity(Qt.CaseInsensitive)

            while cursor.find(regex):
                cursor.mergeCharFormat(format)

    def replace_text(self):
        # Replace text matching a pattern
        search_text, ok = QInputDialog.getText(self, "Search Text", "Enter text to search:")
        if ok and search_text:
            replace_text, ok = QInputDialog.getText(self, "Replace Text", "Enter text to replace:")
            if ok:
                cursor = self.text_edit.textCursor()
                cursor.movePosition(QTextCursor.Start)

                regex = QRegExp(search_text)
                regex.setCaseSensitivity(Qt.CaseInsensitive)

                while cursor.find(regex):
                    cursor.insertText(replace_text)

def main():
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
