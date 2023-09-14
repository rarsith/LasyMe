class TaskAttributesDefinitions:
    def __init__(self):
        self.parent = "parent"
        self.title = "task_title"
        self.created_by = "created_by"
        self.assigned_to = "assigned_to"
        self.date_created = "date_created"
        self.time_created = "time_created"
        self.start_date_interval = "start_date_interval"
        self.end_date_interval = "end_date_interval"
        self.prio = "prio"
        self.status = "status"
        self.active = "active"
        self.task_details = "task_details"
        self.hours_allocated = "hours_allocated"
        self.tags = "tags"


class TagsAttributesDefinitions:
    def __init__(self):
        self.name = "name"
        self.created_by = "created_by"
        self.assigned_to = "assigned_to"
        self.date_created = "date_created"
        self.time_created = "time_created"


class UsersAttributesDefinitions:
    def __init__(self):
        self.name = "name"
        self.assigned_to = "assigned_to"
