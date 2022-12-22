import json
from random import choice
from .models.Lesson import Lesson
from .models.Teacher import Teacher
from .models.Group import Group
from .models.Auditorium import Auditorium


class Loader:
    def __init__(self):
        self.total_lessons = []
        self.groups = []
        self.teachers = []
        self.auditorium = []
        self.all_subjects = []

    def load(self, file_name):
        with open(file_name, encoding='utf-8') as file:
            data = json.loads(file.read())
            self.groups = [Group(group["Name"],
                                 group["Subjects"]) for group in data["Group"]]
            self.teachers = [Teacher(teacher["Name"],
                                     teacher["Subjects"],
                                     teacher['Workload']) for teacher in data["Teacher"]]
            self.auditorium = [Auditorium(auditorium["Number"],
                                          auditorium["Type"]) for auditorium in data["Auditorium"]]
            self.all_subjects = list(set(sum([teacher["Subjects"] for teacher in data["Teacher"]], [])))

    def make_lessons(self):
        for group in self.groups:
            for lesson in group.subjects:
                if not group.subjects.get(lesson):
                    available_teachers = list(filter(lambda teacher: teacher.is_available(lesson), self.teachers))
                    if available_teachers:
                        selected_teacher = choice(available_teachers)
                        group.set_teacher(lesson, selected_teacher)
                        selected_teacher.set_lesson(lesson, group)
                        self.total_lessons.append(Lesson(group, lesson, selected_teacher))
                    else:
                        raise f'{group} has not available teachers for {lesson}'
        print('All of lesson was created')

