class Teacher:
    def __init__(self, name, subjects, workload):
        self.name = name
        self.subjects = {subject.lower(): [] for subject in subjects}
        self.workload = workload

    def is_available(self, subject):
        return subject.lower() in self.subjects and self.workload > 0

    def set_lesson(self, subject, group):
        self.subjects[subject].append(group)
        self.workload -= 1

    def __repr__(self):
        return f'Teacher ({self.name})'

    def __str__(self):
        return self.__repr__()
