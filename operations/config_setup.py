class ConfigAttr:
    def __init__(self):
        self.db_root_path = "db_root_path"
        self.auto_status_management = "auto_status_mng"
        self.auto_prio_management = "auto_prio_mng"
        self.update_interval = "update_interval"


class ConfigManager:
    def __init__(self, definitions: ConfigAttr):
        self.definitions = definitions

        self.db_root_path: str = ""
        self.auto_status_management: bool = False
        self.auto_prio_management: bool = False
        self.update_interval: int = 60  # minutes

    @property
    def root_path(self):
        return self.db_root_path

    @root_path.setter
    def root_path(self, value: str):
        self.db_root_path = value

    @property
    def auto_status_mng(self):
        return self.auto_status_management

    @auto_status_mng.setter
    def auto_status_mng(self, value: bool):
        self.auto_status_management = value

    @property
    def auto_prio_mng(self):
        return self.auto_prio_management

    @auto_prio_mng.setter
    def auto_prio_mng(self, value: bool):
        self.auto_prio_management = value

    @property
    def interval_update(self):
        return self.update_interval

    @interval_update.setter
    def interval_update(self, value: int):
        self.update_interval = value


    def to_dict(self):
        return {self.definitions.db_root_path: self.db_root_path,
                self.definitions.auto_status_management: self.auto_status_management,
                self.definitions.auto_prio_management: self.auto_prio_management,
                self.definitions.update_interval: self.update_interval
                }