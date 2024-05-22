from gene.student_group import StudentGroup
from gene.event import Event
from gene.gene import Gene
from gene.components.classroom import Classroom
from gene.components.teacher import Teacher
from gene.components.timeslot import Timeslot
import random
import json

def store_data_to_file(file_name, teachers, classrooms, student_groups, events):
    data = {
        "teachers": [teacher.to_dict() for teacher in teachers],
        "classrooms": [classroom.to_dict() for classroom in classrooms],
        "student_groups": [student_group.to_dict() for student_group in student_groups],
        "events": [event.to_dict() for event in events]
    }
    with open(file_name, 'w') as f:
        json.dump(data, f)

def read_data_from_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)

    teachers = [Teacher(d["id"]) for d in data["teachers"]]
    classrooms = [Classroom(d["id"], d["capacity"]) for d in data["classrooms"]]
    student_groups = [StudentGroup(d["id"], d["size"]) for d in data["student_groups"]]
    events = [Event(d["id"], [student_groups[id] for id in d["student_group_list"]]) for d in data["events"]]

    return teachers, classrooms, student_groups, events
def generate_teachers(number_of_teachers):
    return [Teacher(f"ID{i}") for i in range(1, number_of_teachers + 1)]
def generate_classrooms(number_of_classrooms):
    return [Classroom(i, random.randint(20, 200)) for i in range(number_of_classrooms)]
def generate_student_groups(number_of_groups):
    return [StudentGroup(i, random.randint(15, 30)) for i in range(number_of_groups)]

def generate_events(number_of_events, student_groups):
    events = []
    for _ in range(number_of_events):
        event_student_group_list = set(random.sample(student_groups, random.randint(1, 3)))
        events.append(Event(_, event_student_group_list))
    return events

# def write_data_to_file(teacher_list, classroom_list, student_group_list, event_list):
#     with open('output.txt', 'w') as f:
#         f.write("Teachers:\n")
#         for teacher in teacher_list:
#             f.write(str(teacher) + '\n')
#         f.write("\n")
        
#         f.write("Classrooms:\n")
#         for classroom in classroom_list:
#             f.write(str(classroom) + '\n')
#         f.write("\n")
        
#         f.write("Student Groups:\n")
#         for student_group in student_group_list:
#             f.write(str(student_group) + '\n')
#         f.write("\n")
        
#         f.write("Events:\n")
#         for event in event_list:
#             f.write(str(event) + '\n')

def main():
    number_of_events = 2
    number_of_groups = 10
    days = 5
    timeslots_in_day = 8
    timeslots = [Timeslot(i) for i in range(days * timeslots_in_day)]
    number_of_classrooms = 10
    number_of_teachers = 4
    teacher_list = generate_teachers(number_of_teachers)
    classroom_list = generate_classrooms(number_of_classrooms)
    student_group_list = generate_student_groups(number_of_groups)
    event_list = generate_events(number_of_events, student_group_list)
    
    store_data_to_file("output.txt", teacher_list, classroom_list, student_group_list, event_list)
    teachers, classrooms, student_groups, events = read_data_from_file("output.txt")
    print(teachers)
    print("---------------")
    print(classrooms)
    print("---------------")
    print(student_groups)
    print("---------------")
    print(events)
    print("---------------")
if __name__ == "__main__":
    main()