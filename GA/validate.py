from gene.gene import Gene

def is_valid(chromosome, gene):
    if not gene.is_gene_timeslot_valid(chromosome):
        return False
    if not gene.is_room_size_valid():
        return False
    if not gene.is_teacher_subject_valid():
        return False
    return True

def is_valid_chromosome(chromosome):
    # print(chromosome)
    for gene in chromosome:
        valid = is_valid(chromosome, gene)
        if not valid:
            return False
    return True