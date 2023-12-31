from PySide2 import QtWidgets, QtCore
from lasy_ops.tdb_priorities import Priorities
from lasy_ops.schemas.task_schema import TaskSchema
from lasy_ops.tdb_attributes_definitions import TaskAttributesDefinitions
from lasy_ui.custom_widgets.task_tags_widget import TasksViewerTagAssignerCore
from lasy_ops.tiny_ops.tasks_ops import TasksOps
from lasy_ui.custom_widgets.task_text_widget import CustomPlainTextEditWDG
from lasy_common_utils.date_time_utils import DateTime
from lasy_ui.custom_widgets.custom_fonts_widget import define_font
import getpass


class InputTaskBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(InputTaskBuild, self).__init__(parent)

        self.setMaximumHeight(300)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        ubuntu_font = define_font()
        self.task_input_ptx = CustomPlainTextEditWDG()
        self.task_input_ptx.setPlaceholderText("Start Typing...First Line is considered the Task Title")
        self.task_input_ptx.setFont(ubuntu_font)

        self.end_date = QtWidgets.QDateEdit(calendarPopup=True)
        self.end_date.setDateTime(QtCore.QDateTime.currentDateTime())

        button_minimum_height = 30

        self.low_prio_btn = QtWidgets.QPushButton(Priorities().low)
        self.low_prio_btn.setMinimumHeight(button_minimum_height)

        self.normal_prio_btn = QtWidgets.QPushButton(Priorities().normal)
        self.normal_prio_btn.setMinimumHeight(button_minimum_height)

        self.med_prio_btn = QtWidgets.QPushButton(Priorities().medium)
        self.med_prio_btn.setMinimumHeight(button_minimum_height)

        self.high_prio_btn = QtWidgets.QPushButton(Priorities().high)
        self.high_prio_btn.setMinimumHeight(button_minimum_height)

        self.critical_prio_btn = QtWidgets.QPushButton(Priorities().critical)
        self.critical_prio_btn.setMinimumHeight(button_minimum_height)

        self.set_parent_btn = QtWidgets.QPushButton("Set Parent...")
        self.set_parent_btn.setMinimumHeight(button_minimum_height)

        self.create_task_btn = QtWidgets.QPushButton("Create")
        self.create_task_btn.setMinimumHeight(30)

        self.set_tags_wdg = TasksViewerTagAssignerCore()

    def create_layout(self):
        calendar_layout = QtWidgets.QFormLayout()
        calendar_layout.addRow("End Date", self.end_date)

        prio_buttons_layout = QtWidgets.QGridLayout()
        prio_buttons_layout.addWidget(self.critical_prio_btn, 0, 0) # (widget, row, column, rowSpan, colSpan)
        prio_buttons_layout.addWidget(self.high_prio_btn, 1, 0)
        prio_buttons_layout.addWidget(self.med_prio_btn, 2, 0)
        prio_buttons_layout.addWidget(self.normal_prio_btn, 3, 0)
        prio_buttons_layout.addWidget(self.low_prio_btn, 4, 0)

        # prio_buttons_layout.addWidget(self.critical_prio_btn, 1, 1, 1, 2) # (widget, row, column, rowSpan, colSpan)
        # prio_buttons_layout.addWidget(self.set_parent_btn, 2, 0, 1, 3) # (widget, row, column, rowSpan, colSpan)

        buttons_layout = QtWidgets.QVBoxLayout()
        buttons_layout.addLayout(calendar_layout)
        buttons_layout.addLayout(prio_buttons_layout)

        task_input_layout = QtWidgets.QHBoxLayout()
        task_input_layout.addWidget(self.task_input_ptx)
        task_input_layout.addLayout(buttons_layout)
        task_input_layout.addWidget(self.set_tags_wdg)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(task_input_layout)
        main_layout.addWidget(self.create_task_btn)


class InputTaskBuildCore(InputTaskBuild):
    def __init__(self, parent=None):
        super(InputTaskBuildCore, self).__init__(parent)

        self.tops = TasksOps()
        self.create_connections()

        self.tasks_key_definitions = TaskAttributesDefinitions()
        self.task_schema = TaskSchema(self.tasks_key_definitions)

    def create_connections(self):
        self.create_task_btn.clicked.connect(self.create_task_document)

        self.low_prio_btn.clicked.connect(self.set_to_low_prio)
        self.med_prio_btn.clicked.connect(self.set_to_med_prio)
        self.high_prio_btn.clicked.connect(self.set_to_high_prio)
        self.critical_prio_btn.clicked.connect(self.set_to_critical_prio)

    def create_task_document(self):
        self.set_task_title()
        self.set_task_details()
        self.get_sel_task_end_date()
        self.get_tags()
        self.task_schema.created_by_user = getpass.getuser()
        self.task_schema.datetime_created_at = DateTime().date_and_time
        self.task_schema.date_created_at = DateTime().curr_date
        self.task_schema.time_created_at = DateTime().curr_time
        self.task_schema.start_interval = DateTime().curr_date
        complete_doc = self.task_schema.to_dict()
        has_content = self.task_input_ptx.toPlainText()
        if not has_content.strip():
            print("No task details found. Please insert text")
            return

        self.tops.insert_task(document=complete_doc)
        self.task_input_ptx.clear()
        self.end_date.setDateTime(QtCore.QDateTime.currentDateTime())

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
        self.task_schema.end_interval = end_sel_date
        return end_sel_date

    def get_title(self):
        text_content = self.task_input_ptx.toPlainText()
        get_lines = text_content.split('\n')
        if len(get_lines[0]) != 0:
            first_line = get_lines[0]
            return first_line
        return "-- Title Needed --"

    def get_tags(self):
        active_buttons = self.set_tags_wdg.get_active_buttons()
        print(active_buttons)
        self.task_schema.task_tag = active_buttons
        self.set_tags_wdg.reset_uncheck_all_buttons()


if __name__ == "__main__":
    import sys
    import os

    # os.environ["LASY_DATA_ROOT"] = 'D:\\My_Apps_Repo\\database_testing_sandbox'

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = InputTaskBuildCore()
    test_dialog.show()
    sys.exit(app.exec_())