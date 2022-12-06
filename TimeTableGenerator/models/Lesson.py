from .Group import Group
from .Teacher import Teacher


class Lesson:
    def __init__(self, group: Group, subject: str, teacher: Teacher):
        self.group = group
        self.subject = subject
        self.teacher = teacher

    def __repr__(self):
        return f'{self.group} {self.subject} {self.teacher}'

    def __str__(self):
        return str(self.__repr__())
