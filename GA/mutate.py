import random
from GA.fitness import fitness_function
import global_data
import copy

all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups


def mutation_function(chromosome):
    random_gene = copy.deepcopy(random.choice(chromosome))
    set_best_timeslot(random_gene, chromosome)
    # mutation_options = [find_random_valid_timeslot, find_random_valid_classroom, find_random_valid_teacher]
    # random.choice(mutation_options)(random_gene, chromosome)   # set_best_timeslot(random_gene, chromosome)
    # for chromosome in offspring:
    #     gene_to_mutate = random.choice(chromosome)
    #     gene_to_mutate.timeslot = random.choice(timeslots)
    #     gene_to_mutate.classroom = random.choice(classrooms)
    #     gene_to_mutate.teacher = random.choice(teachers)
    chromosome[random_gene.event.event_ID]=random_gene
    return chromosome
def find_random_valid_timeslot(gene, chromosome):
    timeslot_Indexes = random.sample(range(0, len(all_timeslots)), len(all_timeslots))
    for timeslot_Index in timeslot_Indexes:
        timeslot_object = all_timeslots[timeslot_Index] #šo dara tikai lai ņemtu komponenti random secībā
        gene.set_timeslot(timeslot_object)
        if gene.is_timeslot_valid_for_student_group(chromosome):
            return True
    return False #return True ja atrod derīgu timeslot ko uzstāda gēnam, ja nav derīgu timeslot return false 
def find_random_valid_classroom(gene, chromosome):
    classroom_Indexes = random.sample(range(0, len(all_classrooms)), len(all_classrooms))
    for classroom_Index in classroom_Indexes:
        classroom_object = all_classrooms[classroom_Index] #šo dara tikai lai ņemtu komponenti random secībā
        gene.set_classroom(classroom_object)
        if gene.is_classroom_timeslot_valid(chromosome) and gene.is_room_size_valid():
            return True
    return False #return True ja atrod derīgu classroom ko uzstāda gēnam, ja nav derīgu classroom return false
def find_random_valid_teacher(gene, chromosome):
    teacher_Indexes = random.sample(range(0, len(all_teachers)), len(all_teachers))
    for teacher_Index in teacher_Indexes:
        teacher_object = all_teachers[teacher_Index] #šo dara tikai lai ņemtu komponenti random secībā
        gene.set_teacher(teacher_object)
        if gene.is_teacher_timeslot_valid(chromosome) and gene.is_teacher_subject_valid():
            return True
    return False #return True ja atrod derīgu classroom ko uzstāda gēnam, ja nav derīgu classroom return false 
def find_all_valid_timeslot(gene, chromosome):
    valid_timeslots = []
    for timeslot in all_timeslots:
        gene.set_timeslot(timeslot)
        if gene.is_timeslot_valid_for_student_group(chromosome):
            valid_timeslots.append(timeslot)
    return valid_timeslots 
def set_best_timeslot(gene, chromosome):
    valid_timeslots = find_all_valid_timeslot(gene, chromosome)
    best_timeslot = random.choice(valid_timeslots)
    gene.set_timeslot(best_timeslot)
    best_fitnes, best_cost = fitness_function(chromosome)
    for timeslot in valid_timeslots:
        gene.set_timeslot(timeslot)
        fitness, cost = fitness_function(chromosome)
        if fitness > best_fitnes:
            best_fitnes = fitness
            best_timeslot = timeslot
        gene.set_timeslot(best_timeslot)

