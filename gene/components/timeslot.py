class Timeslot:
    def __init__(self, timeslot, timeslots_per_day=8):
        self.timeslot = timeslot
        self.timeslots_per_day = timeslots_per_day
        self.day = ((timeslot) // timeslots_per_day) + 1
        self.time = ((timeslot) % timeslots_per_day) + 1
    def __str__(self):
        return f"Timeslot({self.timeslot}, day={self.day}, time={self.time})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Timeslot):
            return self.timeslot == other.timeslot
        return False
    def __hash__(self):
        return hash(self.timeslot)
    def to_dict(self):
        return {
            'timeslot': self.timeslot,
            'timeslots_per_day': self.timeslots_per_day,
        }
    def from_dict(cls, data):
        return cls(data['timeslot'], data['timeslots_per_day'])
    # getters
    def get_timeslot(self):
        return self.timeslot
    def get_day(self):
        return self.day
    def get_time(self):
        return self.time
    # setters
    def set_timeslot(self, timeslot):
        self.timeslot = timeslot
        self.day = ((timeslot) // self.timeslots_per_day) + 1
        self.time = ((timeslot) % self.timeslots_per_day) + 1
