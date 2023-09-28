from PySide2 import QtWidgets, QtCore

class TasksSnoozeWDG(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TasksSnoozeWDG, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.snooze_lb = QtWidgets.QLabel("SNOOZE IT!")

        self.snooze_one_bth = QtWidgets.QPushButton("1 day")
        self.snooze_three_bth = QtWidgets.QPushButton("3 days")
        self.snooze_five_bth = QtWidgets.QPushButton("5 days")

        self.custom_snooze_spb = QtWidgets.QSpinBox()
        self.custom_snooze_spb.setMinimum(1)
        self.custom_snooze_spb.setMaximum(9999)
        self.custom_snooze_spb.setValue(1)
        self.custom_snooze_spb.setFixedHeight(30)

        self.commmit_btn = QtWidgets.QPushButton("OK!")
        self.commmit_btn.setFixedHeight(30)

    def create_layout(self):
        customs_snooze_layout = QtWidgets.QHBoxLayout()
        customs_snooze_layout.addWidget(self.custom_snooze_spb)
        customs_snooze_layout.addWidget(self.commmit_btn)

        presets_layout = QtWidgets.QHBoxLayout()
        presets_layout.addWidget(self.snooze_lb)
        presets_layout.addWidget(self.snooze_one_bth)
        presets_layout.addWidget(self.snooze_three_bth)
        presets_layout.addWidget(self.snooze_five_bth)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(presets_layout)
        main_layout.addLayout(customs_snooze_layout)

    def create_connections(self):
        pass










if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TasksSnoozeWDG()


    test_dialog.show()
    sys.exit(app.exec_())