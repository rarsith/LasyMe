from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Slot
import getpass
from lasy_ui.custom_widgets.task_text_widget import CustomPlainTextEditWDG
from lasy_ops.tdb_attributes_definitions import TaskAttributesDefinitions
from lasy_ops.tdb_attributes_paths import TasksAttributesPaths
from lasy_ops.tiny_ops.tasks_ops import TinyOps
from lasy_ui.custom_widgets.task_tags_widget import TasksViewerTagAssignerCore #TaskTagsWDG
from lasy_ui.custom_widgets.custom_fonts_widget import define_font
from lasy_ui.custom_widgets.separator_widget import SeparatorWDG
from lasy_ui.custom_widgets.tasks_snooze_widget import TasksSnoozeWDG
from lasy_ops.schemas.task_schema import TaskSchema
from lasy_common_utils.date_time_utils import DateTime



class TaskPropertiesEditorBuild(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TaskPropertiesEditorBuild, self).__init__(parent)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        ubuntu_font = define_font()
        self.record_current_sel_task = QtWidgets.QLineEdit()
        self.record_current_sel_task.setDisabled(True)

        self.text_viewer_ptx = CustomPlainTextEditWDG()
        self.text_viewer_ptx.setMinimumHeight(300)
        # self.text_viewer_ptx.setMaximumHeight(450)
        self.text_viewer_ptx.setFont(ubuntu_font)

        self.update_task_text_btn = QtWidgets.QPushButton("Update Task Briefing")
        self.update_task_text_btn.setMinimumHeight(40)

        self.create_tasks_from_selection_btn = QtWidgets.QPushButton("Selection To Tasks")
        self.create_tasks_from_selection_btn.setMinimumHeight(40)
        self.create_tasks_from_selection_btn.setMaximumWidth(100)


        self.created_by_le = QtWidgets.QLineEdit()
        self.created_by_le.setDisabled(True)

        self.assined_to_cb = QtWidgets.QComboBox()
        self.assined_to_cb.setObjectName("AssinedToCB")
        self.assined_to_cb.addItems(["--no DUDES--no DUDDESESS"])
        self.assined_to_cb.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)


        self.start_date_interval_dte = QtWidgets.QDateEdit(calendarPopup=True)
        self.start_date_interval_dte.setCalendarPopup(True)
        self.end_date_interval_dte = QtWidgets.QDateEdit(calendarPopup=True)
        self.end_date_interval_dte.setCalendarPopup(True)

        self.set_tags_wdg = TasksViewerTagAssignerCore()
        self.snooze_it_wdg = TasksSnoozeWDG()

        self.update_task_properties_btn = QtWidgets.QPushButton("Update Task Properties")
        self.update_task_properties_btn.setMinimumHeight(40)

        self.start_lb = QtWidgets.QLabel("Start")
        self.end_lb = QtWidgets.QLabel("End")

        self.created_by_lb = QtWidgets.QLabel("Created by")
        self.assigned_to_lb = QtWidgets.QLabel("Assigned to")
        self.tags_lb = QtWidgets.QLabel("Tags")

    def create_layout(self):
        separator01 = SeparatorWDG()
        separator02 = SeparatorWDG()

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.update_task_text_btn)
        buttons_layout.addWidget(self.create_tasks_from_selection_btn)

        win_layout = QtWidgets.QVBoxLayout()
        win_layout.addWidget(self.snooze_it_wdg)
        win_layout.addWidget(self.record_current_sel_task)
        win_layout.addWidget(self.text_viewer_ptx)
        win_layout.addLayout(buttons_layout)
        win_layout.setStretch(2,1)
        # win_layout.addStretch(1)


        start_date_layout = QtWidgets.QVBoxLayout()
        start_date_layout.addWidget(self.start_lb)
        start_date_layout.addWidget(self.start_date_interval_dte)

        end_date_layout = QtWidgets.QVBoxLayout()
        end_date_layout.addWidget(self.end_lb)
        end_date_layout.addWidget(self.end_date_interval_dte)

        dates_layout = QtWidgets.QHBoxLayout()
        dates_layout.addLayout(start_date_layout)
        dates_layout.addLayout(end_date_layout)

        owner_layout = QtWidgets.QHBoxLayout()
        owner_layout.addWidget(self.created_by_lb)
        owner_layout.addWidget(self.created_by_le)

        assigned_to_layout = QtWidgets.QHBoxLayout()
        assigned_to_layout.addWidget(self.assigned_to_lb)
        assigned_to_layout.addWidget(self.assined_to_cb)

        misc_layout = QtWidgets.QVBoxLayout()
        misc_layout.addLayout(owner_layout)
        misc_layout.addLayout(assigned_to_layout)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(win_layout)
        main_layout.addLayout(dates_layout)
        main_layout.addLayout(misc_layout)
        main_layout.addWidget(self.update_task_properties_btn)
        main_layout.addWidget(separator01)
        main_layout.addWidget(separator02)
        main_layout.addWidget(self.set_tags_wdg)

