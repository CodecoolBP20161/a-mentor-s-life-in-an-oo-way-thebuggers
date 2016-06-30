class Person(object):
    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, vegan, hungriness):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.energy_level = energy_level
        self.vegan = vegan
        self.hungriness = hungriness

    def death(self):
        if self.energy_level < 1:
            print("{0}'s' energy level dropped to zero and died.".format(self.first_name))
            return (self.first_name, self.last_name)

    def eat(self, food_object):
        print("It's lunchbreak time! Finally...\nAfter the holy trinity of git commands,{0} is on the way to eat.".format(self.first_name))
        if food_object.restaurant_status:
            if not self.vegan or (self.vegan and food_object.vegetarian):
                self.energy_level += 1
                print("{0} eats the {1} and goes back to work happily.".format(self.first_name, food_object.name))
            else:
                if int(self.hungriness) < 3:
                    self.energy_level -= 1
                    if self.death():
                        pass
                    else:
                        print("{0} goes back to work without eating.".format(self.first_name))
                else:
                    setattr(self, "energy_level", 15)
                    print("The only food around is {0}, but {1} is too hungry to be vegan this time.".format(
                        food_object.name, self.first_name))
        else:
            setattr(self, "energy_level", 0)
            if self.death():
                pass
            else:
                print("There's no {0}, so {1} goes back to work hungry.".format(food_object.name, self.first_name))
