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

        self.db_root_path = ""
        self.auto_status_management = ""
        self.auto_prio_management = ""
        self.update_interval = ""  # minutes
        self.start_work_day = ""
        self.end_work_day = ""

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
    def update_timer_interval(self):
        return self.update_interval

    @update_timer_interval.setter
    def update_timer_interval(self, value: int):
        self.update_interval = value

    @property
    def start_day(self):
        return self.start_work_day

    @start_day.setter
    def start_day(self, value: int):
        self.start_work_day = value

    @property
    def end_day(self):
        return self.end_work_day

    @end_day.setter
    def end_day(self, value: int):
        self.end_work_day = value


    def to_dict(self):
        return {self.definitions.db_root_path: self.root_path,
                self.definitions.auto_status_management: self.auto_status_mng,
                self.definitions.auto_prio_management: self.auto_prio_mng,
                self.definitions.update_interval: self.update_timer_interval,
                self.definitions.start_work_day: self.start_day,
                self.definitions.end_work_day: self.end_day
                }

if __name__ == "__main__":
    Attr = ConfigAttr()
    ConfMan = ConfigManager(Attr)
    ConfMan.update_timer_interval = "18"

    Con_dict = ConfMan.to_dict()
    print(Con_dict)