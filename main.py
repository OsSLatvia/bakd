from gene.student_group import StudentGroup
from gene.event import Event
from gene.gene import Gene
from gene.components.classroom import Classroom
from gene.components.teacher import Teacher
from gene.components.timeslot import Timeslot
import random
from GA.initilize import create_initial_population
from GA.fitness import fitness_function
import global_data
from GA.crossover import crossover_function
from GA.validate import is_valid_chromosome
from GA.main_GA import genetic_algorithm
from GA.mutate import mutation_function

    
all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups

# initial_population = create_initial_population(200)  
# print ("fitness:")
# fitness, cost = fitness_function(initial_population[0])
# print(fitness)
# number_of_offsprings=2
# offsprings = crossover_function([initial_population[0], initial_population[1]], number_of_offsprings)
# print(fitness_function(offsprings[0]))
# # PyGAD configuration
# initial_population_size = 10
num_genes= len(all_events)
population_size = 500
generations = 10000

best_individual, best_fitness = genetic_algorithm(population_size, generations, fitness_function, crossover_function, mutation_function, create_initial_population)
print (best_individual)
print (best_fitness)


# print("Population:")
# for solution in ga_instance.population:
#     print(solution)