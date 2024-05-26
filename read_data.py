from gene.student_group import StudentGroup
from gene.event import Event
from gene.gene import Gene
from gene.components.classroom import Classroom
from gene.components.teacher import Teacher
from gene.components.timeslot import Timeslot
import random
import json
import tkinter as tk
from tkinter import ttk
import json
import matplotlib.pyplot as plt

# Function to plot the schedule
def plot_schedule(student_group_events):
    # Initialize grid with 5 days and 8 timeslots per day
    grid = [['' for _ in range(8)] for _ in range(5)]

    # Iterate through student group events and place them in the grid
    for student_group, genes in student_group_events.items():
        for gene in genes:
            # Determine day and timeslot indices using the Timeslot object
            day_index = gene.timeslot.day - 1  # Assuming Timeslot object has a 'day' attribute
            timeslot_index = gene.timeslot.time - 1  # Assuming Timeslot object has a 'time' attribute

            # Add event name to the grid
            # print("day_index", type(gene.event.event_ID))
            grid[day_index][timeslot_index] = gene.event.event_ID  # Assuming event has a 'name' attribute
    missing_event_value=-100
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '':
                grid[i][j] = missing_event_value
    # print("grid", grid, type(grid[0][0]))  
    # Plot the schedule grid
    plt.figure(figsize=(10, 6))
    # print ("next:")
    plt.imshow(grid, cmap='viridis', aspect='auto')
    # print ("next2:")
    # Add color bar for reference
    # plt.colorbar(label='Event ID')
    # Add labels for each square
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            event_id = grid[i][j]
            if event_id != missing_event_value:
                plt.text(j, i, "ID " + str(event_id), ha='center', va='center', color='white')

    # Add labels and legend
    plt.title('Event Schedule')
    plt.xlabel('Timeslots')
    plt.ylabel('Days')
    # plt.colorbar(label='Event')
    plt.xticks(range(8), [f'Timeslot {i+1}' for i in range(8)])
    plt.yticks(range(5), [f'Day {i+1}' for i in range(5)])
    plt.grid(visible=False)

    # Show plot
    plt.show()

def read_data_from_file(file_path):
    with open(file_path, 'r') as f:
        data_read = json.load(f)

    recreated_best_individuals = []
    for individual_data in data_read.get('best_individuals', []):
        event_data = individual_data['event']
        timeslot_data = individual_data['timeslot']
        classroom_data = individual_data['classroom']
        teacher_data = individual_data['teacher']
        students_in_event = individual_data['students_in_event']

        student_groups_data = event_data.get('student_group_list', [])
        student_groups = [StudentGroup(sg['id'], sg['size']) for sg in student_groups_data]

        event = Event(event_data['id'], student_groups)
        timeslot = Timeslot(timeslot_data['timeslot'], timeslot_data['timeslots_per_day'])
        classroom = Classroom(classroom_data['id'], classroom_data['capacity'])
        teacher = Teacher(teacher_data['id'])

        gene = Gene(event, timeslot, classroom, teacher)
        gene.students_in_event = students_in_event
        recreated_best_individuals.append(gene)

    return recreated_best_individuals

# Function to extract student group events
# Function to extract student group events
def extract_student_group_events(recreated_best_individuals):
    student_group_events = {}

    for gene in recreated_best_individuals:
        event = gene.event
        student_groups = event.student_groups

        for student_group in student_groups:
            student_group_id = str(student_group.group_ID)

            # Create an empty list if the student group is not already in the dictionary
            if student_group_id not in student_group_events:
                student_group_events[student_group_id] = []

            # Append the gene object to the list of events for the student group
            student_group_events[student_group_id].append(gene)

    return student_group_events


# Tkinter GUI function to update events list
def update_events_list(gene):  # No need to pass student_group_events as a parameter
    selected_student_group = student_group_combobox.get()
    if selected_student_group in student_group_events:
        events_for_selected_group = student_group_events[selected_student_group]
        # print("Events for Selected Group:", events_for_selected_group)  # Debugging print statement
        # print("type:", type(events_for_selected_group[0]))  # Debugging print statement
        try:
            events_listbox.delete(0, tk.END)
            events_listbox.insert(tk.END, *[str(event.event.event_ID) for event in events_for_selected_group])
            # Plot the schedule for the selected student group
            plot_schedule({selected_student_group: events_for_selected_group})
        except Exception as e:
            print("Error inserting events into Listbox:", e)  # Debugging print statement




# Read data from file and extract student group events
recreated_best_individuals = read_data_from_file("result.txt")
student_group_events = extract_student_group_events(recreated_best_individuals)

# Create a Tkinter window
window = tk.Tk()
window.title("Student Group Events")

# Create a Combobox to select student groups
student_group_combobox_label = ttk.Label(window, text="Select Student Group:")
student_group_combobox_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
student_group_combobox = ttk.Combobox(window, values=list(student_group_events.keys()))
student_group_combobox.grid(row=0, column=1, padx=5, pady=5)
student_group_combobox.bind("<<ComboboxSelected>>", update_events_list)

# Create a Listbox to display events
events_listbox_label = ttk.Label(window, text="Events for Selected Student Group:")
events_listbox_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
events_listbox = tk.Listbox(window)
events_listbox.grid(row=1, column=1, padx=5, pady=5)

# Create a button to close the window
close_button = ttk.Button(window, text="Close", command=window.quit)
close_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

# Run the Tkinter event loop
window.mainloop()