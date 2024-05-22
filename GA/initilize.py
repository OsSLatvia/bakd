import random
from gene.gene import Gene
import global_data
from GA.validate import is_valid_chromosome
from GA.validate import is_valid
all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups

def create_random_gene(event, all_timeslots, all_classrooms, all_teachers):
    gene = Gene(event)
    gene.timeslot = random.choice(all_timeslots)
    gene.classroom = random.choice(all_classrooms)
    gene.teacher = random.choice(all_teachers)
    return gene

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
def create_random_valid_gene(chromosome):

    gene=Gene(all_events[len(chromosome)])
    max_tries = 10
    for _ in range(max_tries):
        if not find_random_valid_timeslot(gene, chromosome):
            break
        else:
            if not find_random_valid_classroom(gene, chromosome):
                continue
            else:
                if not find_random_valid_teacher(gene, chromosome):
                    continue
                else:
                    return gene
    raise Exception("Failed to make valid gene") 

def create_chromosome():
    chromosome=[]
    for event in all_events:
        gene = create_random_valid_gene(chromosome)
        chromosome.append(gene)
    # print(is_valid_chromosome(chromosome))
    return chromosome

def create_initial_population(population_size):
    population = []
    while len(population)<(population_size):
        try:
            chromosome = create_chromosome()
            population.append(chromosome)
        except Exception as e:
            print("failed to create chromosome:", e)
            continue
    return population
