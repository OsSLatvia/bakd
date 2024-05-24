import random
import global_data
import math
import gc
from GA.mutate import mutation_function_gene
from GA.validate import is_valid_chromosome 
from gene.gene import Gene
from collections import Counter

# crossover_probability = global_data.crossover_probability
# mutation_probability = global_data.mutation_probability
number_of_offsprings = global_data.number_of_offsprings
# # number_of_parents = global_data.number_of_parents
# hillclimbing_probability = global_data.hillclimbing_probability
def calculate_diversity(population):
    diversity = 0
    num_genes = len(population[0])
    for i in range(num_genes):
        gene_variants = Counter(ind[i] for ind in population)
        diversity += len(gene_variants)
    return diversity / num_genes

def genetic_algorithm(print_msg, hillclimbing_probability, crossover_probability,  mutation_probability, population_size, generations, parent_count, selection_function, fitness_function, crossover_function, mutation_function, initialization_function):
    """
    Main Genetic Algorithm method

    Parameters:
    population_size (int): The size of the population
    generations (int): The number of generations to run the algorithm
    fitness_function (function): The fitness function to evaluate individuals
    crossover_function (function): The crossover function to generate new individuals
    mutation_function (function): The mutation function to introduce randomness
    initialization_function (function): The initialization function to create the initial population

    Returns:
    best_individual (list): The best individual found by the algorithm
    best_fitness (float): The best fitness value found by the algorithm
    """
    # Initialize the population
    population = initialization_function(population_size)

    # Evaluate the initial population
    fitness_values = []
    # Initialize the best individual and fitness value
    best_individual = population[0]
    best_fitness, best_cost = fitness_function(population[0])
    best_fitness_index = 0
    cost_values = []
    for individual in population:
        fitness, cost = fitness_function(individual)
        fitness_values.append(fitness)
        cost_values.append(cost)
        if (best_fitness<fitness):
            best_fitness=fitness
            best_cost = cost
            best_fitness_index=fitness_values.index(fitness)
            best_individual = population[best_fitness_index]
    # Run the algorithm for the specified number of generations
    for generation in range(generations):
        # Select parents for crossover
        gc.collect()
        
        
        # Perform crossover to generate new individuals
        offsprings = []
        next_generation=[]
        next_generation.append(population[best_fitness_index]) #izmanto elitism, vienmēr patur labāko indivīdu
        next_generation.append(mutation_function(copy_chromosome(population[best_fitness_index])))
        # next_generation.append(apply_hillclimbing(copy_chromosome(population[best_fitness_index])))
        random_number = random.random()
        
        while len(next_generation)<population_size:
            parents = selection_function(population, fitness_values, parent_count)
            if random_number < crossover_probability:
                offsprings = crossover_function(parents, number_of_offsprings)
            else:
                offsprings = parents

            # Perform mutation on the new individuals
            for individual in offsprings:
                # print(is_valid_chromosome(individual))
                
                if random.random() < mutation_probability:  
                    individual = mutation_function(copy_chromosome(individual))
                if random.random() < hillclimbing_probability: 
                    individual = apply_hillclimbing(copy_chromosome(individual))
                if len(next_generation)<population_size:
                    next_generation.append(individual)
                else:
                    break
        population = next_generation
        # Evaluate the new population
        fitness_values = []
        # Initialize the best individual and fitness value
        best_individual = population[0]
        best_fitness, best_cost = fitness_function(population[0])
        best_fitness_index = 0
        cost_values = []
        for individual in population:
            fitness, cost = fitness_function(individual)
            fitness_values.append(fitness)
            cost_values.append(cost)
            if (best_fitness<fitness):
                best_fitness=fitness
                best_cost = cost
                best_fitness_index=fitness_values.index(fitness)
                best_individual = population[best_fitness_index]
        # print ("generation: ", generation )
        # print ("best individual: ", best_individual)
        avarage_fitness=sum(fitness_values)/len(fitness_values)
        
        print (print_msg, " generation: ", generation, "best fitness: ", round(best_fitness,6), "avarage fitness: ", round(avarage_fitness, 6), "best_cost: ", best_cost)
        # print ("avarage fitness: ", avarage_fitness)
        # print ("best_cost: ", best_cost)
        diversity = calculate_diversity(population)
        print(f"Generation {generation}: Diversity {diversity}")
        if math.isclose(avarage_fitness, best_fitness, rel_tol=1e-6):
            break
        

    # Run the algorithm for the specified number of generations
    return best_individual, best_fitness
def copy_chromosome(chromosome):
    chromosome_copy=[]
    for gene in chromosome:
        gene_copy = Gene(gene.event)
        gene_copy.set_classroom(gene.classroom)
        gene_copy.set_teacher(gene.teacher)
        gene_copy.set_timeslot(gene.timeslot)
        chromosome_copy.append(gene_copy)
    return chromosome_copy
def apply_hillclimbing(chromosome):
    for gene in chromosome:
        mutation_function_gene(chromosome, gene)
    # print("hillclimb")
    return chromosome


