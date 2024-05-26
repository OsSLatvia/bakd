import copy
class Gene:
    def __init__(self, Event, timeslot=None, classroom=None, teacher=None):
        self.event = Event
        self.timeslot = timeslot
        self.classroom = classroom
        self.teacher = teacher
        self.students_in_event = 0
        for student_group in Event.student_groups:
            self.students_in_event = self.students_in_event + student_group.size

    def __str__(self):
        return f"event={self.event}, timeslot={self.timeslot}, classroom={self.classroom}, teacher={self.teacher})"
    def __repr__(self):
        return self.__str__()
    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        copied_gene = Gene(copy.deepcopy(self.event, memo))
        memo[id(self)] = copied_gene
        copied_gene.timeslot = copy.deepcopy(self.timeslot, memo)
        copied_gene.classroom = copy.deepcopy(self.classroom, memo)
        copied_gene.teacher = copy.deepcopy(self.teacher, memo)
        return copied_gene
    def __eq__(self, other):
        if isinstance(other, Gene):
            return (self.event == other.event and
                    self.timeslot == other.timeslot and
                    self.classroom == other.classroom and
                    self.teacher == other.teacher)
        return False
    def __hash__(self):
        return hash((self.event, self.timeslot, self.classroom, self.teacher))
    def to_dict(self):
        return {
            'event': self.event.to_dict(),
            'timeslot': self.timeslot.to_dict(),
            'classroom': self.classroom.to_dict(),
            'teacher': self.teacher.to_dict(),
            'students_in_event': self.students_in_event
        }
    # @classmethod
    # def from_dict(cls, data):
    #     event = Event.from_dict(data['event'])
    #     timeslot = Timeslot.from_dict(data['timeslot'])
    #     classroom = Classroom.from_dict(data['classroom'])
    #     teacher = Teacher.from_dict(data['teacher'])
    #     students_in_event = data['students_in_event']

    #     # Now create a new Gene instance with the reconstructed objects
    #     gene = cls(event=event, timeslot=timeslot, classroom=classroom, teacher=teacher)
    #     gene.students_in_event = students_in_event

    #     return gene
    # getters
    def get_event(self):
        return self.event
    def get_timeslot(self):
        return self.timeslot
    def get_classroom(self):
        return self.classroom
    def get_teacher(self):
        return self.teacher
    # setters
    def set_timeslot(self, timeslot):
        self.timeslot = timeslot
    def set_classroom(self, classroom):
        self.classroom = classroom
    def set_teacher(self, teacher):
        self.teacher = teacher
    # gene timeslot Hard constraint checks
    def is_gene_timeslot_valid (self, chromosome):
        if not self.is_teacher_timeslot_valid (chromosome):
            return False
        if not self.is_classroom_timeslot_valid (chromosome):
            return False
        if not self.is_timeslot_valid_for_student_group (chromosome):
            return False
        return True
    def is_teacher_timeslot_valid (self, chromosome): # pārbauda vai dotais pasniedzējs ir brīvs noteiktajā laikā, izpildīts nosacījums pasniedzejs nevar būt 2 nodarbībās vienlaikus
        for gene in chromosome:
            if self==gene:
                continue
            if gene.get_timeslot() == self.get_timeslot() and gene.get_teacher()==self.get_teacher():
                return False
        return True
    def is_classroom_timeslot_valid (self, chromosome): # pārbauda vai dotā telpa ir brīva noteiktajā laikā, izpildīts nosacījums telpā nevar būt 2 nodarbībās vienlaikus
        for gene in chromosome:
            if self==gene:
                continue
            if gene.get_timeslot() == self.get_timeslot() and gene.get_classroom()==self.get_classroom():
                return False
        return True
    def is_timeslot_valid_for_student_group(self, chromosome): #pārbaud vai studentu grupa brīva noteiktajā laikā, izpildīts nosacījums studenti nevar būt 2 nodarbībās vienlaikus
        current_event = self.get_event()
        timeslot=self.get_timeslot()
        # print (current_event)
        student_groups_for_event = current_event.get_student_groups() # paņem visas grubas kas ir šajā event
        for student_group in student_groups_for_event:  # no visu šī event grupu saraksta apstrādā katru grupu atsevišķi
            events_for_group = student_group.get_events() # katrai grupai ir event saraksts, kuru laiki jāpārbauda lai nepārklājas ar šobrīdējā gēna laiku
            for event in events_for_group:
                if current_event == event:
                    continue
                else:
                    event_Nr = event.get_event_ID()
                    if event_Nr < len(chromosome):
                        if timeslot == chromosome[event_Nr].get_timeslot(): # event.get_event_ID atgriež eventID kas sakrī ar kārtas numuru kur tas atrodas hromosomā
                            return False
                    else:
                        continue
                        # # print ("not all events in chromosome")
                        # print("++++++++++++++++++++")
                        # print (timeslot)
                        # print(self)
                        # if (event_Nr<len(chromosome)):
                        #     print (chromosome[event_Nr])
                        # if len(chromosome)>0:
                        #     print (chromosome[len(chromosome)-1])
                        
                        # return True #hromosomā ievietotie gēni derīgi, bet hromosomā nav visi events                 
        return  True
    # gene studentu grupas izmēra un telpas izmēra nosacījumu pārbaude
    def is_room_size_valid(self):
        students_in_event = 0
        for student_group in self.event.get_student_groups():
            students_in_event += student_group.get_size()
        if self.get_classroom().get_size()<students_in_event:
            return False
        return True
    def is_teacher_subject_valid(self):
        if self.get_event().get_subject() is None or self.get_teacher().get_subjects() is None:
            return True
        if not self.get_event().get_subject() in self.get_teacher().get_subjects() :
            return False
        return True