import random
from GA.fitness import fitness_function
import global_data
from gene.gene import Gene

all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups


def hill_mutation_function(chromosome):
    random_gene = random.choice(chromosome)
    set_best_timeslot(random_gene, chromosome) 
    return chromosome
def hill__multiple_gene_mutation_function(chromosome):
    for i in range(len(chromosome)//10): #mutation notiek 10% no gēniem hromosomā
        random_gene = random.choice(chromosome)
        set_best_timeslot(random_gene, chromosome)
    return chromosome
def random_mutation_function(chromosome):
    random_gene = random.choice(chromosome)
    mutation_options = [find_random_valid_timeslot, find_random_valid_classroom, find_random_valid_teacher]
    random.choice(mutation_options)(random_gene, chromosome)   # set_best_timeslot(random_gene, chromosome)
    return chromosome
def random__multiple_gene_mutation_function(chromosome):
    for i in range(len(chromosome)//10): #mutation notiek 10% no gēniem hromosomā
        random_gene = random.choice(chromosome)
        mutation_options = [find_random_valid_timeslot, find_random_valid_classroom, find_random_valid_teacher]
        random.choice(mutation_options)(random_gene, chromosome)   # set_best_timeslot(random_gene, chromosome)
    return chromosome
def combined__multiple_gene_mutation_function(chromosome):
    for i in range(len(chromosome)//10): #mutation notiek 10% no gēniem hromosomā
        random_gene = random.choice(chromosome)
        before_mutation_hash = hash(random_gene)
        mutation_options = [find_random_valid_classroom, find_random_valid_teacher]
        did_gene_change = random.choice(mutation_options)(random_gene, chromosome)
        # print (did_gene_change)
        if did_gene_change:  # set_best_timeslot(random_gene, chromosome)
            set_best_timeslot(random_gene, chromosome) 
            # print("mutation ok")
        else:
            pass
            # print("failed mutation")
    return chromosome
def mutation_function_gene(chromosome, gene):
    set_best_timeslot(gene, chromosome)
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
    original_classroom = gene.classroom
    classroom_Indexes = random.sample(range(0, len(all_classrooms)), len(all_classrooms))
    for classroom_Index in classroom_Indexes:
        classroom_object = all_classrooms[classroom_Index] #šo dara tikai lai ņemtu komponenti random secībā
        if (classroom_object==original_classroom):
            continue
        gene.set_classroom(classroom_object)
        if gene.is_classroom_timeslot_valid(chromosome) and gene.is_room_size_valid():
            return True
    gene.classroom = original_classroom
    return False #return True ja atrod derīgu classroom ko uzstāda gēnam, ja nav derīgu classroom return false
def find_random_valid_teacher(gene, chromosome):
    original_teacher = gene.teacher
    teacher_Indexes = random.sample(range(0, len(all_teachers)), len(all_teachers))
    for teacher_Index in teacher_Indexes:
        teacher_object = all_teachers[teacher_Index] #šo dara tikai lai ņemtu komponenti random secībā
        if (teacher_object==teacher_object):
            continue
        gene.set_teacher(teacher_object)
        if gene.is_teacher_timeslot_valid(chromosome) and gene.is_teacher_subject_valid():
            return True
    gene.teacher = original_teacher
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
        chromosome[gene.event.event_ID]=gene
        fitness, cost = fitness_function(chromosome)
        if fitness > best_fitnes:
            best_fitnes = fitness
            best_timeslot = timeslot
    gene.set_timeslot(best_timeslot)

