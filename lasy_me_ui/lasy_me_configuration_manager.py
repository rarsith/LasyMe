import sys
from PySide2 import QtWidgets, QtCore

from lasy_me_ui.tasks_viewer import ExistingTasksViewerCore
from lasy_me_ui.tasks_properties_tabs import TaskPropertiesTabsBuild
from lasy_me_ui.tasks_user_input import InputTaskBuildCore
from lasy_me_ui.tasks_user_input_preview import TaskPreviewPropertiesCore
from lasy_me_ui.tasks_viewer_tag_filter import TasksViewerTagFilterCore
from lasy_me_ui.tasks_viewer_scope_status_filter import PrioStatusFilterButtonCore


class LasyMeConfigurationManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LasyMeConfigurationManager, self).__init__(parent)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        self.open_browser_btn = QtWidgets.QPushButton("...")
        self.open_browser_btn.setMaximumWidth(35)

        self.db_root_path_le = QtWidgets.QLineEdit()
        self.db_root_path_le.setPlaceholderText("Set Root Path")
        self.db_root_path_le.setMinimumWidth(250)

        self.work_starts_at_le = QtWidgets.QLineEdit()
        self.work_starts_at_le.setPlaceholderText("hh:mm")
        self.work_starts_at_le.setMaximumWidth(50)

        self.work_ends_at_le = QtWidgets.QLineEdit()
        self.work_ends_at_le.setPlaceholderText("hh:mm")
        self.work_ends_at_le.setMaximumWidth(50)

        self.main_viewer_update_interval_le = QtWidgets.QLineEdit()
        self.main_viewer_update_interval_le.setPlaceholderText("min")
        self.main_viewer_update_interval_le.setMaximumWidth(50)

        self.databse_backup_interval_le = QtWidgets.QLineEdit()
        self.databse_backup_interval_le.setPlaceholderText("days")
        self.databse_backup_interval_le.setMaximumWidth(50)

        self.time_per_day_allocation_le = QtWidgets.QLineEdit()
        self.time_per_day_allocation_le.setPlaceholderText("min")
        self.time_per_day_allocation_le.setMaximumWidth(50)


        self.auto_status_management_le = QtWidgets.QCheckBox()
        self.auto_prio_management_le = QtWidgets.QCheckBox()

        self.save_btn = QtWidgets.QPushButton("Save Changes")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")




    def create_layout(self):
        spacer = QtWidgets.QSpacerItem(10, 30)


        path_input_layout = QtWidgets.QHBoxLayout()
        path_input_layout.addWidget(self.db_root_path_le)
        path_input_layout.addWidget(self.open_browser_btn)

        wdg_layout = QtWidgets.QFormLayout()
        wdg_layout.setAlignment(QtCore.Qt.AlignRight)
        wdg_layout.addRow("DB_ROOT_PATH ", path_input_layout)
        wdg_layout.addItem(spacer)
        wdg_layout.addRow("WORK STARTS AT ", self.work_starts_at_le)
        wdg_layout.addRow("WORK ENDS AT ", self.work_ends_at_le)
        wdg_layout.addItem(spacer)
        wdg_layout.addRow("DB UPDATE INTERVAL ", self.main_viewer_update_interval_le)
        wdg_layout.addRow("DB BACKUP INTERVAL ", self.databse_backup_interval_le)
        wdg_layout.addRow("TIME PER DAY ALLOCATED ", self.time_per_day_allocation_le)
        wdg_layout.addItem(spacer)
        wdg_layout.addRow("AUTO STATUS MANAGEMENT ", self.auto_status_management_le)
        wdg_layout.addRow("AUTO PRIORITIES MANAGEMENT ", self.auto_prio_management_le)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.save_btn)
        buttons_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(wdg_layout)
        main_layout.addItem(spacer)
        main_layout.addLayout(buttons_layout)


    def create_connections(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeConfigurationManager()
    test_dialog.show()

    sys.exit(app.exec_())