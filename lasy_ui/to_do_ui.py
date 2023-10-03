import sys
from PySide2 import QtWidgets

from lasy_ui.tasks_viewer import ExistingTasksViewerCore
from lasy_ui.tasks_properties_tabs import TaskPropertiesTabsBuild
from lasy_ui.tasks_user_input import InputTaskBuildCore
from lasy_ui.tasks_user_input_preview import TaskPreviewPropertiesCore
from lasy_ui.tasks_viewer_tag_filter import TasksViewerTagFilterCore
from lasy_ui.tasks_viewer_prios_filter import TasksPrioFilterCore
from lasy_ui.tasks_viewer_status_filter import TasksStatusFilterCore
from lasy_ui.custom_widgets.separator_widget import SeparatorWDG


class ToDoMeMainCore(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ToDoMeMainCore, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        self.tasks_tags_filter_viewer_wdg = TasksViewerTagFilterCore()
        self.tasks_viewer_wdg = ExistingTasksViewerCore()
        self.tasks_prio_filter_wdg = TasksPrioFilterCore()
        self.tasks_status_filter_wdg = TasksStatusFilterCore()
        self.task_input_wdg = InputTaskBuildCore()
        self.task_preview_properties_wdg = TaskPreviewPropertiesCore()
        self.task_properties_tabs_wdg = TaskPropertiesTabsBuild()

    def create_layout(self):
        separator01 = SeparatorWDG()
        separator02 = SeparatorWDG()

        filters_layout = QtWidgets.QVBoxLayout()
        filters_layout.addWidget(self.tasks_prio_filter_wdg)
        filters_layout.addWidget(separator01)
        filters_layout.addWidget(separator02)
        filters_layout.addWidget(self.tasks_status_filter_wdg)
        filters_layout.addStretch(1)

        viewer_layout = QtWidgets.QHBoxLayout()
        viewer_layout.addWidget(self.tasks_viewer_wdg)
        viewer_layout.addLayout(filters_layout)
        viewer_layout.addWidget(self.task_properties_tabs_wdg)

        tags_viewer_layout = QtWidgets.QVBoxLayout()
        tags_viewer_layout.addLayout(viewer_layout)
        # tags_viewer_layout.addStretch(1)
        tags_viewer_layout.addWidget(self.task_preview_properties_wdg)
        tags_viewer_layout.addWidget(self.task_input_wdg)

        # tags_viewer_layout.addLayout(filters_layout)
        # tags_viewer_layout.setContentsMargins(0, 0, 0, 0)

        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.tasks_tags_filter_viewer_wdg)
        main_layout.addLayout(tags_viewer_layout)

    def create_connections(self):
        self.task_input_wdg.create_task_btn.clicked.connect(self.tasks_viewer_wdg.refresh_all)
        self.task_input_wdg.create_task_btn.clicked.connect(self.task_preview_properties_wdg.clear_all)
        self.task_input_wdg.task_input_ptx.textChanged.connect(self.set_preview_title)
        self.task_input_wdg.end_date.dateChanged.connect(self.set_preview_end_date)
        self.task_input_wdg.normal_prio_btn.clicked.connect(self.set_preview_normal_prio)
        self.task_input_wdg.low_prio_btn.clicked.connect(self.set_preview_low_prio)
        self.task_input_wdg.med_prio_btn.clicked.connect(self.set_preview_med_prio)
        self.task_input_wdg.high_prio_btn.clicked.connect(self.set_preview_high_prio)
        self.task_input_wdg.critical_prio_btn.clicked.connect(self.set_preview_critical_prio)

        self.tasks_viewer_wdg.task_document_retrieval.connect\
            (self.task_properties_tabs_wdg.task_properties_wdg.populate_all_widgets)

        self.task_properties_tabs_wdg.task_properties_wdg.update_task_text_btn.clicked.connect\
            (self.tasks_viewer_wdg.populate_tasks)

        self.task_properties_tabs_wdg.task_properties_wdg.create_tasks_from_selection_btn.clicked.connect \
            (self.tasks_viewer_wdg.populate_tasks)

        self.task_properties_tabs_wdg.task_properties_wdg.update_task_properties_btn.clicked.\
            connect(self.tasks_viewer_wdg.populate_tasks)

        self.tasks_tags_filter_viewer_wdg.tag_button_info.connect(self.tasks_viewer_wdg.populate_tasks_by_tags)

        self.tasks_prio_filter_wdg.filter_prio_info.connect(self.tasks_viewer_wdg.populate_tasks_by_prio)

        self.tasks_status_filter_wdg.filter_status_info.connect(self.tasks_viewer_wdg.populate_tasks_by_status)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.create_tag_btn.clicked.\
            connect(self.tasks_tags_filter_viewer_wdg.update_tags)

        self.task_properties_tabs_wdg.task_properties_wdg.set_tags_wdg.assign_tag_button_info. \
            connect(self.task_properties_tabs_wdg.task_properties_wdg.update_per_click_tags)

        self.task_properties_tabs_wdg.task_properties_wdg.snooze_it_wdg.snooze_one_bth.clicked. \
            connect(lambda: self.tasks_viewer_wdg.refresh_all())

        self.task_properties_tabs_wdg.task_properties_wdg.snooze_it_wdg.snooze_three_bth.clicked. \
            connect(lambda: self.tasks_viewer_wdg.refresh_all())

        self.task_properties_tabs_wdg.task_properties_wdg.snooze_it_wdg.snooze_five_bth.clicked. \
            connect(lambda: self.tasks_viewer_wdg.refresh_all())

        self.task_properties_tabs_wdg.task_properties_wdg.snooze_it_wdg.commmit_btn.clicked. \
            connect(lambda: self.tasks_viewer_wdg.refresh_all())


        self.task_properties_tabs_wdg.task_tag_manager_wdg.create_tag_btn.clicked. \
            connect(self.task_properties_tabs_wdg.task_properties_wdg.set_tags_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked. \
            connect(self.task_properties_tabs_wdg.task_properties_wdg.set_tags_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.create_tag_btn.clicked. \
            connect(self.task_input_wdg.set_tags_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked.\
            connect(self.task_input_wdg.set_tags_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked.\
            connect(self.tasks_tags_filter_viewer_wdg.update_tags)

        # self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked. \
        #     connect(self.tasks_tags_filter_viewer_wdg.update_tags)

    def set_preview_title(self):
        title_in = self.task_input_wdg.get_title()
        self.task_preview_properties_wdg.update_task_title_wdg(title_in)

    def set_preview_end_date(self):
        end_date_in = self.task_input_wdg.get_sel_task_end_date()
        self.task_preview_properties_wdg.update_end_wdg(end_date_in)

    def set_preview_normal_prio(self):
        prio_in = self.task_input_wdg.set_to_normal_prio()
        self.task_preview_properties_wdg.update_priority_wdg(prio_in)

    def set_preview_low_prio(self):
        prio_in = self.task_input_wdg.set_to_low_prio()
        self.task_preview_properties_wdg.update_priority_wdg(prio_in)

    def set_preview_med_prio(self):
        prio_in = self.task_input_wdg.set_to_med_prio()
        self.task_preview_properties_wdg.update_priority_wdg(prio_in)

    def set_preview_high_prio(self):
        prio_in = self.task_input_wdg.set_to_high_prio()
        self.task_preview_properties_wdg.update_priority_wdg(prio_in)

    def set_preview_critical_prio(self):
        prio_in = self.task_input_wdg.set_to_critical_prio()
        self.task_preview_properties_wdg.update_priority_wdg(prio_in)


if __name__ == "__main__":
    qss_style_file = "stylesheets/dark_orange/dark_orange_style.qss"

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = ToDoMeMainCore()
    test_dialog.show()

    with open(qss_style_file, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())
