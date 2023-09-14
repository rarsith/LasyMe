class Priorities:
    def __init__(self):
        self.low = "Low"
        self.normal = "Normal"
        self.medium = "Medium"
        self.high = "High"
        self.critical = "CRITICAL"

    @property
    def all_priorities(self):
        return [self.low ,self.normal, self.medium, self.high, self.critical]
