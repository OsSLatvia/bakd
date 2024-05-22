import random
from GA.validate import is_valid
import global_data

all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups

def repair_gene(chromosome, gene):
    # Example repair logic
    # Attempts to fix an invalid gene by changing its attributes
    attempts = 0
    max_attempts = 10
    while not is_valid(chromosome, gene) and attempts < max_attempts: 
        gene.timeslot = random.choice(all_timeslots)
        gene.classroom = random.choice(all_classrooms)
        gene.teacher = random.choice(all_teachers)
        attempts += 1
    return is_valid(chromosome, gene)
def find_random_valid_timeslot(gene, chromosome, all_timeslots):
    timeslot_Indexes = random.sample(range(0, len(all_timeslots)), len(all_timeslots))
    for timeslot_Index in timeslot_Indexes:
        timeslot_object = all_timeslots[timeslot_Index] #šo dara tikai lai ņemtu komponenti random secībā
        gene.set_timeslot(timeslot_object)
        if gene.is_timeslot_valid_for_student_group(chromosome):
            return True
    return False #return True ja atrod derīgu timeslot ko uzstāda gēnam, ja nav derīgu timeslot return false 