from person import Person


class Robber(Person):

    def __init__(self, outfit, weapon, *args, **kwargs):
        self.outfit = outfit
        self.weapon = weapon
        super.(Robber, self).__init__(*args, **kwargs)
