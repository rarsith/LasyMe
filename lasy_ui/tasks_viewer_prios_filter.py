from PySide2 import QtWidgets, QtCore
from lasy_ops.tdb_priorities import Priorities

class TasksPrioFilterButtonWDG(QtWidgets.QPushButton):
    def __init__(self, name, parent=None):
        super(TasksPrioFilterButtonWDG, self).__init__(parent)

        self.button_name = name
        self.set_button_name()

    def set_button_name(self):
        self.setText(self.button_name)


class TasksPrioFilterBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TasksPrioFilterBuild, self).__init__(parent)

        self.create_layout()

    def create_layout(self):
        self.prio_buttons_layout = QtWidgets.QVBoxLayout()

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.prio_buttons_layout)
        self.main_layout.setContentsMargins(0,0,0,0)

class TasksPrioFilterCore(TasksPrioFilterBuild):
    filter_prio_info = QtCore.Signal(dict)
    filter_status_info = QtCore.Signal(dict)

    def __init__(self, parent=None):
        super(TasksPrioFilterCore, self).__init__(parent)

        self.update_filters()

    def update_prio_filters(self):
        self.clear_layout(self.prio_buttons_layout)
        get_prio_filters = Priorities().all_priorities

        for prio_filter in get_prio_filters:
            self.prio_button = TasksPrioFilterButtonWDG(name=prio_filter)
            self.prio_button.clicked.connect(self.transmit_prio)
            self.prio_button.setCheckable(True)
            self.prio_buttons_layout.addWidget(self.prio_button)

        spacer = QtWidgets.QSpacerItem(30, 30)
        self.main_layout.addItem(spacer)

        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.refresh_btn)
        self.setLayout(self.main_layout)

    def update_filters(self):
        self.clear_layout(self.main_layout)
        get_prio_filters = Priorities().all_priorities

        for prio_filter in get_prio_filters:
            self.button = TasksPrioFilterButtonWDG(name=prio_filter)
            self.button.clicked.connect(self.transmit_prio)
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

    def transmit_prio(self):
        get_active_tags = self.get_active_buttons()
        self.filter_prio_info.emit({"prios": get_active_tags})

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
    test_dialog = TasksPrioFilterCore()
    test_dialog.show()
    sys.exit(app.exec_())