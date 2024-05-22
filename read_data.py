from gene.student_group import StudentGroup
from gene.event import Event
from gene.gene import Gene
from gene.components.classroom import Classroom
from gene.components.teacher import Teacher
from gene.components.timeslot import Timeslot
import random



def read_data_from_file():
    teachers = []
    classrooms = []
    student_groups = []
    events = []

    with open('output.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            if line.startswith("Teacher("):
                name = line[8:-1]
                teacher = Teacher(name)
                teachers.append(teacher)
            elif line.startswith("Classroom("):
                id, capacity = line[10:-1].split(", ")
                classroom = Classroom(id, capacity)
                classrooms.append(classroom)
            elif line.startswith("StudentGroup("):
                id, size = line[13:-1].split(", ")
                student_group = StudentGroup(int(id), int(size))
                student_groups.append(student_group)
            elif line.startswith("Event("):
                # Parse the event line to create an Event object
                pass

    return teachers, classrooms, student_groups, events

def print_data(teachers, classrooms, student_groups, events):
    print("Teachers:")
    for teacher in teachers:
        print(teacher)

    print("\nClassrooms:")
    for classroom in classrooms:
        print(classroom)

    print("\nStudent Groups:")
    for student_group in student_groups:
        print(student_group)

    print("\nEvents:")
    for event in events:
        print(event)

teachers, classrooms, student_groups, events = read_data_from_file()
print_data(teachers, classrooms, student_groups, events)