from person import Person
from robber import Robber
from pornstar import Pornstar
import csv


class Mentor(Person):
    def __init__(self, nickname, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)
        self.nickname = nickname

    def create_by_csv(self, csv_file):
        mentors = []
        with open(csv_file, newline='') as csvfile:
            all_mentors = csv.reader(csvfile)
            for row in all_mentors:
                name = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                mentors.append(name)
        return mentors

    def open_ringing_door(self, person):
        if isinstance(person, Pornstar):
            if self.energy_level < 2:
                print("Come to the other office Lady {0}, i will test your skills! -said by mentor {1}".format(person.first_name, self.nickname))
            if self.energy_level > 2:
                print("Here take some money lady {0}, said by mmentor {1}".format(person.first_name, self.first_name))
        if isinstance(person, Robber):
            if self.energy_level < 2:
                print("Ohh noh, get the fuck out")
            if self.energy_level > 2:
                print("I will beat the shit about you!")

    def morning_routine(self, person):
        if person.energy_level < 2:
            print("Take here some cocain")
        if person.energy_level > 2:
            print("Take some weed")
