class TinyAttributesPaths:
    def __init__(self, definitions):
        self.definitions = definitions

    def active(self, value: bool) -> dict:
        return {self.definitions.active: value}

    def parent(self, value: int) -> dict:
        return {self.definitions.parent: value}

    def task_title(self, value: str) -> dict:
        return {self.definitions.title: value}

    def assigned_to(self, value: str) -> dict:
        return {self.definitions.assigned_to: value}

    def start_interval(self, value: int) -> dict:
        return {self.definitions.start_date_interval: value}

    def end_interval(self, value: int) -> dict:
        return {self.definitions.end_date_interval: value}

    def hours_allocated(self, value: int) -> dict:
        return {self.definitions.hours_allocated: value}

    def priority(self, value: str) -> dict:
        return {self.definitions.prio: value}

    def status(self, value: str) -> dict:
        return {self.definitions.status: value}

    def task_details(self, value: str) -> dict:
        return {self.definitions.task_details: value}
