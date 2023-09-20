import getpass
from lasy_common_utils.date_time import DateTime
from lasy_ops.tdb_attributes_definitions import TaskAttributesDefinitions
from lasy_ops.tdb_priorities import Priorities
from lasy_ops.tdb_statuses import Statuses


class TaskSchema:
    def __init__(self, definitions: TaskAttributesDefinitions):
        self.definitions = definitions

        self.parent = "root"
        self.title = "-- no title --"
        self.created_by = ""
        self.date_created = ""
        self.time_created = ""
        self.datetime_created = ""
        self.assigned_to = ""
        self.start_date_interval = ""
        self.end_date_interval = ""
        self.prio = Priorities().normal
        self.status = Statuses().init
        self.active = True
        self.task_details = ""
        self.hours_allocated = ""
        self.tags = []

    @property
    def task_title(self):
        return self.title

    @task_title.setter
    def task_title(self, task_title):
        self.title = task_title

    @property
    def parent_task(self):
        return self.parent

    @parent_task.setter
    def parent_task(self, parent_task_id):
        self.parent = parent_task_id

    @property
    def created_by_user(self):
        return self.created_by

    @created_by_user.setter
    def created_by_user(self, value):
        self.created_by = value

    @property
    def date_created_at(self):
        return self.date_created

    @date_created_at.setter
    def date_created_at(self, value):
        self.date_created = value

    @property
    def time_created_at(self):
        return self.time_created

    @time_created_at.setter
    def time_created_at(self, value):
        self.time_created = value

    @property
    def datetime_created_at(self):
        return self.datetime_created

    @datetime_created_at.setter
    def datetime_created_at(self, value):
        self.datetime_created = value

    @property
    def assigned_to_user(self):
        return self.assigned_to

    @assigned_to_user.setter
    def assigned_to_user(self, value):
        self.assigned_to = value

    @property
    def start_interval(self):
        return self.start_date_interval

    @start_interval.setter
    def start_interval(self, value):
        self.start_date_interval = value

    @property
    def end_interval(self):
        return self.end_date_interval

    @end_interval.setter
    def end_interval(self, value):
        self.end_date_interval = value

    @property
    def task_details_text(self):
        return self.task_details

    @task_details_text.setter
    def task_details_text(self, value):
        self.task_details = value

    @property
    def hours_executable(self):
        return self.hours_allocated

    @hours_executable.setter
    def hours_executable(self, value):
        self.hours_allocated = value

    @property
    def task_tag(self):
        return self.tag

    @task_tag.setter
    def task_tag(self, value):
        self.tag = value

    @property
    def task_priority(self):
        return self.prio

    @task_priority.setter
    def task_priority(self, value:Priorities):
        self.prio = value

    def to_dict(self):
        return {self.definitions.title: self.task_title,
                self.definitions.parent: self.parent_task,
                self.definitions.created_by: self.created_by,
                self.definitions.date_created: self.date_created,
                self.definitions.time_created: self.time_created,
                self.definitions.datetime_created: self.datetime_created,
                self.definitions.assigned_to: self.assigned_to,
                self.definitions.start_date_interval: self.start_date_interval,
                self.definitions.end_date_interval: self.end_date_interval,
                self.definitions.hours_allocated: self.hours_allocated,
                self.definitions.prio: self.prio,
                self.definitions.status: self.status,
                self.definitions.active: self.active,
                self.definitions.task_details: self.task_details,
                self.definitions.tags: ''
                }


if __name__ == "__main__":
    import pprint

    tasks_key_definitions = TaskAttributesDefinitions()
    new_task = TaskSchema(tasks_key_definitions)

    new_task.task_title="This is a new Title Using decoupling"
    new_task.parent = 2
    new_task.hours_allocated = 4
    new_task.assigned_to = "dumbledoreSS"

    dict_conv = new_task.to_dict()

    pprint.pprint(dict_conv)

