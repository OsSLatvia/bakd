class Classroom:
    def __init__(self, classroom, size):
        self.classroom = classroom
        self.size = size

    def __str__(self):
        return f"Classroom({self.classroom}, size={self.size})"
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if isinstance(other, Classroom):
            return self.classroom == other.classroom
        return False
    def to_dict(self):
        return {"id": self.classroom, "capacity": self.size}

    # getters
    def get_classroom(self):
        return self.classroom
    def get_size(self):
        return self.size
    # setters
    def set_classroom(self, classroom):
        self.classroom = classroom
    def set_size(self, size):
        self.size = size