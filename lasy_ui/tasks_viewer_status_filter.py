from PySide2 import QtWidgets, QtCore
from lasy_ops.tdb_statuses import Statuses


class TasksStatusFilterButtonWDG(QtWidgets.QPushButton):
    def __init__(self, name, parent=None):
        super(TasksStatusFilterButtonWDG, self).__init__(parent)

        self.button_name = name
        self.set_button_name()

    def set_button_name(self):
        self.setText(self.button_name)


class TasksStatusFilterBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TasksStatusFilterBuild, self).__init__(parent)

        self.create_layout()

    def create_layout(self):
        self.status_buttons_layout = QtWidgets.QVBoxLayout()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.status_buttons_layout)
        self.main_layout.setContentsMargins(0,0,0,0)


class TasksStatusFilterCore(TasksStatusFilterBuild):
    filter_status_info = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(TasksStatusFilterCore, self).__init__(parent)

        self.update_filters()

    def update_filters(self):
        self.clear_layout(self.main_layout)
        get_status_filters = Statuses().all_statuses

        for status_filter in get_status_filters:
            self.button = TasksStatusFilterButtonWDG(name=status_filter)
            self.button.clicked.connect(self.transmit_status)
            self.button.setCheckable(True)
            self.main_layout.addWidget(self.button)

        self.main_layout.addStretch(1)
        self.setLayout(self.main_layout)

    def clear_layout(self, layout_wdg):
        while layout_wdg.count():
            item = layout_wdg.takeAt(0)
            widget = item.widget()
            if widget and widget != self.refresh_btn:
                widget.deleteLater()

    def transmit_status(self):
        get_active_tags = self.get_active_buttons()
        self.filter_status_info.emit({"statuses": get_active_tags})

    def get_active_buttons(self):
        active_buttons = []
        for index in range(self.main_layout.count()):
            widget = self.main_layout.itemAt(index).widget()
            if isinstance(widget, QtWidgets.QPushButton) and widget.isChecked():
                active_buttons.append(widget.text())
        return active_buttons


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TasksStatusFilterCore()
    test_dialog.show()
    sys.exit(app.exec_())