from person import Person
from robber import Robber
from pornstar import Pornstar
import csv


class Mentor(Person):
    def __init__(self, nickname, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, csv_file):
        mentors = []
        with open(csv_file, newline='') as csvfile:
            all_mentors = csv.reader(csvfile)
            for row in all_mentors:
                name = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                mentors.append(name)
        return mentors

    def open_ringing_door(person):
        if isinstance(person, Pornstar):
            if self.energy_level < 2:
                print("Come to the other office Lady {0}, i will test your skills! -said by mentor {1}".format(person.first_name, self.nickname))
        pass
