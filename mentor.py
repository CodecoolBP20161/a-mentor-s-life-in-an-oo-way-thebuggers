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
        print("Mentors are initialized from CSV")
        cls.mentors = []
        with open(csv_file, newline='') as csvfile:
            all_mentors = csv.reader(csvfile)
            for row in all_mentors:
                name = Mentor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                cls.mentors.append(name)
        return cls.mentors

    def open_ringing_door(self, person):
        if isinstance(person, Pornstar):
            if int(self.energy_level) > 2:
                setattr(self, "energy_level", 1)
                print("Come to the other office lady {0}, i will test your skills, in the other office! -said by mentor {1}".format(person.name, self.nickname))
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return
            if int(self.energy_level) < 2:
                print("I'am too tired for this shit. Here take some money lady {0}, said by mentor {1}".format(person.name, self.nickname))
                setattr(self, "energy_level", 3)
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return
        if isinstance(person, Robber):
            if int(self.energy_level) < 2:
                print("Ohh noh, get the fuck out")
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return
            if int(self.energy_level) > 2:
                setattr(self, "energy_level", 1)
                print("I will beat the sh*t about you!")
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return

    def morning_routine(self, person):
        if int(person.energy_level) < 2:
            print("You look freakin tired! Here take some Coke! said by mentor {0}".format(self.nickname))
            setattr(person, "energy_level", 3)
            print("{0} energy level is now {1}".format(person.first_name, person.energy_level))
        if int(person.energy_level) > 2:
            print("Woo, calm down. This will good for you! said by mentor {0}, and give some weed to {1}".format(self.nickname, person.first_name))
            setattr(person, "energy_level", 2)
            print("{0} energy level is now {1}".format(person.first_name, person.energy_level))
