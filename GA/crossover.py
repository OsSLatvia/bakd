import random
from GA.validate import is_valid
from GA.repair import repair_gene
import copy

def crossover_function(parents, offspring_size, ga_instance):
    offspring = []
    num_parents = len(parents)
    # tries=0
    while len(offspring) < offspring_size[0]:
        # tries = tries+1
        # print (tries)
        parent1_idx = random.randint(0, num_parents - 1)
        parent2_idx = random.randint(0, num_parents - 1)

        parent1 = copy.deepcopy(parents[parent1_idx])
        parent2 = copy.deepcopy(parents[parent2_idx])
        
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
        
        # Validate and repair offspring1
        offspring1_valid = all(is_valid(offspring1, gene) for gene in offspring1) or all(repair_gene(offspring1, gene) for gene in offspring1)
        
        # Validate and repair offspring2
        offspring2_valid = all(is_valid(offspring2, gene) for gene in offspring2) or all(repair_gene(offspring2, gene) for gene in offspring2)
        
        # Add valid offspring to the list
        if offspring1_valid:
            offspring.append(offspring1)
        if offspring2_valid and len(offspring) < offspring_size[0]:
            offspring.append(offspring2)

    return offspring