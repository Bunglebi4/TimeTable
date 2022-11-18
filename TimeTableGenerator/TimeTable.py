from .Loader import Loader
from random import choice

class TimeTable:
    def __init__(self, input_file):
        self.matrix = None
        self.free = []

        self.loader = Loader()
        self.loader.load(input_file)

    def set_up(self):
        w, h = len(self.loader.auditorium), 36  # 6 (workdays) * 6 (work hours) = 36
        self.matrix = [[None for x in range(w)] for y in range(h)]

        # initialise free dict as all the fields from matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.free.append((i, j))

    def start_fill(self):
        self.loader.make_lessons()
        for i, lesson in enumerate(self.loader.total_lessons):
            available_auditorium = [i for i, el in enumerate(self.loader.auditorium)
                                    if el.is_correct_auditorium(lesson)]
            coords = filter(lambda coord: coord[1] in available_auditorium, self.free)
            x, y = choice(list(coords))
            self.free.remove((x, y))
            self.matrix[x][y] = i
            print(i, lesson)



    def show_timetable(self):
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        hours = ['8:00', '9:50', '11:40', '13:10', '15:30', '17:20']

        # print heading for classrooms
        for i in range(len(self.matrix[0])):
            if i == 0:
                print('{:23s} {:12s}'.format('', self.loader.auditorium[i]), end='')
            else:
                print('{:12s}'.format(self.loader.auditorium[i]), end='')
        print()

        day_counter = 0
        lesson_counter = 0
        for i in range(len(self.matrix)):
            day = days[day_counter]
            hour = hours[lesson_counter]
            print('{:12s} {:6s} ->  '.format(day, hour), end='')
            for j in range(len(self.matrix[i])):
                print('{:11s} '.format(str(self.matrix[i][j])), end='')
            print()
            lesson_counter += 1
            if lesson_counter == 6:
                lesson_counter = 0
                day_counter += 1
                print()
