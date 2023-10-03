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

    def get_selected_lines(self):
        delimiter = ""
        cursor = self.textCursor()
        selected_text = cursor.selectedText()
        selected_paragraph = selected_text.split('\u2029')

        return selected_paragraph

    def remove_selected_text(self, text_as_replacement=None, replace=False):
        cursor = self.textCursor()
        if cursor.hasSelection():
            if not replace:
                cursor.removeSelectedText()
            else:
                if text_as_replacement:
                    cursor.insertText(text_as_replacement)
