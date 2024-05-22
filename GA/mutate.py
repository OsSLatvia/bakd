import random
def mutation_function(offspring, ga_instance):
    for chromosome in offspring:
        gene_to_mutate = random.choice(chromosome)
        gene_to_mutate.timeslot = random.choice(timeslots)
        gene_to_mutate.classroom = random.choice(classrooms)
        gene_to_mutate.teacher = random.choice(teachers)
    return offspring