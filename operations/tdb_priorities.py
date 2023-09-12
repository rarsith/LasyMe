class Priorities:
    def __init__(self):
        self.normal = "Normal"
        self.medium = "Medium"
        self.high = "High"
        self.critical = "Critical"

    @property
    def all_priorities(self):
        return [self.normal, self.medium, self.high, self.critical]
