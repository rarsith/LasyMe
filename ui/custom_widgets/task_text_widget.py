from PySide2 import QtWidgets


class CustomPlainTextEditWDG(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        super(CustomPlainTextEditWDG, self).__init__(parent)

        self.create_connections()

    def create_connections(self):
        self.textChanged.connect(self.get_title)

    def get_title(self):
        text_content = self.toPlainText()
        get_lines = text_content.split('\n')
        if len(get_lines[0]) != 0:
            first_line = get_lines[0]
            print(first_line)
            return first_line
        return "-- Title Needed --"

    def get_task_details(self):
        text_content = self.toPlainText()
        get_lines = text_content.split('\n')
        details_line = get_lines[1:]
        return details_line

    def add_task_text(self, text_to_import):
        self.clear()
        self.setPlainText(text_to_import)

