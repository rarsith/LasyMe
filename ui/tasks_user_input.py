from PySide2 import QtWidgets, QtCore
from operations.tdb_priorities import Priorities
from operations.schemas.task_schema import TaskSchema
from operations.tdb_attributes_definitions import TaskAttributesDefinitions
from operations.tiny_ops.tasks_ops import TinyOps
from ui.custom_widgets.task_text_widget import CustomPlainTextEditWDG


class InputTaskBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InputTaskBuild, self).__init__(parent)

        self.setMaximumHeight(170)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.task_input_ptx = CustomPlainTextEditWDG()
        self.task_input_ptx.setPlaceholderText("Start Typing...First Line is considered the Task Title")

        self.end_date = QtWidgets.QDateEdit(calendarPopup=True)
        self.end_date.setDateTime(QtCore.QDateTime.currentDateTime())

        self.thirty_min_btn = QtWidgets.QPushButton("30")
        self.sixty_min_btn = QtWidgets.QPushButton("60")
        self.ninety_min_btn = QtWidgets.QPushButton("90")

        self.low_prio_btn = QtWidgets.QPushButton(Priorities().low)

        self.normal_prio_btn = QtWidgets.QPushButton(Priorities().normal)
        self.med_prio_btn = QtWidgets.QPushButton(Priorities().medium)
        self.high_prio_btn = QtWidgets.QPushButton(Priorities().high)
        self.critical_prio_btn = QtWidgets.QPushButton(Priorities().critical)

        self.set_parent_btn = QtWidgets.QPushButton("Set Parent...")

        self.create_task_btn = QtWidgets.QPushButton("Create")

    def create_layout(self):
        calendar_layout = QtWidgets.QFormLayout()
        calendar_layout.addRow("End Date", self.end_date)

        execution_buttons_layout = QtWidgets.QHBoxLayout()
        execution_buttons_layout.addWidget(self.thirty_min_btn)
        execution_buttons_layout.addWidget(self.sixty_min_btn)
        execution_buttons_layout.addWidget(self.ninety_min_btn)

        prio_buttons_layout = QtWidgets.QGridLayout()
        prio_buttons_layout.addWidget(self.normal_prio_btn, 0, 0)
        prio_buttons_layout.addWidget(self.med_prio_btn, 0, 1)
        prio_buttons_layout.addWidget(self.low_prio_btn, 0, 2)
        prio_buttons_layout.addWidget(self.high_prio_btn, 1, 0)
        prio_buttons_layout.addWidget(self.critical_prio_btn, 1, 1, 1, 2) # (widget, row, column, rowSpan, colSpan)
        prio_buttons_layout.addWidget(self.set_parent_btn, 2, 0, 1, 3) # (widget, row, column, rowSpan, colSpan)

        buttons_layout = QtWidgets.QVBoxLayout()
        buttons_layout.addLayout(calendar_layout)
        buttons_layout.addLayout(execution_buttons_layout)
        buttons_layout.addStretch(1)
        buttons_layout.addLayout(prio_buttons_layout)

        task_input_layout = QtWidgets.QHBoxLayout()
        task_input_layout.addWidget(self.task_input_ptx)
        task_input_layout.addLayout(buttons_layout)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(task_input_layout)
        main_layout.addWidget(self.create_task_btn)


class InputTaskBuildCore(InputTaskBuild):
    def __init__(self, parent=None):
        super(InputTaskBuildCore, self).__init__(parent)

        self.tops = TinyOps()
        self.create_connections()

        self.tasks_key_definitions = TaskAttributesDefinitions()
        self.task_schema = TaskSchema(self.tasks_key_definitions)


    def create_connections(self):
        self.create_task_btn.clicked.connect(self.create_task_document)
        self.thirty_min_btn.clicked.connect(self.set_time_thirty)
        self.sixty_min_btn.clicked.connect(self.set_time_sixty)
        self.ninety_min_btn.clicked.connect(self.set_time_ninety)

        self.low_prio_btn.clicked.connect(self.set_to_low_prio)
        self.med_prio_btn.clicked.connect(self.set_to_med_prio)
        self.high_prio_btn.clicked.connect(self.set_to_high_prio)
        self.critical_prio_btn.clicked.connect(self.set_to_critical_prio)

        self.set_parent_btn.clicked.connect(self.set_parent)

    def create_task_document(self):
        self.set_task_title()
        self.set_task_details()
        self.get_sel_task_end_date()
        complete_doc = self.task_schema.to_dict()
        has_content = self.task_input_ptx.toPlainText()
        if not has_content.strip():
            print("No task details found. Please insert text")
            return

        self.tops.insert_task(document=complete_doc)
        self.task_input_ptx.clear()

    def set_time_thirty(self):
        duration_value = "30"
        self.task_schema.hours_executable = duration_value
        return duration_value

    def set_time_sixty(self):
        duration_value = "60"
        self.task_schema.hours_executable = duration_value
        return duration_value

    def set_time_ninety(self):
        duration_value = "90"
        self.task_schema.hours_executable = duration_value
        return duration_value

    def set_to_normal_prio(self):
        prio_value = Priorities().normal
        self.task_schema.task_priority = prio_value
        return prio_value

    def set_to_low_prio(self):
        prio_value = Priorities().low
        self.task_schema.task_priority = prio_value
        return prio_value

    def set_to_med_prio(self):
        prio_value = Priorities().medium
        self.task_schema.task_priority = prio_value
        return prio_value

    def set_to_high_prio(self):
        prio_value = Priorities().high
        self.task_schema.task_priority = prio_value
        return prio_value

    def set_to_critical_prio(self):
        prio_value = Priorities().critical
        self.task_schema.task_priority = prio_value
        return prio_value

    def set_parent(self):
        self.task_schema.parent_task = "root"

    def set_task_title(self):
        collected_title = self.task_input_ptx.get_title()
        self.task_schema.task_title = collected_title

    def set_task_details(self):
        collected_details = self.task_input_ptx.get_task_details()
        self.task_schema.task_details_text = collected_details

    def get_sel_task_end_date(self):
        end_date_raw = self.end_date.date()
        end_sel_date = end_date_raw.toString("yyyy-MM-dd")
        # print(end_sel_date)
        self.task_schema.end_interval = end_sel_date
        return end_sel_date

    def get_title(self):
        text_content = self.task_input_ptx.toPlainText()
        get_lines = text_content.split('\n')
        if len(get_lines[0]) != 0:
            first_line = get_lines[0]
            return first_line
        return "-- Title Needed --"


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = InputTaskBuildCore()
    # test_dialog.get_live_title()
    test_dialog.show()
    sys.exit(app.exec_())