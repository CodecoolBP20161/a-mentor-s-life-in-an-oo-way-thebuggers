from person import Person


class Mentor(Person):
    def __init__(self, nickname, *args, *kwargs):
        super().__init__(*args, *kwargs)
        self.nickname = nickname

    @classmethod
    def create_by_csv(csv_file):
        pass

    def open_ringing_door(person):
        pass
