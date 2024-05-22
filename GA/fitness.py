from GA.validate import is_valid
import global_data

all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_group_list = global_data.student_groups

def fitness_function(chromosome):
    # # Define your fitness calculation logic here
    # score = sum([1 for gene in solution if is_valid(gene)])
    # return score
    cost = costOfSoftConstraints(chromosome)
    fitness_value=1/(1+cost)

    return fitness_value, cost

def costOfSoftConstraints(chromosome):
    weights=[0.2, 0.6]
    free_day_cost = checkForFreeDay(chromosome) * weights[0]
    teacher_load_cost = checkTeacherLoad(chromosome) * weights[1]
    # constraint3_cost = constraints.checkConstraint3(chromosome) * weights[2]
    # constraint4_cost = constraints.checkConstraint4(chromosome) * weights[3]
    return free_day_cost + teacher_load_cost #+ constraint2_cost + constraint3_cost + constraint4_cost
def checkForFreeDay(chromosome):
    cost=0
    for student_group in student_group_list:
        unique_days=set()
        for event in student_group.get_events():
            gene=chromosome[event.get_event_ID()]
            timeslot=gene.get_timeslot()
            unique_days.add(timeslot.get_day())
        if len(unique_days) > 4:
            cost=cost+1 #ja studentu grupai nav brīvas dienas, mīkstā ierobežojuma pārkāpšanas maksa tiek palielināta
        else:
            if 1 in unique_days and 5 in unique_days:
                cost=cost+0.3 #ja ir brīva diena bet nav ne nedēļas beigās ne sākumā, arī palielina pārkāpšanas maksu 
    return cost
def checkTeacherLoad(chromsome):
    cost = 0
    return cost