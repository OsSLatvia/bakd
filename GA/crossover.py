import random
from GA.validate import is_valid
from GA.validate import is_valid_chromosome
from GA.repair import repair_gene
import copy
from GA.initilize import create_random_valid_gene
from GA.main_GA import copy_chromosome

def crossover_function2(parents, number_of_offsprings):
    offspring = []
    num_parents = len(parents)
    max_tries = 3
    tries=0
    while len(offspring) < number_of_offsprings and tries<max_tries:
        tries=tries+1
        parent1_idx = random.randint(0, num_parents - 1)
        parent2_idx = random.randint(0, num_parents - 1)

        parent1 = copy_chromosome(parents[parent1_idx])
        parent2 = copy_chromosome(parents[parent2_idx])
        
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
        if offspring2_valid and len(offspring) < number_of_offsprings:
            offspring.append(offspring2)

    return offspring

def crossover_function(parents, number_of_offsprings):
    offspring = []
    num_parents = len(parents)
    while len(offspring) < number_of_offsprings:

        parent1_idx = random.randint(0, num_parents - 1)
        parent2_idx = random.randint(0, num_parents - 1)

        parent1 = parents[parent1_idx]
        parent2 = parents[parent2_idx]
        offspring1=[]
        offspring1.append(parent1[0])
        for _ in range(1, len(parent1)):
            gene=None
            if random.random() < 0.5:
                gene=parent1[_]
                if is_valid(offspring1, gene):
                    offspring1.append(gene)
                else:
                    gene=parent2[_]
                    if is_valid(offspring1, gene):
                        offspring1.append(gene)
            else:
                gene=parent2[_]
                if is_valid(offspring1, gene):
                    offspring1.append(gene)
                else:
                    gene=parent1[_]
                    if is_valid(offspring1, gene):
                        offspring1.append(gene)
            if not len(offspring1)>_:
                # print ("creating random valid gene ")
                gene=create_random_valid_gene(offspring1)
                offspring1.append(gene)
        # crossover_point = random.randint(1, len(parent1) - 1)
        # offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        # offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

        # Validate and repair offspring1
        # offspring1_valid = all(is_valid(offspring1, gene) for gene in offspring1)
        
        # # Validate and repair offspring2
        # offspring2_valid = all(is_valid(offspring2, gene) for gene in offspring2) or all(repair_gene(offspring2, gene) for gene in offspring2)
        
        # Add valid offspring to the list
        # print(is_valid_chromosome(offspring1))
        # if offspring1_valid:
        #     offspring.append(offspring1)
        offspring.append(offspring1)
    return offspring
def crossover_function3(parents, number_of_offsprings):
    offspring = []
    num_parents = len(parents)
    tries = 0
    max_tries = 10
    while len(offspring) < number_of_offsprings and tries<max_tries:
            
            failed_to_find_good_gene = False
            parent1_idx = random.randint(0, num_parents - 1)
            parent2_idx = random.randint(0, num_parents - 1)

            parent1 = parents[parent1_idx]
            parent2 = parents[parent2_idx]
            offspring1=[]
            offspring1.append(parent1[0])
            for _ in range(1, len(parent1)):
                gene=None
                if parent1[_]==parent2[_]:
                    gene=parent1[_]
                    if is_valid(offspring1, gene):
                        offspring1.append(gene)
                else:
                    if random.random() < 0.5:
                        gene=parent1[_]
                        if is_valid(offspring1, gene):
                            offspring1.append(gene)
                        else:
                            gene=parent2[_]
                            if is_valid(offspring1, gene):
                                offspring1.append(gene)
                    else:
                        gene=parent2[_]
                        if is_valid(offspring1, gene):
                            offspring1.append(gene)
                        else:
                            gene=parent1[_]
                            if is_valid(offspring1, gene):
                                offspring1.append(gene)
                if not len(offspring1)>_:
                    # print ("creating random valid gene ")
                    for parent in parents:
                        if parent1[_]!=parent[_]:
                            gene=parent[_]
                            if is_valid(offspring1, gene):
                                offspring1.append(gene)
                                break
                    if not len(offspring1)>_:
                        failed_to_find_good_gene = True
                        break
            if failed_to_find_good_gene:
                tries+=1
                # print ("tries ",tries)
                continue
                    # gene=create_random_valid_gene(offspring1)
                    # offspring1.append(gene)
            # crossover_point = random.randint(1, len(parent1) - 1)
            # offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
            # offspring2 = parent2[:crossover_point] + parent1[crossover_point:]

            # Validate and repair offspring1
            # offspring1_valid = all(is_valid(offspring1, gene) for gene in offspring1)
            
            # # Validate and repair offspring2
            # offspring2_valid = all(is_valid(offspring2, gene) for gene in offspring2) or all(repair_gene(offspring2, gene) for gene in offspring2)
            
            # Add valid offspring to the list
            # print(is_valid_chromosome(offspring1))
            # if offspring1_valid:
            #     offspring.append(offspring1)
            offspring.append(offspring1)
            # print("len ",len(offspring))
            tries = 0
    return offspring


