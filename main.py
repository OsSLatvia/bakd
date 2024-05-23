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
import pygad
import numpy as np

def fitness_func(ga_instance, solution, solution_idx):
    return fitness_function(solution)
def crossover_func(parents, offspring_size, ga_instance):
        return np.array(crossover_function(parents, offspring_size, ga_instance))

class CustomGA(pygad.GA):
    def __init__(self, create_initial_population, *args, **kwargs):
        self.create_initial_population = create_initial_population
        super().__init__(*args, **kwargs)
        # Initialize population as a numpy array
        self.population = np.array(self.create_initial_population(self.sol_per_pop))

    # def crossover_func(self, parents, offspring_size, ga_instance):
    #     print("crossover works")

    #     return crossover_function(parents, offspring_size, ga_instance)

    def mutation(self, offspring, ga_instance):
        print("mutation works")
        # No mutation logic for now since mutation_probability is set to 0
        return offspring

    def cal_pop_fitness(self):
        fitness = []
        for i, solution in enumerate(self.population):
            fitness.append(self.fitness_func(self, solution, i))  # Pass the instance of the GA class
        fitness_np = np.array(fitness)  # Convert fitness list to numpy array
        return fitness_np

    # def create_population(self):
    #     pop = self.create_initial_population(self.sol_per_pop)
    #     print(pop)
    #     return pop

    
all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups

# initial_population = create_initial_population(200)  
# print ("fitness:")
# print(fitness_function(initial_population[0]))
# offsprings = crossover_function([initial_population[0], initial_population[1]], [2], None)
# print(fitness_function(offsprings[0]))
# # PyGAD configuration
initial_population_size = 10
num_genes= len(all_events)
ga_instance = CustomGA(
    create_initial_population=create_initial_population,
    num_generations=20,                 # Number of generations
    num_parents_mating=10,                # Number of parents to select for mating
    fitness_func=fitness_func,           # Fitness function
    sol_per_pop=initial_population_size, # Population size
    num_genes=num_genes,                 # Number of genes in each solution
    gene_type=object,                    # Type of gene (set to object for custom class)
    parent_selection_type='tournament',  # Parent selection type
    crossover_probability=0.7,           # Crossover probability
    mutation_probability=0.0,           # Set mutation probability to 0
    crossover_type=crossover_func
)

ga_instance.run()

# Get the best solution
solution, solution_fitness, solution_idx = ga_instance.best_solution()

print("Best solution found:", solution)
print("Fitness value of the best solution:", solution_fitness)
# print("Population:")
# for solution in ga_instance.population:
#     print(solution)