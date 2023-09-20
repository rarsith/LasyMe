class ConfigAttr:
    def __init__(self):
        self.db_root_path = "db_root_path"
        self.auto_status_management = "auto_status_mng"
        self.auto_prio_management = "auto_prio_mng"
        self.update_interval = "update_interval"
        self.start_work_day = "start_work_day"
        self.end_work_day = "end_work_day"
        self.time_per_day_allocation = "time_per_day_allocation"


class ConfigManager:
    def __init__(self, definitions: ConfigAttr):
        self.definitions = definitions

        self.definitions.db_root_path: str = ""
        self.definitions.auto_status_management: bool = False
        self.definitions.auto_prio_management: bool = False
        self.definitions.update_interval: int = "60"  # minutes
        self.definitions.start_work_day = "10:00"
        self.definitions.end_work_day = "19:00"

    @property
    def root_path(self):
        return self.definitions.db_root_path

    @root_path.setter
    def root_path(self, value: str):
        self.definitions.db_root_path = value

    @property
    def auto_status_mng(self):
        return self.definitions.auto_status_management

    @auto_status_mng.setter
    def auto_status_mng(self, value: bool):
        self.definitions.auto_status_management = value

    @property
    def auto_prio_mng(self):
        return self.definitions.auto_prio_management

    @auto_prio_mng.setter
    def auto_prio_mng(self, value: bool):
        self.definitions.auto_prio_management = value

    @property
    def update_interval(self):
        return self.definitions.update_interval

    @update_interval.setter
    def update_interval(self, value: int):
        self.definitions.update_interval = value

    @property
    def start_day(self):
        return self.definitions.start_work_day

    @start_day.setter
    def start_day(self, value: int):
        self.definitions.start_work_day = value

    @property
    def end_day(self):
        return self.definitions.end_work_day

    @end_day.setter
    def end_day(self, value: int):
        self.definitions.end_work_day = value


    def to_dict(self):
        return {self.definitions.db_root_path: self.root_path,
                self.definitions.auto_status_management: self.auto_status_mng,
                self.definitions.auto_prio_management: self.auto_prio_mng,
                self.definitions.update_interval: self.update_interval,
                self.definitions.start_work_day: self.start_day,
                self.definitions.end_work_day: self.end_day
                }