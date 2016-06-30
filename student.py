from person import Person
import csv


class Student(Person):
    def __init__(self, knowledge_level, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.knowledge_level = knowledge_level


    @classmethod
    def create_by_csv(cls, csv_file):
        print("Mentors are initialized from CSV")
        cls.students = []
        with open(csv_file, newline='') as csvfile:
            all_students = csv.reader(csvfile)
            for row in all_students:
                name = Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                cls.students.append(name)
        return cls.students

    def ending_routine(self, mentor):
        if self.energy_level == 1:
            print("alcohol")
        if self.energy_level == 2:
            print("weed")
        if self.energy_level == 3:
            print("cocain")
        else:
            print("fuck off")
