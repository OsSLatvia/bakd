# from gene.student_group import StudentGroup
# from gene.event import Event
# from gene.gene import Gene
# from gene.components.classroom import Classroom
# from gene.components.teacher import Teacher
# from gene.components.timeslot import Timeslot
# import random
from GA.initilize import create_initial_population
from GA.fitness import fitness_function
import global_data
from GA.crossover import crossover_function
from GA.crossover import crossover_function2
from GA.crossover import crossover_function3
from GA.validate import is_valid_chromosome
from GA.main_GA import genetic_algorithm
from GA.mutate import hill_mutation_function
from GA.mutate import hill__multiple_gene_mutation_function
from GA.mutate import random_mutation_function
from GA.mutate  import combined__multiple_gene_mutation_function
from GA.mutate import random__multiple_gene_mutation_function
from GA.selection import roulet_select_parents
from GA.selection import tournament_select_parents
# import threading
# import multiprocessing
from multiprocessing import Process

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
generations = [60000, 60000, 60000, 60000]
population_size = [50, 200, 50, 200]
parent_count = [2, 2, 2, 2]
selection_function = [tournament_select_parents, tournament_select_parents, roulet_select_parents, roulet_select_parents]
mutation_func = [combined__multiple_gene_mutation_function, combined__multiple_gene_mutation_function, combined__multiple_gene_mutation_function, combined__multiple_gene_mutation_function]
crossover_func = [crossover_function3, crossover_function3, crossover_function3, crossover_function3]
hillclimbing_probability=[0.0, 0.0, 0.0, 0.00]
crossover_probability=[0.75, 0.75, 0.75, 0.75]
mutation_probability=[0.15, 0.15, 0.05, 0.05]
# best_individual, best_fitness = genetic_algorithm("", population_size, generations, fitness_function, crossover_function, mutation_function, create_initial_population)
# thread1 = threading.Thread(target=genetic_algorithm, args=("thread1:", hillclimbing_probability[0], crossover_probability[0],  mutation_probability[0], population_size[0], generations[0], parent_count[0], selection_function[0], fitness_function, crossover_func[0], mutation_func[0], create_initial_population))
# thread2 = threading.Thread(target=genetic_algorithm, args=("thread2:", hillclimbing_probability[1], crossover_probability[1],  mutation_probability[1], population_size[1], generations[1], parent_count[1], selection_function[1], fitness_function, crossover_func[1], mutation_func[1], create_initial_population))
# thread3 = threading.Thread(target=genetic_algorithm, args=("thread3:", hillclimbing_probability[2], crossover_probability[2],  mutation_probability[2], population_size[2], generations[2], parent_count[2], selection_function[2], fitness_function, crossover_func[2], mutation_func[2], create_initial_population))
# thread4 = threading.Thread(target=genetic_algorithm, args=("thread4:", hillclimbing_probability[3], crossover_probability[3],  mutation_probability[3], population_size[3], generations[3], parent_count[3], selection_function[3], fitness_function, crossover_func[3], mutation_func[3], create_initial_population))

# thread1.start()
# # thread2.start() 
# thread3.start() 
# thread4.start() 
if __name__ == '__main__':
    process1 = Process(target=genetic_algorithm, args=("process1:", hillclimbing_probability[0], crossover_probability[0], mutation_probability[0], population_size[0], generations[0], parent_count[0], selection_function[0], fitness_function, crossover_func[0], mutation_func[0], create_initial_population))
    process2 = Process(target=genetic_algorithm, args=("process2:", hillclimbing_probability[1], crossover_probability[1], mutation_probability[1], population_size[1], generations[1], parent_count[1], selection_function[1], fitness_function, crossover_func[1], mutation_func[1], create_initial_population))
    process3 = Process(target=genetic_algorithm, args=("process3:", hillclimbing_probability[2], crossover_probability[2], mutation_probability[2], population_size[2], generations[2], parent_count[2], selection_function[2], fitness_function, crossover_func[2], mutation_func[2], create_initial_population))
    process4 = Process(target=genetic_algorithm, args=("process4:", hillclimbing_probability[3], crossover_probability[3], mutation_probability[3], population_size[3], generations[3], parent_count[3], selection_function[3], fitness_function, crossover_func[3], mutation_func[3], create_initial_population))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
    # print (best_individual)
    # print (best_fitness)


    # print("Population:")
    # for solution in ga_instance.population:
    #     print(solution)