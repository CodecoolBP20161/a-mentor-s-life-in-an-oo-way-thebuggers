# from student.py import Student


class Person(object):
    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, vegan, hungriness):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = int(year_of_birth)
        self.gender = gender
        self.energy_level = int(energy_level)
        self.vegan = vegan
        self.hungriness = int(hungriness)

    def death(self):
        if self.energy_level < 1:
            # Student.remove_dead(self.first_name, self.last_name)
            return(True)

    def eat(self, food_object):
        print("""It's lunchbreak time! Finally...\nAfter the holy trinity of git \
commands, {0} is on the way to eat.""".format(self.first_name))
        if food_object.restaurant_status:
            if not self.vegan or (self.vegan and food_object.vegetarian):
                self.energy_level += 1
                print("""{0} eats some {1} and goes back to work with enough energy to survive the day.\
\n{0}'s energy level is now: {2}.""".format(self.first_name, food_object.name, self.energy_level))
            else:
                if self.hungriness < 3:
                    self.energy_level -= 1
                    if self.death():
                        print("""The only food around is {0}, but {1} won't eat that. {1}'s' energy level \
dropped to zero and died.\nLest we forget!""".format(food_object.name, self.first_name))
                        pass
                    else:
                        print("""{0} goes back to work without eating.\n{0}'s \
energy level is now: {1}.""".format(self.first_name, self.energy_level))
                else:
                    self.energy_level = 15  # for testing, originally it's '+= 1'
                    print("The only food around is {0}, but {1}'s hungriness \
level is too high ({2}) to be vegan this time.".format(food_object.name, self.first_name, self.hungriness))
        else:
            self.energy_level = 0  # for testing, originally it's '-= 1'
            if self.death():
                print("""There's no {0}, {1}'s' energy level dropped to zero and died.\
\nLest we forget!""".format(food_object.name, self.first_name))
                pass
            else:
                print("""There's no {0}, so {1} goes back to work hungry.\n{1}'s energy \
level is now: {2}.""".format(food_object.name, self.first_name, self.energy_level))
