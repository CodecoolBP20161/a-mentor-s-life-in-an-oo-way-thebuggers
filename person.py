class Person:
    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, vegan, hungriness):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.energy_level = energy_level
        self.vegan = vegan
        self.hungriness = hungriness

    def eat(self, food_object):
        if self.vegan:
            pass
