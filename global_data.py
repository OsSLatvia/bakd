from generate_data import read_data_from_file
from gene.components.timeslot import Timeslot

all_teachers, all_classrooms, student_groups, all_events = read_data_from_file("data.txt")
all_timeslots = []
days = 5
timeslots_in_day = 8
number_of_timeslots = days * timeslots_in_day
for i in range(number_of_timeslots):
    all_timeslots.append(Timeslot(i, timeslots_in_day))
number_of_events=len(all_events)