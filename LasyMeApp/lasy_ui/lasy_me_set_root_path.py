import os
import sys
from  pathlib import Path
from LasyMeApp.lasy_common_utils import files_utils as filops
from PySide2 import QtWidgets, QtCore
from LasyMeApp.lasy_ops.schemas.config_schema import ConfigSchemaAttrNames, ConfigSchema
from LasyMeApp.lasy_envars.envars import Envars
from LasyMeApp.lasy_ops.connection import ConfigPath


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

        self.save_btn = QtWidgets.QPushButton("Save Changes")
        self.use_default_btn = QtWidgets.QPushButton("Use Default")

    def create_layout(self):
        # spacer = QtWidgets.QSpacerItem(10, 30)

        path_input_layout = QtWidgets.QHBoxLayout()
        path_input_layout.addWidget(self.db_root_path_le)
        path_input_layout.addWidget(self.open_browser_btn)

        wdg_layout = QtWidgets.QFormLayout()
        wdg_layout.setAlignment(QtCore.Qt.AlignRight)
        wdg_layout.addRow("DB_ROOT_PATH ", path_input_layout)
        # wdg_layout.addItem(spacer)

        buttons_layout = QtWidgets.QHBoxLayout()
        buttons_layout.addWidget(self.save_btn)
        buttons_layout.addWidget(self.use_default_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(wdg_layout)
        # main_layout.addItem(spacer)
        main_layout.addLayout(buttons_layout)

    def create_connections(self):
        self.open_browser_btn.clicked.connect(self.open_file_dialog)
        self.save_btn.clicked.connect(self.write_config_file)
        self.use_default_btn.clicked.connect(lambda: self.close())
        self.use_default_btn.clicked.connect(lambda: self.deleteLater())

    def gather_options(self):
        schema_attr_names = ConfigSchemaAttrNames()
        schema = ConfigSchema(schema_attr_names)

        schema.root_path = self.db_root_path_le.text()
        get_all_options = schema.to_dict()

        return get_all_options

    def write_config_file(self):
        base_path = Path(ConfigPath)
        config_file = self.gather_options()
        config_file_name = "lasy_config_data"
        path_to_write_to = "../lasy_config"
        filops.write_json(base_path, config_file_name, config_file)

    def open_file_dialog(self):
        response = QtWidgets.QFileDialog.getExistingDirectory(self, caption='Select a folder')
        if response:
            self.db_root_path_le.setText(response)

    def custom_config_exists(self):
        base_path = Path(ConfigPath)
        custom_config_file_path = "lasy_config_data.json"
        full_path = base_path.joinpath(custom_config_file_path)

        return os.path.exists(full_path)

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
        base_path = Path(ConfigPath)
        default_config_file_path = "config_defaults"
        default_config_file_name = "lasy_default_config_data.json"
        full_path = base_path.joinpath(default_config_file_path, default_config_file_name)
        get_config_data = filops.open_json(full_path)
        return get_config_data

    def get_custom(self):
        base_path = Path(ConfigPath)
        custom_config_file_path = "lasy_config_data.json"
        full_path = base_path.joinpath(custom_config_file_path)
        get_config_data = filops.open_json(full_path)
        return get_config_data

    def load_config(self, config_file):
        schema_attr_names = ConfigSchemaAttrNames()
        self.db_root_path_le.setText(config_file[schema_attr_names._db_root_path])

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
