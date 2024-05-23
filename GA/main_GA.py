import random
import global_data
import math
import gc
from GA.validate import is_valid_chromosome 

crossover_probability = global_data.crossover_probability
mutation_probability = global_data.mutation_probability
number_of_offsprings = global_data.number_of_offsprings
number_of_parents = global_data.number_of_parents

def genetic_algorithm(population_size, generations, fitness_function, crossover_function, mutation_function, initialization_function):
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
        random_number = random.random()
        
        while len(next_generation)<population_size:
            parents = roulet_select_parents(population, fitness_values, number_of_parents)
            if random_number < crossover_probability:
                offsprings = crossover_function(parents, number_of_offsprings)
            else:
                offsprings = parents

            # Perform mutation on the new individuals
            for individual in offsprings:
                # print(is_valid_chromosome(individual))
                
                if random.random() < mutation_probability:  
                    # print("befoe mutation: ", fitness_function(individual))
                    individual = mutation_function(individual)
                    # print("after mutation: ", fitness_function(individual))
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
        
        print ("generation: ", generation, "best fitness: ", round(best_fitness,6), "avarage fitness: ", round(avarage_fitness, 6), "best_cost: ", best_cost)
        # print ("avarage fitness: ", avarage_fitness)
        # print ("best_cost: ", best_cost)
        if math.isclose(avarage_fitness, best_fitness, rel_tol=1e-6):
            break
        

    # Run the algorithm for the specified number of generations
    return best_individual, best_fitness


def tournament_select_parents(population, fitness_values, number_of_parents):
    parents = []
    for _ in range(number_of_parents):
        tournament = random.sample(population, k=5)  # Select a random subset of 5 individuals
        max_fitness = max(fitness_values[i] for i in range(len(tournament)))
        parents.append(tournament[fitness_values.index(max_fitness)])
    return parents

def roulet_select_parents(population, fitness_values, number_of_parents):
    # Calculate the total fitness
    total_fitness = sum(fitness_values)
    
    # Calculate the relative fitness (probability) of each individual
    relative_fitness = [f / total_fitness for f in fitness_values]
    
    # Cumulative probability distribution
    cumulative_probabilities = []
    cumulative_sum = 0
    for rf in relative_fitness:
        cumulative_sum += rf
        cumulative_probabilities.append(cumulative_sum)
    
    # Select parents
    parents = []
    for _ in range(number_of_parents):
        r = random.random()
        for i, individual in enumerate(population):
            if r <= cumulative_probabilities[i]:
                parents.append(individual)
                break
    
    return parents

