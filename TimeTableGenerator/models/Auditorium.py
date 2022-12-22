class Auditorium:
    def __init__(self, name, auditorium_type):
        self.number = name
        self.auditorium_type = auditorium_type

    def is_correct_auditorium(self, lesson):
        lesson_type = lesson.subject.split()[-1]
        return self.auditorium_type.lower() == lesson_type.lower()

    def __repr__(self):
        return f'{self.number}({self.auditorium_type})'

    def __str__(self):
        return self.__repr__()

    def __format__(self, format_spec):
        return str(self).__format__(format_spec)
