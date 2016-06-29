from person import Person
import csv


class Student(Person):
    def __init__(self, knowledge_level, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self.knowledge_level = knowledge_level

    def ending_routine(mentor):
        if mentor.energy_level = 1:
            print("alcohol")
        if person.energy_level = 2:
            print("weed")
        if mentor.energy_level = 3:
            print("cocain")
        else:
            print("fuck off")

    @classmethod
    def create_by_csv(self, csv_file):
        students = []
        with open(csv_file, newline='') as csvfile:
            all_students = csv.reader(csvfile)
            for row in all_students:
                name = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                students.append(name)
        return students
