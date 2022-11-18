class Group:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = {subject.lower(): None for subject in subjects}

    def set_teacher(self, subject, teacher):
        self.subjects[subject] = teacher

    def __repr__(self):
        return f'Group ({self.name})'

    def __str__(self):
        return self.__repr__()
