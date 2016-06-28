from person import Person


class Student(Person):
    def __init__(self, knowledge_level, *args, *kwargs):
        super().__init__(*args, *kwargs)
        self.knowledge_level = knowledge_level

    def ending_routine(mentor):
        pass

    @classmethod
    def create_by_csv(csv_file):
        pass
