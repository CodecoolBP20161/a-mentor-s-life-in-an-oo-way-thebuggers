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
        print("Someone just pressed the doorbell...")
        if isinstance(person, Pornstar):
            if int(self.energy_level) > 2:
                setattr(self, "energy_level", 1)
                print("""A famous pornstar stood in front of the office door, mentor {1} opened the door,
                /"Come to the other office lady {0}, I would like to perform a merge on you/", thats what
                mentor {1} said while he thought /"My second honeymoon is finally here/"
                """.format(person.name, self.nickname))
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return
            if int(self.energy_level) < 2:
                print("""A famous pornstar stood in front of the office door, mentor {1} opened the door,
                Im too tired for this shit, he said. Here take some money lady {0},
                what do you mean you dont accept bitcoin? said by mentor {1}""".format(person.name, self.nickname))
                setattr(self, "energy_level", 3)
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return
        if isinstance(person, Robber):
            if int(self.energy_level) < 2:
                print("""On a cloudy afternoon a dangerous robber broke into the office building, he managed to reach
                the first floor after he lied to the security officer by saying he is just a pole dancer. This was a
                daily routine in the office building located under Nagymezo 44, so there was no suspicion. The robber
                just stopped in front of a door with a codecool sign on it, pulled out his gun and rang the doorbell,
                mentor {1} opened the door, and before the robber even had a chance to say something, our great mentor
                smashed the door in the robbers face and shout /"Get the fuck out/" The robber was so embarrassed,
                he leaved immediately and gave up on his plans about invading codecool.""")
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return
            if int(self.energy_level) > 2:
                setattr(self, "energy_level", 1)
                print("""On a cloudy afternoon a dangerous robber broke into the office building, he managed to reach
                the first floor after he lied to the security officer by saying he is just a pole dancer. This was a
                daily routine in the office building located under Nagymezo 44, so there was no suspicion. The robber
                just stopped in front of a door with a codecool sign on it, pulled out his gun and rang the doorbell,
                mentor {1} opened the door, and before the robber even had a chance to say something, our great mentor
                grabbed his gun which accidentally got fired and the bullet hit the office precious projector.
                /"I will beat the sh*t out from you for this!/" shouted mentor {1}, then he punched the robber so
                hard that a mortal kombat fatality looks peanuts besides it.""")
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
                return

    def morning_routine(self, person):
        if int(person.energy_level) < 2:
            print("You look freakin tired! Here sniff some Coke! said by mentor {0}".format(self.nickname))
            setattr(person, "energy_level", 3)
            print("{0} energy level is now {1}".format(person.first_name, person.energy_level))
        if int(person.energy_level) > 2:
            print("Woo, calm down. This will do good for you! said by mentor {0}, and gave some weed to {1}".format(self.nickname, person.first_name))
            setattr(person, "energy_level", 2)
            print("{0} energy level is now {1}".format(person.first_name, person.energy_level))
