class Statuses:
    def __init__(self):
        self.init = "Init"
        self.in_progress = "InProgress"
        self.done = "DONE"
        self.blocked = "BLOCKED"
        self.followup = "FollowUp"
    @property
    def all_statuses(self):
        return [self.init, self.in_progress, self.done, self.blocked, self.followup]
