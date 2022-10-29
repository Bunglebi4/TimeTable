class Group:
    def __init__(self, number, subjects):
        self.number = number
        self.subjects = subjects
        self.min_num_of_lessons = 2
        self.max_num_of_lessons = 5
        self.curr_lessons = None

    ''' 
    метод показывает, можем ли мы поставить группе еще одну пару, в случае успеха возвращает True
    '''
    def add_lesson(self, lesson):
        if len(self.curr_lessons) < self.max_num_of_lessons:
            self.curr_lessons += lesson
            return True
        else:
            return False

    def __repr__(self):
        return f'Номер группы: {self.number} \n Предметы, которые нужно провести {self.subjects} \n Проведенные пары: {self.curr_lessons} '

    def __str__(self):
        return self.__repr__()