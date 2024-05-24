import random
from GA.validate import is_valid
import global_data
from GA.fitness import fitness_function

all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups

def repair_gene(chromosome, gene):
    # print("Repairing gene: ", gene)
    # Attempts to fix an invalid gene by changing its attributes
    attempts = 0
    max_attempts = 1
    gene_valid = is_valid(chromosome, gene)
    while ((not gene_valid) and (attempts < max_attempts)): 
        if set_best_timeslot(gene, chromosome):
        # gene.timeslot = random.find_random_valid_timeslot(all_timeslots)
        # gene.classroom = random.choice(all_classrooms)
        # gene.teacher = random.choice(all_teachers)
            return True
        else:
            attempts += 1
    # print("cant repairing")
    return False
def find_random_valid_timeslot(gene, chromosome):
    timeslot_Indexes = random.sample(range(0, len(all_timeslots)), len(all_timeslots))
    for timeslot_Index in timeslot_Indexes:
        timeslot_object = all_timeslots[timeslot_Index] #šo dara tikai lai ņemtu komponenti random secībā
        gene.set_timeslot(timeslot_object)
        if gene.is_timeslot_valid_for_student_group(chromosome):
            return True
    return False #return True ja atrod derīgu timeslot ko uzstāda gēnam, ja nav derīgu timeslot return false 

def find_all_valid_timeslot(gene, chromosome):
    valid_timeslots = []
    for timeslot in all_timeslots:
        gene.set_timeslot(timeslot)
        if gene.is_timeslot_valid_for_student_group(chromosome):
            valid_timeslots.append(timeslot)
    return valid_timeslots 
def set_best_timeslot(gene, chromosome):
    valid_timeslots = find_all_valid_timeslot(gene, chromosome)
    if len(valid_timeslots)==0:
        return False
    else:
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
        return True
