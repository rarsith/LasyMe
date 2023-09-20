class ConfigSchemaAttrNames:
    def __init__(self):
        self._db_root_path = "db_root_path"
        self._auto_status_management = "auto_status_mng"
        self._auto_prio_management = "auto_prio_mng"
        self._update_interval = "update_interval"
        self._start_work_day = "start_work_day"
        self._end_work_day = "end_work_day"
        self._time_per_day_allocation = "time_per_day_allocation"
        self._db_backup_interval = "database_backup_interval"



class ConfigSchema:
    def __init__(self, definitions: ConfigSchemaAttrNames):
        self.definitions = definitions

        self._db_root_path = ""
        self._auto_status_management = ""
        self._auto_prio_management = ""
        self._update_interval = ""  # minutes
        self._time_per_day_alloc = ""
        self._database_backup_inter = ""
        self._start_work_day = ""
        self._end_work_day = ""

    @property
    def root_path(self):
        return self._db_root_path

    @root_path.setter
    def root_path(self, value: str):
        self._db_root_path = value

    @property
    def auto_status_mng(self):
        return self._auto_status_management

    @auto_status_mng.setter
    def auto_status_mng(self, value: bool):
        self._auto_status_management = value

    @property
    def auto_prio_mng(self):
        return self._auto_prio_management

    @auto_prio_mng.setter
    def auto_prio_mng(self, value: bool):
        self._auto_prio_management = value

    @property
    def update_timer_interval(self):
        return self._update_interval

    @update_timer_interval.setter
    def update_timer_interval(self, value: int):
        self._update_interval = value

    @property
    def start_day(self):
        return self._start_work_day

    @start_day.setter
    def start_day(self, value: int):
        self._start_work_day = value

    @property
    def end_day(self):
        return self._end_work_day

    @end_day.setter
    def end_day(self, value: int):
        self._end_work_day = value

    @property
    def time_per_day(self):
        return self._time_per_day_alloc

    @time_per_day.setter
    def time_per_day(self, value: int):
        self._time_per_day_alloc = value

    @property
    def database_backup_interval(self):
        return self._database_backup_inter

    @database_backup_interval.setter
    def database_backup_interval(self, value: int):
        self._database_backup_inter = value

    def to_dict(self):
        return {self.definitions._db_root_path: self.root_path,
                self.definitions._auto_status_management: self.auto_status_mng,
                self.definitions._auto_prio_management: self.auto_prio_mng,
                self.definitions._update_interval: self.update_timer_interval,
                self.definitions._time_per_day_allocation: self.time_per_day,
                self.definitions._db_backup_interval: self.database_backup_interval,
                self.definitions._start_work_day: self.start_day,
                self.definitions._end_work_day: self.end_day

                }

if __name__ == "__main__":
    Attr = ConfigSchemaAttrNames()
    ConfMan = ConfigSchema(Attr)
    ConfMan.update_timer_interval = "18"

    Con_dict = ConfMan.to_dict()
    print(Con_dict)