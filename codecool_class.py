from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        cls.location = "Budapest"
        cls.year = 2016
        cls.mentors = Mentor.create_by_csv(cls, 'data/mentors.csv')
        cls.students = "sanyi"
        return CodecoolClass(cls.location, cls.year, cls.mentors, cls.students)

    def find_student_by_full_name(self, full_name):
        mentor_name = ("%s %s" % (self.mentors[0], self.mentors[1]))
