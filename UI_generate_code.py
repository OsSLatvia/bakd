import tkinter as tk
from generate_data import generate_teachers
from generate_data import generate_classrooms
from generate_data import generate_events
from generate_data import generate_student_groups
from generate_data import store_data_to_file
from tkinter import messagebox

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.number_of_events_label = tk.Label(self, text="Number of Events:")
        self.number_of_events_label.pack(side="top")

        self.number_of_events_entry = tk.Entry(self)
        self.number_of_events_entry.pack(side="top")

        self.number_of_groups_label = tk.Label(self, text="Number of Groups:")
        self.number_of_groups_label.pack(side="top")

        self.number_of_groups_entry = tk.Entry(self)
        self.number_of_groups_entry.pack(side="top")

        self.days_label = tk.Label(self, text="Number of Days:")
        self.days_label.pack(side="top")

        self.days_entry = tk.Entry(self)
        self.days_entry.pack(side="top")

        self.timeslots_label = tk.Label(self, text="Timeslots per Day:")
        self.timeslots_label.pack(side="top")

        self.timeslots_entry = tk.Entry(self)
        self.timeslots_entry.pack(side="top")

        self.number_of_classrooms_label = tk.Label(self, text="Number of Classrooms:")
        self.number_of_classrooms_label.pack(side="top")

        self.number_of_classrooms_entry = tk.Entry(self)
        self.number_of_classrooms_entry.pack(side="top")

        self.number_of_teachers_label = tk.Label(self, text="Number of Teachers:")
        self.number_of_teachers_label.pack(side="top")

        self.number_of_teachers_entry = tk.Entry(self)
        self.number_of_teachers_entry.pack(side="top")

        self.generate_button = tk.Button(self)
        self.generate_button["text"] = "Generate Data"
        self.generate_button["command"] = self.generate_data
        self.generate_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def generate_data(self):
        try:
            number_of_events = int(self.number_of_events_entry.get())
            number_of_groups = int(self.number_of_groups_entry.get())
            days = int(self.days_entry.get())
            timeslots = int(self.timeslots_entry.get())
            number_of_classrooms = int(self.number_of_classrooms_entry.get())
            number_of_teachers = int(self.number_of_teachers_entry.get())

            # Generate data here
            teachers = generate_teachers(number_of_teachers)
            classrooms = generate_classrooms(number_of_classrooms)
            student_groups = generate_student_groups(number_of_groups)
            events = generate_events(number_of_events, student_groups)

            # Store data to file
            store_data_to_file("data.txt", teachers, classrooms, student_groups, events)

            messagebox.showinfo("Success", "Data generated and stored successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()