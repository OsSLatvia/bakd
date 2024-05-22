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
all_events = global_data.all_events
all_teachers = global_data.all_teachers
all_classrooms = global_data.all_classrooms
all_timeslots = global_data.all_timeslots
student_groups = global_data.student_groups

gene1= Gene(all_events[0])
gene2= Gene(all_events[1])
classroom1 = Classroom(13, 9)
teacher1 = Teacher  ("Janis")
teacher2 = Teacher  ("Karlis")
timeslot1 = Timeslot (1)
timeslot2 = Timeslot (2)
gene1.set_classroom(all_classrooms[0])
gene1.set_teacher(all_teachers[0])
gene1.set_timeslot(timeslot1)
gene2.set_classroom(all_classrooms[0])
gene2.set_teacher(all_teachers[1])
gene2.set_timeslot(timeslot2)
chromosome = [gene1, gene2]
print(chromosome)
print(gene1.is_gene_timeslot_valid(chromosome))
print(gene2.is_room_size_valid())
print(gene2)
print("-----> ", all_timeslots)
print("________________")
initial_population = create_initial_population(200)  
# print (initial_population)
print ("fitness:")
print(fitness_function(initial_population[0]))
print(fitness_function(initial_population[1]))
print(fitness_function(initial_population[2]))
print(fitness_function(initial_population[3]))
offsprings = crossover_function([initial_population[0], initial_population[1]], [2], None)
# print("_--------------------------------")
# print (offsprings[0])
# print("_--------------------------------")
# print (initial_population[0])
# print("_--------------------------------")
print(fitness_function(offsprings[0]))
# for pop in initial_population:
#     print(is_valid_chromosome(pop))
