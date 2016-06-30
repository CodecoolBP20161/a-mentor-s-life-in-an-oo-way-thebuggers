from mentor import Mentor
from student import Student
import random


class CodecoolClass:

    def __init__(self, location, year, mentors, students):  # instance constructor
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):    # returning an instance with these parameters
        cls.location = "Budapest"
        cls.year = 2016
        cls.mentors = Mentor.create_by_csv('data/mentors.csv')
        cls.students = Student.create_by_csv('data/students.csv')
        return CodecoolClass(cls.location, cls.year, cls.mentors, cls.students)

    def find_mentor_by_full_name(self, full_name):  # returns a Mentor object from the list
        name = full_name.split()
        for i, j in enumerate(self.mentors):
            if j.last_name == name[1]:
                return self.mentors[i]

    def find_student_by_full_name(self, full_name):  # returns a Student object from the list
        name = full_name.split()
        for i, j in enumerate(self.students):
            if j.last_name == name[1]:
                return self.students[i]

    def get_random_student(self):
        random_index = random.randint(1, len(self.students))
        full_name = "{0} {1}".format(self.students[random_index].first_name, self.students[random_index].last_name)
        return full_name
