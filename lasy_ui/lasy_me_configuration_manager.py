import os
import sys
from lasy_common_utils import files_utils as filops
from lasy_common_utils import path_utils as patils
from PySide2 import QtWidgets, QtCore
from lasy_ops.schemas.config_schema import ConfigSchemaAttrNames, ConfigSchema
from lasy_common_utils import config_file_utils
from lasy_ops.connection import LasyConnections


class LasyFileDialog(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LasyFileDialog, self).__init__(parent)

        self.setWindowTitle("Select root path")

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        pass

    def create_layout(self):
        pass

    def create_connections(self):
        pass


class LasyMeConfigurationManager(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LasyMeConfigurationManager, self).__init__(parent)

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("Lasy Configuration")

        self.create_widgets()
        self.create_layout()
        self.create_connections()
        self.populate_config()

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

        self.database_backup_interval_le = QtWidgets.QLineEdit()
        self.database_backup_interval_le.setPlaceholderText("days")
        self.database_backup_interval_le.setMaximumWidth(50)

        self.time_per_day_allocation_le = QtWidgets.QLineEdit()
        self.time_per_day_allocation_le.setPlaceholderText("min")
        self.time_per_day_allocation_le.setMaximumWidth(50)

        self.auto_status_management_chckb = QtWidgets.QCheckBox()
        self.auto_prio_management_chckb = QtWidgets.QCheckBox()

        self.save_btn = QtWidgets.QPushButton("Save Changes")
        self.cancel_btn = QtWidgets.QPushButton("Cancel")

    def create_layout(self):
        separator01 = self.create_separator()
        separator02 = self.create_separator()
        separator03 = self.create_separator()
        separator04 = self.create_separator()

        path_input_layout = QtWidgets.QHBoxLayout()
        path_input_layout.addWidget(self.db_root_path_le)
        path_input_layout.addWidget(self.open_browser_btn)

        wdg_layout = QtWidgets.QFormLayout()
        wdg_layout.setAlignment(QtCore.Qt.AlignLeft)
        # wdg_layout.addRow("DB_ROOT_PATH ", path_input_layout)
        # wdg_layout.addWidget(separator01)
        wdg_layout.addRow("WORK STARTS AT ", self.work_starts_at_le)
        wdg_layout.addRow("WORK ENDS AT ", self.work_ends_at_le)
        wdg_layout.addWidget(separator02)
        wdg_layout.addRow("DB UPDATE INTERVAL ", self.main_viewer_update_interval_le)
        wdg_layout.addRow("DB BACKUP INTERVAL ", self.database_backup_interval_le)
        wdg_layout.addRow("TIME PER DAY ALLOCATED ", self.time_per_day_allocation_le)
        wdg_layout.addWidget(separator03)
        wdg_layout.addRow("AUTO STATUS MANAGEMENT ", self.auto_status_management_chckb)
        wdg_layout.addRow("AUTO PRIORITIES MANAGEMENT ", self.auto_prio_management_chckb)
        wdg_layout.addWidget(separator04)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.save_btn)
        buttons_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(wdg_layout)
        main_layout.addLayout(buttons_layout)

    def create_separator(self):
        separator = QtWidgets.QFrame()
        separator.setFrameShape(QtWidgets.QFrame.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        return separator

    def create_connections(self):
        # self.open_browser_btn.clicked.connect(self.open_file_dialog)
        self.save_btn.clicked.connect(self.create_lasy_data)

        self.save_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.deleteLater)

        self.cancel_btn.clicked.connect(self.close)
        self.cancel_btn.clicked.connect(self.deleteLater)

    def create_lasy_data(self):
        root_path = patils.convert_path_to_universal(os.environ.get("LASY_DATA_ROOT"))
        LasyConnections().create_implicit_structure(root_path)
        self.write_config_file()

    def gather_options(self):
        schema_attr_names = ConfigSchemaAttrNames()
        schema = ConfigSchema(schema_attr_names)
        # schema.root_path = self.db_root_path_le.text()
        schema.start_day = self.work_starts_at_le.text()
        schema.end_day = self.work_ends_at_le.text()
        schema.update_timer_interval = self.main_viewer_update_interval_le.text()
        schema.database_backup_interval = self.database_backup_interval_le.text()
        schema.time_per_day = self.time_per_day_allocation_le.text()

        is_status_checked = self.auto_status_management_chckb.isChecked()
        schema.auto_status_mng = is_status_checked

        is_prio_checked = self.auto_prio_management_chckb.isChecked()
        schema.auto_prio_mng = is_prio_checked

        get_all_options = schema.to_dict()

        return get_all_options

    def write_config_file(self):
        base_path = LasyConnections().config_dir_path()
        config_file = self.gather_options()
        config_file_name = "lasy_config_data"
        filops.write_json(base_path, config_file_name, config_file)

    def write_default_config_file(self):
        base_path = LasyConnections().default_config_path()
        config_file = self.create_default_config_file()
        config_file_name = "lasy_default_config_data"
        filops.write_json(base_path, config_file_name, config_file)

    def open_file_dialog(self):
        response = QtWidgets.QFileDialog.getExistingDirectory(self, caption='Select a folder')
        if response:
            self.db_root_path_le.setText(response)

    def custom_config_exists(self):
        custom_config_exists = config_file_utils.custom_config_exists()
        return custom_config_exists

    def populate_config(self):
        is_custom = self.custom_config_exists()
        if not is_custom:
            self.write_default_config_file()
            print ("Loading Defaults. No custom config file found!")
            default_config = self.get_defaults()
            self.load_config(config_file=default_config)
        else:
            custom_config = self.get_custom()
            self.load_config(config_file=custom_config)

    def get_defaults(self):
        base_path = LasyConnections().default_config_full_path()
        get_config_data = filops.open_json(base_path)
        return get_config_data

    def get_custom(self):
        config_file = LasyConnections().get_config_file_content()
        return config_file

    def load_config(self, config_file):
        schema_attr_names = ConfigSchemaAttrNames()
        # if len(config_file[schema_attr_names._db_root_path]) != 0:
        #     self.db_root_path_le.setText(config_file[schema_attr_names._db_root_path])
        # else:
        #     default_databses_folder = patils.to_user_home_dir(parent_directory="lasy_databses")
        #     self.db_root_path_le.setText(str(default_databses_folder))

        self.work_starts_at_le.setText(config_file[schema_attr_names._start_work_day])
        self.work_ends_at_le.setText(config_file[schema_attr_names._end_work_day])
        self.main_viewer_update_interval_le.setText(config_file[schema_attr_names._update_interval])
        self.database_backup_interval_le.setText(config_file[schema_attr_names._db_backup_interval])
        self.time_per_day_allocation_le.setText(config_file[schema_attr_names._time_per_day_allocation])
        self.auto_status_management_chckb.setChecked(config_file[schema_attr_names._auto_status_management])
        self.auto_prio_management_chckb.setChecked(config_file[schema_attr_names._auto_prio_management])

    def create_default_config_file(self):
        schema_attr_names = ConfigSchemaAttrNames()
        schema = ConfigSchema(schema_attr_names)

        # schema.root_path = patils.to_user_home_dir()
        schema.start_day = "10:00"
        schema.end_day = "19:00"
        schema.update_timer_interval = "60"
        schema.database_backup_interval = "10"
        schema.time_per_day = "300"

        is_status_checked = False
        schema.auto_status_mng = is_status_checked

        is_prio_checked = False
        schema.auto_prio_mng = is_prio_checked

        get_all_options = schema.to_dict()

        return get_all_options


if __name__ == "__main__":
    import pprint
    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeConfigurationManager()
    test_dialog.show()

    sys.exit(app.exec_())

    # cc = os.environ.get("LASY_DATA_ROOT")
    # print(cc)
    # pprint.pprint(dict(cc), width = 1)