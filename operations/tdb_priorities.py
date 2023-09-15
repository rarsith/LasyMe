class Priorities:
    def __init__(self):
        self.low = "Low"
        self.normal = "Normal"
        self.medium = "Medium"
        self.high = "High"
        self.critical = "Critical"

    @property
    def all_priorities(self):
        return [self.critical, self.high, self.medium, self.normal, self.low]
