import copy
class StudentGroup:
    def __init__(self, group_ID, size, events=None):
        self.group_ID = group_ID
        self.size = size
        self.events = set()
        if events is not None:
            for event in events:
                self.events.add(event)
                event.add_student_group(self)
    
    def __str__(self):
        return f"group({self.group_ID}, size={self.size})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, StudentGroup):
            return self.group_ID == other.group_ID
        return False
    def to_dict(self):
        return {"id": self.group_ID, "size": self.size}


    def __hash__(self):
        return hash(self.group_ID)
    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        copied_group = StudentGroup(self.group_ID, self.size)
        memo[id(self)] = copied_group
        copied_group.events = copy.deepcopy(self.events, memo)
        return copied_group
    # getters
    def get_group_ID(self):
        return self.group_ID
    def get_size(self):
        return self.size
    def get_events(self):
        return self.events
    # setters
    def set_size (self, size):
        self.size = size
    def set_events(self, events):
        self.events = events
    def add_events(self, events):
        for event in events:
            if event not in self.events:
                self.events.add(event)
                event.add_student_group(self)
    def add_event(self, event):
        if event not in self.events:
            self.events.add(event)
            event.add_student_group(self)
    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)
            event.remove_student_group(self)