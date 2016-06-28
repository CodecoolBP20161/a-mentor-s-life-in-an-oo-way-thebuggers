from person import Person


class Pornstar(Person):

    def __init__(self, sex_toy, *args, **kwargs):
        self.sex_toy = sex_toy
        super.(Pornstar, self).__init__(*args, **kwargs)
