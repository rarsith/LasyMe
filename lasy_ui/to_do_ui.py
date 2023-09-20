import sys
from PySide2 import QtWidgets

from lasy_ui.tasks_viewer import ExistingTasksViewerCore
from lasy_ui.tasks_properties_tabs import TaskPropertiesTabsBuild
from lasy_ui.tasks_user_input import InputTaskBuildCore
from lasy_ui.tasks_user_input_preview import TaskPreviewPropertiesCore
from lasy_ui.tasks_viewer_tag_filter import TasksViewerTagFilterCore
from lasy_ui.tasks_viewer_scope_status_filter import PrioStatusFilterButtonCore


class ToDoMeMainCore(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ToDoMeMainCore, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.tasks_tags_filter_viewer_wdg = TasksViewerTagFilterCore()
        self.tasks_viewer_wdg = ExistingTasksViewerCore()
        self.tasks_prio_status_filter_wdg = PrioStatusFilterButtonCore()
        self.task_input_wdg = InputTaskBuildCore()
        self.task_preview_properties_wdg = TaskPreviewPropertiesCore()
        self.task_properties_tabs_wdg = TaskPropertiesTabsBuild()

    def create_layout(self):

        viewer_and_input_layout = QtWidgets.QVBoxLayout()
        viewer_and_input_layout.addWidget(self.tasks_viewer_wdg)
        viewer_and_input_layout.addWidget(self.task_preview_properties_wdg)
        viewer_and_input_layout.addWidget(self.task_input_wdg)

        tags_viewer_layout = QtWidgets.QHBoxLayout()
        tags_viewer_layout.addWidget(self.tasks_tags_filter_viewer_wdg)
        tags_viewer_layout.addLayout(viewer_and_input_layout)
        tags_viewer_layout.addWidget(self.tasks_prio_status_filter_wdg)
        tags_viewer_layout.setContentsMargins(0, 0, 0, 0)


        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addLayout(tags_viewer_layout)
        main_layout.addLayout(viewer_and_input_layout)
        main_layout.addWidget(self.task_properties_tabs_wdg)

    def create_connections(self):
        self.task_input_wdg.create_task_btn.clicked.connect(self.tasks_viewer_wdg.refresh_all)
        self.task_input_wdg.task_input_ptx.textChanged.connect(self.set_preview_title)
        self.task_input_wdg.end_date.dateChanged.connect(self.set_preview_end_date)
        self.task_input_wdg.normal_prio_btn.clicked.connect(self.set_preview_normal_prio)
        self.task_input_wdg.low_prio_btn.clicked.connect(self.set_preview_low_prio)
        self.task_input_wdg.med_prio_btn.clicked.connect(self.set_preview_med_prio)
        self.task_input_wdg.high_prio_btn.clicked.connect(self.set_preview_high_prio)
        self.task_input_wdg.critical_prio_btn.clicked.connect(self.set_preview_critical_prio)
        self.task_input_wdg.thirty_min_btn.clicked.connect(self.set_preview_duration_thirty)
        self.task_input_wdg.sixty_min_btn.clicked.connect(self.set_preview_duration_sixty)
        self.task_input_wdg.ninety_min_btn.clicked.connect(self.set_preview_duration_ninety)

        self.tasks_viewer_wdg.task_document_retrieval.connect\
            (self.task_properties_tabs_wdg.task_properties_wdg.populate_all_widgets)

        self.task_properties_tabs_wdg.task_properties_wdg.update_task_text_btn.clicked.connect\
            (self.tasks_viewer_wdg.populate_tasks)
        self.task_properties_tabs_wdg.task_properties_wdg.update_task_properties_btn.clicked.\
            connect(self.tasks_viewer_wdg.populate_tasks)

        self.tasks_tags_filter_viewer_wdg.tag_button_info.connect(self.tasks_viewer_wdg.populate_tasks_by_tags)
        self.tasks_prio_status_filter_wdg.filter_prio_info.connect(self.tasks_viewer_wdg.populate_tasks_by_prio)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.create_tag_btn.clicked.\
            connect(self.tasks_tags_filter_viewer_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.create_tag_btn.clicked. \
            connect(self.task_properties_tabs_wdg.task_properties_wdg.set_tags_wdg.refresh_tag_box)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked.\
            connect(self.tasks_tags_filter_viewer_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked.\
            connect(self.tasks_tags_filter_viewer_wdg.update_tags)

        self.task_properties_tabs_wdg.task_tag_manager_wdg.delete_tag_btn.clicked. \
            connect(self.tasks_tags_filter_viewer_wdg.update_tags)


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

    def set_preview_duration_thirty(self):
        duration_in = self.task_input_wdg.set_time_thirty()
        self.task_preview_properties_wdg.update_duration_wdg(duration_in)

    def set_preview_duration_sixty(self):
        duration_in = self.task_input_wdg.set_time_sixty()
        self.task_preview_properties_wdg.update_duration_wdg(duration_in)

    def set_preview_duration_ninety(self):
        duration_in = self.task_input_wdg.set_time_ninety()
        self.task_preview_properties_wdg.update_duration_wdg(duration_in)





if __name__ == "__main__":
    qss_style_file = "stylesheets/dark_orange/dark_orange_style.qss"

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = ToDoMeMainCore()
    test_dialog.show()

    with open(qss_style_file, "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec_())