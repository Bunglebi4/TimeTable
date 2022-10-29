class Auditorium:
    def __init__(self, number, type_of_auditorium):
        self.type_of_auditorium = type_of_auditorium
        self.number = number
        self.is_empty = False

    def fill(self):
        self.is_empty = True

    def __repr__(self):
        return f"Аудитория №{self.number}, тип: {self.type_of_auditorium}"

    def __str__(self):
        return self.__repr__()