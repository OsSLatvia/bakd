import random

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