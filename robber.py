class Robber(object):

    def __init__(self, name, outfit, weapon, *args, **kwargs):
        self.name = name
        self.outfit = outfit
        self.weapon = weapon
        super(Robber, self).__init__(*args, **kwargs)
