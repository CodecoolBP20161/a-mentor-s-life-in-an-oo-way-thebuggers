from person import Person
import csv


class Student(Person):
    def __init__(self, knowledge_level, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.knowledge_level = knowledge_level


    @classmethod
    def create_by_csv(cls, csv_file):
        cls.students = []
        with open(csv_file, newline='') as csvfile:
            all_students = csv.reader(csvfile)
            for row in all_students:
                name = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                cls.students.append(name)
        return cls.students

    def ending_routine(self, mentor):
        if self.energy_level == 1:
            print("""Our great mentor is low on energy and his mood lacks of happiness, so he decided to make things
            a little more exciting by announcing a self evaluation opportunity to the students, and by self evaluation,
            he meant a mandatory exam. He thought that would be nice towards codecoolers if the eligible level would be
            set to 98%. /"Im such a sweetheart/" he said, as he was astonished by his own generosity""")
        if self.energy_level == 3:
            print("""Our great mentor felt a great amount of energy in himself, /"Its time to give/" he thought.
            So he decided to buy beer for the entire class, he later realized the consequences of his generosity as his
            purse became way more lighter than before. But this was a day to give, not to take.""")
        else:
            print("""Our great mentor has reached the proper energy level, which made him realize the fact that no one gives
            a flying fuck about codecool. /"My work is done here/" thats what he said to himself while he was
            walking out of the office building, located under Nagymezo street 44""")
