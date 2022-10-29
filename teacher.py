"""
У преподавателя должны быть предмет с указанием типа, группы у которых он может вести и количество нагрузки
"""

class Teacher:
    def __init__(self, name, subjects):
        self.name = name
        self.subject = subjects
        self.groups = None
        self.workload = None

    def get_values(self):

        arr = [" ФИО:", self.name, "\n", "Предмет: ", self.subject,"\n" ,"Работает с группами: ", self.groups, "\n", "Осталось нагрузки: ", self.workload, "часов"]
        return arr

    def not_too_much(self):
        """
        буль функшн есть ли у препода еще время
        """
        if self.workload > 0:
            return True

    def teaches_a_lesson(self):
        """
        пара отнимает у препода очко:)) нагрузки
        :return:
        """
        if self.not_too_much():
            self.workload-=1
            return self
        return "Преподаватель устал"

    def is_group_suitable(self, group):
        """
        На вход дается группа
        проверяет, может ли препод вести у этой группы.
        возвращает True/False
        """
        if group in self.groups: return True
        else: return False

    def __repr__(self):
        return f' ФИО преподавателя - {self.name} \n Он ведет {self.subject} у групп {self.groups} \n Он(а) еще может провести {self.workload} пар'


    def __str__(self):
        return self.__repr__()
