import copy
class Event:
    def __init__(self, event_ID, student_groups=None, subject=None):
        self.event_ID = event_ID
        self.student_groups = set()
        if student_groups is not None:
            for student_group in student_groups:
                self.student_groups.add(student_group)
                student_group.add_event(self)
        self.subject=subject
    def __str__(self):
        return f"event({self.event_ID}, student_groups={self.student_groups})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Event):
            return self.event_ID == other.event_ID
        return False
    def to_dict(self):
        return {"id": self.event_ID, "student_group_list": [group.group_ID for group in self.student_groups]}
    
    def __hash__(self):
        return hash(self.event_ID)
    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        copied_event = Event(self.event_ID)
        memo[id(self)] = copied_event
        copied_event.student_groups = copy.deepcopy(self.student_groups, memo)
        copied_event.subject = copy.deepcopy(self.subject, memo)
        return copied_event
    # getters
    def get_event_ID(self):
        return self.event_ID
    def get_subject(self):
        return self.subject
    def get_student_groups(self):
        return self.student_groups
    # setters
    def set_subject(self, subject):
        self.subject=subject
    def set_student_groups(self, student_groups):
        self.student_groups = student_groups
    def add_student_groups(self, student_groups):
        for student_group in student_groups:
            if student_group not in self.student_groups:
                self.student_groups.add(student_group)
                student_group.add_event(self)
    def add_student_group(self, student_group):
        if student_group not in self.student_groups:
            self.student_groups.add(student_group)
            student_group.add_event(self)