class TaskPropertiesEditorCore(TaskPropertiesEditorBuild):
    def __init__(self, parent=None):
        super(TaskPropertiesEditorCore, self).__init__(parent)

        self.doc_attrib = TaskAttributesDefinitions()
        self.tops = TinyOps()
        self.task_attr_paths = TasksAttributesPaths(self.doc_attrib)

        self.create_connections()

    def create_connections(self):
        self.update_task_text_btn.clicked.connect(self.update_task_briefing_text)
        self.create_tasks_from_selection_btn.clicked.connect(self.create_tasks_from_selection)
        self.update_task_properties_btn.clicked.connect(self.update_task_properties)
        self.snooze_it_wdg.snooze_one_bth.clicked.connect(self.snooze_task_one)
        self.snooze_it_wdg.snooze_three_bth.clicked.connect(self.snooze_task_three)
        self.snooze_it_wdg.snooze_five_bth.clicked.connect(self.snooze_task_five)
        self.snooze_it_wdg.commmit_btn.clicked.connect(self.add_custom_snooze)

    def create_tasks_from_selection(self):
        task_schema = TaskSchema(self.doc_attrib)

        selected_lines = self.text_viewer_ptx.get_selected_lines()
        get_current_id = self.record_current_sel_task.text()
        active_document = self.tops.get_doc_by_id(int(get_current_id))

        task_schema.task_title = "Split --> " + active_document["task_title"]
        task_schema.created_by_user = getpass.getuser()
        task_schema.datetime_created_at = DateTime().date_and_time
        task_schema.date_created_at = DateTime().curr_date
        task_schema.time_created_at = DateTime().curr_time
        task_schema.start_interval = active_document["start_date_interval"]
        task_schema.end_date_interval = active_document["end_date_interval"]
        task_schema.prio = active_document["prio"]
        task_schema.status = active_document["status"]
        task_schema.task_details = selected_lines  # find a way to insert more spaces from the title
        task_schema.task_tag = active_document["tags"]

        complete_doc = task_schema.to_dict()

        new_task_id = self.tops.insert_task(document=complete_doc)

        replacement = "Content became Task with id: {}".format(new_task_id)
        self.text_viewer_ptx.remove_selected_text(text_as_replacement=replacement, replace=True)
        self.update_task_briefing_text()

    def add_custom_snooze(self):
        get_current_id = self.record_current_sel_task.text()
        get_end_date_raw = self.end_date_interval_dte.date()
        get_custom_value = self.snooze_it_wdg.custom_snooze_spb.value()
        snoozed_date = get_end_date_raw.addDays(get_custom_value)
        get_end_date = snoozed_date.toString("yyyy-MM-dd")
        self.tops.update_task(int(get_current_id), self.task_attr_paths.end_interval(get_end_date))
        active_document = self.tops.get_doc_by_id(int(get_current_id))
        self.populate_all_widgets({"task_id_emit": get_current_id, "task_emit": active_document})

    def snooze_task_one(self):
        get_current_id = self.record_current_sel_task.text()
        get_end_date_raw = self.end_date_interval_dte.date()
        snoozed_date = get_end_date_raw.addDays(1)
        get_end_date = snoozed_date.toString("yyyy-MM-dd")
        self.tops.update_task(int(get_current_id), self.task_attr_paths.end_interval(get_end_date))
        active_document = self.tops.get_doc_by_id(int(get_current_id))
        self.populate_all_widgets({"task_id_emit":get_current_id,"task_emit":active_document})

    def snooze_task_three(self):
        get_current_id = self.record_current_sel_task.text()
        get_end_date_raw = self.end_date_interval_dte.date()
        snoozed_date = get_end_date_raw.addDays(3)
        get_end_date = snoozed_date.toString("yyyy-MM-dd")
        self.tops.update_task(int(get_current_id), self.task_attr_paths.end_interval(get_end_date))
        active_document = self.tops.get_doc_by_id(int(get_current_id))
        self.populate_all_widgets({"task_id_emit": get_current_id, "task_emit": active_document})

    def snooze_task_five(self):
        get_current_id = self.record_current_sel_task.text()
        get_end_date_raw = self.end_date_interval_dte.date()
        snoozed_date = get_end_date_raw.addDays(5)
        get_end_date = snoozed_date.toString("yyyy-MM-dd")
        self.tops.update_task(int(get_current_id), self.task_attr_paths.end_interval(get_end_date))
        active_document = self.tops.get_doc_by_id(int(get_current_id))
        self.populate_all_widgets({"task_id_emit": get_current_id, "task_emit": active_document})

    def update_dates(self):
        get_current_id = self.record_current_sel_task.text()
        get_start_date_raw = self.start_date_interval_dte.date()
        get_start_date = get_start_date_raw.toString("yyyy-MM-dd")
        get_end_date_raw = self.end_date_interval_dte.date()
        get_end_date = get_end_date_raw.toString("yyyy-MM-dd")
        self.tops.update_task(int(get_current_id), self.task_attr_paths.start_interval(get_start_date))
        self.tops.update_task(int(get_current_id), self.task_attr_paths.end_interval(get_end_date))

    def update_task_properties(self):
        get_current_id = self.record_current_sel_task.text()

        get_start_date_raw = self.start_date_interval_dte.date()
        get_start_date = get_start_date_raw.toString("yyyy-MM-dd")

        get_end_date_raw = self.end_date_interval_dte.date()
        get_end_date = get_end_date_raw.toString("yyyy-MM-dd")

        get_owner = self.created_by_le.text()

        self.tops.update_task(int(get_current_id), self.task_attr_paths.start_interval(get_start_date))
        self.tops.update_task(int(get_current_id), self.task_attr_paths.end_interval(get_end_date))
        self.tops.update_task(int(get_current_id), self.task_attr_paths.task_created_by(get_owner))

    @Slot(dict)
    def update_per_click_tags(self, current_tags_selection):
        get_emitted_tags = current_tags_selection["assigned_tags"]
        get_current_id = self.record_current_sel_task.text()
        self.tops.update_task(int(get_current_id), self.task_attr_paths.tags(get_emitted_tags))

    def update_task_briefing_text(self):
        get_current_title = self.text_viewer_ptx.get_title()
        get_current_text = self.text_viewer_ptx.get_task_details()
        get_current_id = self.record_current_sel_task.text()
        self.tops.update_task(int(get_current_id), self.task_attr_paths.task_details(get_current_text))
        self.tops.update_task(int(get_current_id), self.task_attr_paths.task_title(get_current_title))

    @Slot(dict)
    def populate_all_widgets(self, received_task_doc: dict):
        self.load_task_text(received_task_doc["task_emit"])
        self.load_dates(received_task_doc["task_emit"])
        self.load_user(received_task_doc["task_emit"])
        self.load_tags(received_task_doc["task_emit"])
        self.load_task_id(received_task_doc["task_id_emit"])

    def get_full_text_from_task_doc(self, task_doc: dict):
        get_title = task_doc[self.doc_attrib.title]
        get_text = task_doc[self.doc_attrib.task_details]
        if isinstance(get_text, list):
            rebuild_string = "\n".join([str(each) for each in get_text])
            including_title = "\n".join([get_title, rebuild_string])
            return including_title

    def load_task_text(self, task_doc):
        text = self.get_full_text_from_task_doc(task_doc=task_doc)
        self.text_viewer_ptx.clear()
        self.text_viewer_ptx.insertPlainText(text)

    def load_dates(self, task_doc: dict):
        start_date = task_doc[self.doc_attrib.start_date_interval]
        end_date = task_doc[self.doc_attrib.end_date_interval]
        start_date_wdg = QtCore.QDate.fromString(start_date, "yyyy-MM-dd")
        end_date_wdg = QtCore.QDate.fromString(end_date, "yyyy-MM-dd")
        self.start_date_interval_dte.setDate(start_date_wdg)
        self.end_date_interval_dte.setDate(end_date_wdg)

    def load_user(self, task_doc: dict):
        user = task_doc[self.doc_attrib.created_by]
        self.created_by_le.clear()
        self.created_by_le.setText(user)

    def load_tags(self, task_doc: dict):
        tags = task_doc[self.doc_attrib.tags]
        self.set_tags_wdg.activate_tags(tags)

    def load_task_id(self, task_id):
        self.record_current_sel_task.setText(task_id)


if __name__ == "__main__":
    import os
    import sys

    # os.environ["LASY_DATA_ROOT"] = 'D:\\My_Apps_Repo\\database_testing_sandbox'

    task_sample = {"task_title": "new Task Title",
                   "parent": "root",
                   "created_by": "arsithra",
                   "date_created": "2023-09-14",
                   "time_created": "08:23",
                   "assigned_to": "arsithra",
                   "start_date_interval": "2023-09-14",
                   "end_date_interval": "2023-09-15",
                   "hours_allocated": "60",
                   "prio": "Medium",
                   "status": "Init",
                   "active": True,
                   "task_details": ["", "Details details"],
                   "tags": ['project_', 'LasyMe_TODOs']}

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = TaskPropertiesEditorCore()

    # reformatted_text = test_dialog.get_full_text_from_task_doc(task_sample)
    # test_dialog.load_task_text(reformatted_text)
    test_dialog.load_dates(task_sample)
    test_dialog.load_user(task_sample)
    test_dialog.load_tags(task_sample)

    test_dialog.show()
    sys.exit(app.exec_())
