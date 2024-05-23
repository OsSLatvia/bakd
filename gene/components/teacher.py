class Teacher:
    def __init__(self, teacher, subjects = None):
        self.teacher = teacher
        self.subjects = set()
        if subjects is not None:
            for subject in subjects:
                self.subjects.add(subject)
    def __str__(self):
        return f"Teacher({self.teacher})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.teacher == other.teacher
        return False
    def to_dict(self):
        return {"id": self.teacher}
    def __hash__(self):
        return hash(self.teacher)
    # getters 
    def get_teacher(self):
        return self.teacher
    def get_subjects(self):
        return self.subjects
    # setters
    def set_teacher(self, teacher):
        self.teacher = teacher
    def set_subjects(self, subjects):
        self.subjects = subjects
    def add_subject(self, subject):
        self.subjects.add(subject)
    def remove_subject(self, subject):
        self.subjects.discard(subject)

