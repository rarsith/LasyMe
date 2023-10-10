class Statuses:
    def __init__(self):
        self.init = "Init"
        self.in_progress = "InProgress"
        self.done = "DONE"
        self.blocked = "BLOCKED"
        self.followup = "FollowUp"
        self.persistent = "PERSISTENT"
    @property
    def all_statuses(self):
        return [self.init, self.persistent, self.in_progress, self.blocked, self.followup, self.done]
