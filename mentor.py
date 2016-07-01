from person import Person
from robber import Robber
from pornstar import Pornstar
import csv


class Mentor(Person):
    def __init__(self, nickname, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, csv_file):   # creates and returns a list of mentors
        print("Mentors are initialized from CSV.")
        cls.mentors = []
        with open(csv_file, newline='') as csvfile:
            all_mentors = csv.reader(csvfile)
            for row in all_mentors:
                name = Mentor(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                cls.mentors.append(name)
        return cls.mentors

    def open_ringing_door(self, person):
        print("Someone just pressed the doorbell...Who could it possibly be? :O")
        input()
        if isinstance(person, Pornstar):
            if int(self.energy_level) > 2:
                setattr(self, "energy_level", 1)
                print("""
A famous pornstar stood in front of the office door with {2} in her hand, mentor {1} opened the door:
"Come to the other office lady {0}, I would like to perform a merge on you",
 that's what mentor {1} said while he thought:
"My second honeymoon is finally here"
                """.format(person.name, self.nickname, person.sex_toy))
                input()
                print("***after a while***\nMentor {0}'s energy level is now {1}.".format(
                    self.nickname, int(self.energy_level)))
            elif int(self.energy_level) < 2:
                print("""
A famous pornstar stood in front of the office door with {2} in her hand,
mentor {1} opened the door:
"Im too tired for this shit"-he said. "Here take some money lady {0}!"\n
"What do you mean you dont accept bitcoin?"
Mentor {1}'s happiness level would have dropped down...if he had one.
                """.format(person.name, self.nickname, person.sex_toy))
                setattr(self, "energy_level", 3)
                input()
                print("Mentor {0} energy level is now {1}.".format(self.nickname, int(self.energy_level)))
        if isinstance(person, Robber):
            if int(self.energy_level) < 2:
                print("""
On a cloudy afternoon a dangerous robber broke into the office building, he managed to reach
the first floor after he lied to the security officer by saying he is just a pole dancer. This was a
daily routine in the office building located under Nagymezo 44, so there was no suspicion. The robber
just stopped in front of a door with a codecool sign on it, pulled out his gun and rang the doorbell,
mentor {0} opened the door, and before the robber even had a chance to say something, our great mentor
smashed the door in the robbers face and shout /"Get the fuck out/" The robber was so embarrassed,
he left immediately and gave up on his plans about invading codecool.
                """.format(self.nickname))
                print("Mentor {0}'s energy level is now {1}.".format(self.nickname, self.energy_level))
            if int(self.energy_level) > 2:
                setattr(self, "energy_level", 1)
                print("""
On a cloudy afternoon a dangerous robber broke into the office building, he managed to reach
the first floor after he lied to the security officer by saying he is just a pole dancer. This was a
daily routine in the office building located under Nagymezo 44, so there was no suspicion. The robber
just stopped in front of a door with a codecool sign on it, pulled out his gun and rang the doorbell,
mentor {0} opened the door, and before the robber even had a chance to say something, our great mentor
grabbed his gun which accidentally got fired and the bullet hit the office precious projector.
/"I will beat the sh*t out from you for this!/" shouted mentor {0}, then he punched the robber so
hard that a mortal kombat fatality looks peanuts besides it.
                """.format(self.nickname))
                print("Mentor {0}'s energy level is now {1}.".format(self.nickname, self.energy_level))

    def morning_routine(self, person):
        print("How's student {0} {1}'s energy level in the morning?\nIt's on {2}.".format(
            person.first_name, person.last_name, person.energy_level))
        input()
        if int(person.energy_level) <= 2:
            print("Mentor {0} to {1}:You look freakin tired! Here, sniff some Coke!".format(
                    self.nickname, person.first_name))
            setattr(person, "energy_level", 1024)
            print("{0}'s energy level is now {1}. {0} túltolta".format(person.first_name, person.energy_level))
        elif int(person.energy_level) > 2:
            print("""
Woo, calm down, you have some extra energy.
This'll be good for you!-said mentor {0}, while passing a joint to {1}.""".format(self.nickname, person.first_name))
            setattr(person, "energy_level", 2)
            input()
            print("{0}'s energy level is now {1}.".format(person.first_name, person.energy_level))
