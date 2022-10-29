import json
from group import Group
from teacher import Teacher
from auditorium import Auditorium
from pprint import pprint


class Sheduler:
    def __init__(self):
        self.list_of_groups = []
        self.list_of_teacher = []
        self.list_of_auditorium =[]

    def load(self, file_name):
        with open(file_name, encoding='utf-8') as file:
            data = json.loads(file.read())
            self.list_of_groups = [Group(group["Name"], group["List_of_subjects"]) for group in data["Group"]]
            self.list_of_teachers = [Teacher(teacher["Name"], teacher["Subjects"]) for teacher in data["Teacher"]]
            self.list_of_auditorium = [Auditorium(cls["Number"], cls["Type"]) for cls in data["Auditorium"]]

    def make_lessons(self):
        for group in self.list_of_groups:
            for subject in group.subjects:
                pair = make_lesson(subjects, self.list_of_teacher)

#load("Test_input_2.json")