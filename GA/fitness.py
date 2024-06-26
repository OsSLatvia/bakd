from GA.validate import is_valid
import global_data

all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_group_list = global_data.student_groups

def fitness_function(chromosome):
    costs = costOfSoftConstraints(chromosome)
    cost_sum = sum(costs)
    fitness_value=1/(1+cost_sum)

    return fitness_value, costs

def costOfSoftConstraints(chromosome):
    weights=[0.2, 0.7, 0.7, 0.2, 0.4]
    cost=[]
    cost.append(checkForFreeDay(chromosome) * weights[0])
    cost.append(checkTeacherLoad(chromosome) * weights[1])
    cost.append(checkRoomSpace(chromosome) * weights[2])
    cost.append(checkForFreePeriodsInDay(chromosome) * weights[3])
    cost.append(checkForEventsInDay(chromosome) * weights[4])
    rounded_cost = [round(c, 2) for c in cost]
    return rounded_cost 
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
    teacher_loads = {}
    for gene in chromsome:
        if gene.get_teacher() not in teacher_loads:
            teacher_loads[gene.get_teacher()] = 0
        teacher_loads[gene.get_teacher()] += 1
    for teacher, count in teacher_loads.items():
        
        if count > 10:
            cost = cost + 1
        if count < 5:
            cost = cost + 1
    return cost
def checkRoomSpace(chromosome):
    cost = 0
    for gene in chromosome:
        students_in_event = gene.students_in_event
        maximum_room_capacity = gene.get_classroom().get_size()
        if students_in_event > maximum_room_capacity:
            cost += 1
        elif students_in_event > 0.9 * maximum_room_capacity:
            over_capacity_percentage = (students_in_event - 0.9 * maximum_room_capacity) / (0.1 * maximum_room_capacity)
            cost += over_capacity_percentage
    return cost
def checkForFreePeriodsInDay(chromosome):
    cost = 0
    for student_group in student_group_list:
        unique_days = set()
        for event in student_group.get_events():
            gene = chromosome[event.get_event_ID()]
            timeslot = gene.get_timeslot()
            unique_days.add(timeslot.get_day())
        
        for day in unique_days:
            events_on_day = [event for event in student_group.get_events() if chromosome[event.get_event_ID()].get_timeslot().get_day() == day]
            events_on_day.sort(key=lambda event: chromosome[event.get_event_ID()].get_timeslot().get_timeslot())  # Sort events by timeslot
            
            prev_event_end = 0
            for event in events_on_day:
                timeslot = chromosome[event.get_event_ID()].get_timeslot()
                event_start = timeslot.get_timeslot()
                
                # Check if there's a gap between the previous event end and the current event start
                if event_start - prev_event_end > 1:
                    cost += 1  # Increase cost if there's a gap
                prev_event_end = event_start + 1  # Update previous event end
                
    return cost

def checkForEventsInDay(chromosome):
    cost = 0
    for student_group in student_group_list:
        unique_days = set()
        for event in student_group.get_events():
            gene = chromosome[event.get_event_ID()]
            timeslot = gene.get_timeslot()
            unique_days.add(timeslot.get_day())
        
        for day in unique_days:
            events_on_day = [event for event in student_group.get_events() if chromosome[event.get_event_ID()].get_timeslot().get_day() == day]
            
            # Count the number of events on the day
            num_events_on_day = len(events_on_day)
            
            # Increase cost if there are more than 4 events in one day
            if num_events_on_day > 5:
                cost += 1
            else:
                if num_events_on_day > 4:
                    cost += 0.5     
                else:
                    if num_events_on_day > 3:
                        cost += 0.2              
    return cost
