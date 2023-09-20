import sys
from LasyMeApp.lasy_common_utils import files_utils as filops
from PySide2 import QtWidgets, QtCore
from LasyMeApp.lasy_ops.schemas.config_schema import ConfigSchemaAttrNames, ConfigSchema


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


class LasyMeConfigurationManager(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LasyMeConfigurationManager, self).__init__(parent)

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
        wdg_layout.addRow("DB BACKUP INTERVAL ", self.database_backup_interval_le)
        wdg_layout.addRow("TIME PER DAY ALLOCATED ", self.time_per_day_allocation_le)
        wdg_layout.addItem(spacer)
        wdg_layout.addRow("AUTO STATUS MANAGEMENT ", self.auto_status_management_chckb)
        wdg_layout.addRow("AUTO PRIORITIES MANAGEMENT ", self.auto_prio_management_chckb)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.save_btn)
        buttons_layout.addWidget(self.cancel_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(wdg_layout)
        main_layout.addItem(spacer)
        main_layout.addLayout(buttons_layout)

    def create_connections(self):
        self.open_browser_btn.clicked.connect(self.open_file_dialog)
        self.save_btn.clicked.connect(self.write_cofig_file)
        self.auto_prio_management_chckb.stateChanged.connect(self.is_checked)
        self.cancel_btn.clicked.connect(self.close)
        self.cancel_btn.clicked.connect(self.deleteLater)

    def is_checked(self):
        get_val = self.auto_prio_management_chckb.isChecked()
        print(get_val)

    def gather_options(self):
        schema_attr_names = ConfigSchemaAttrNames()
        schema = ConfigSchema(schema_attr_names)

        schema.root_path = self.db_root_path_le.text()
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

    def write_cofig_file(self):
        config_file = self.gather_options()
        config_file_name = "lasy_config_data"
        path_to_write_to = "../lasy_config"
        filops.write_json(path_to_write_to, config_file_name, config_file)

    def open_file_dialog(self):
        response = QtWidgets.QFileDialog.getExistingDirectory(self, caption='Select a folder')
        if response:
            print(response)
            self.db_root_path_le.setText(response)

    def custom_config_exists(self):
        import os
        relative_path = "../lasy_config/lasy_config_data.json"
        absolute_path = os.path.abspath(relative_path)

        return os.path.exists(absolute_path)

    def populate_config(self):
        is_custom = self.custom_config_exists()
        if not is_custom:
            print ("Loading Defaults. No custom config file found!")
            default_config = self.get_defaults()
            self.load_config(config_file=default_config)
        else:
            custom_config = self.get_custom()
            self.load_config(config_file=custom_config)

    def get_defaults(self):
        default_config_file_path = "../lasy_config/config_defaults/lasy_default_config_data.json"
        get_config_data = filops.open_json(default_config_file_path)
        return get_config_data

    def get_custom(self):
        custom_config_file_path = "../lasy_config/lasy_config_data.json"
        get_config_data = filops.open_json(custom_config_file_path)
        return get_config_data

    def load_config(self, config_file):
        schema_attr_names = ConfigSchemaAttrNames()

        self.db_root_path_le.setText(config_file[schema_attr_names._db_root_path])
        self.work_starts_at_le.setText(config_file[schema_attr_names._start_work_day])
        self.work_ends_at_le.setText(config_file[schema_attr_names._end_work_day])
        self.main_viewer_update_interval_le.setText(config_file[schema_attr_names._update_interval])
        self.database_backup_interval_le.setText(config_file[schema_attr_names._db_backup_interval])
        self.time_per_day_allocation_le.setText(config_file[schema_attr_names._time_per_day_allocation])
        self.auto_status_management_chckb.setChecked(config_file[schema_attr_names._auto_status_management])
        self.auto_prio_management_chckb.setChecked(config_file[schema_attr_names._auto_prio_management])




if __name__ == "__main__":
    # try:
    #     app.close()  # pylint: disable=E0601
    #     app.deleteLater()
    #     del (app)
    # except:
    #     print("instance not deleted")

    app = QtWidgets.QApplication(sys.argv)
    test_dialog = LasyMeConfigurationManager()
    test_dialog.show()

    sys.exit(app.exec_())
