from .Loader import Loader
from random import choice


class TimeTable:
    def __init__(self, input_file):
        self.matrix = None
        self.free = []
        self.used = []
        self.price = 0
        self.loader = Loader()
        self.loader.load(input_file)
        self.overlay = 0

        self.best_score = 500

    def set_up(self):
        w, h = len(self.loader.auditorium), 36  # 6 (workdays) * 6 (work hours) = 36
        self.matrix = [[None for x in range(w)] for y in range(h)]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.free.append((i, j))

    def start_fill(self):
        self.loader.make_lessons()
        for i, lesson in enumerate(self.loader.total_lessons):
            x, y = choice(list(self.get_available_coord(lesson)))
            self.free.remove((x, y))
            self.used.append((x, y))
            self.matrix[x][y] = lesson

    def get_available_coord(self, lesson):
        available_auditorium = [j for j, el in enumerate(self.loader.auditorium)
                                if el.is_correct_auditorium(lesson)]

        available_time = []
        for k, one_time in enumerate(self.matrix):
            groups = [j.group for j in one_time if j is not None]
            teachers = [j.teacher for j in one_time if j is not None]

            if lesson.group not in groups and lesson.teacher not in teachers:
                available_time.append(k)

        coords = filter(lambda coord: coord[1] in available_auditorium, self.free)
        coords = filter(lambda coord: coord[0] in available_time, coords)
        return coords

    def show_timetable(self):
        for i, lesson in enumerate(self.loader.total_lessons):
            print(i, lesson)

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

    def costs(self):
        days = []
        self.price = 0
        self.overlay = 0
        for start_of_day in range(0, 31, 6):
            day = []
            day_array_of_groups = []
            for i in range(start_of_day, start_of_day + 6):
                day.append(self.matrix[i])
                for j in range(len(self.loader.auditorium)):
                    if self.matrix[i][j] is not None:
                        day_array_of_groups.append(self.matrix[i][j].group)
            days.append(day)
            day.clear()
            for group in self.loader.groups:
                if 3 < day_array_of_groups.count(group) or day_array_of_groups.count(group) > 5:
                    self.price += 5

        # тест на количество физры в день
        sport_lessons = {}
        for count, day in enumerate(days):
            sport_lessons[count] = [lessons for x in day for lessons in x if lessons is not None]
        for key in sport_lessons:
            sport_lessons[key] = list(filter(lambda x: ("физкультура" in x.subject), list(sport_lessons[key])))
            for group in self.loader.groups:
                cnt = 0
                for lesson in sport_lessons[key]:
                    if lesson.group == group:
                        cnt += 1
                        if cnt == 2:
                            self.price += 2
        # тест на окна и наложения
        groups_with_pairs = {}
        for groups in self.loader.groups:
            for count, pairs in enumerate(self.matrix):
                for lesson in pairs:
                    if lesson is not None and lesson.group == groups:
                        groups_with_pairs.setdefault(groups, []).append([count, lesson])

        for key in groups_with_pairs:
            cnt = 0
            for i in range(len(list(groups_with_pairs[key])) - 1):
                if list(groups_with_pairs[key])[i][0] // 6 == list(groups_with_pairs[key])[i + 1][0] // 6 and (
                        list(groups_with_pairs[key])[i + 1][0] - list(groups_with_pairs[key])[i][0]) == 0:
                    self.overlay += 1
                if list(groups_with_pairs[key])[i][0] // 6 == list(groups_with_pairs[key])[i + 1][0] // 6 and (
                        list(groups_with_pairs[key])[i + 1][0] - list(groups_with_pairs[key])[i][0]) == 1:
                    cnt += 1
                    if cnt > 1:
                        self.price += 2
                if list(groups_with_pairs[key])[i][0] // 6 == list(groups_with_pairs[key])[i + 1][0] // 6 and (
                        list(groups_with_pairs[key])[i + 1][0] - list(groups_with_pairs[key])[i][0]) > 1:
                    self.price += 3
        lesson_dict = {}
        for key in groups_with_pairs:
            for subj in self.loader.all_subjects:
                lesson_dict[subj.lower()] = 0
            for lessons in groups_with_pairs[key]:
                lesson_dict[lessons[1].subject] = lessons[0]
            for subj in self.loader.all_subjects:
                if subj.lower()[-1] == "л":
                    lab = None
                    lecture = subj.lower()
                    practice = subj.lower()[0:-2] + " п"
                    if subj.lower() + "б" in self.loader.all_subjects:
                        lab = subj.lower() + "б"
                    if lesson_dict[lecture] < lesson_dict[practice]:
                        if lab is not None:
                            if lesson_dict[lab] > lesson_dict[practice]:
                                continue
                            else:
                                self.price += 1
                    else:
                        self.price += 1

    def make_mutation(self):
        old_x, old_y = choice(self.used)
        lesson = self.matrix[old_x][old_y]

        new_x, new_y = choice(list(self.get_available_coord(lesson)))
        self.matrix[old_x][old_y] = None
        self.matrix[new_x][new_y] = lesson
        self.costs()
        if self.price < self.best_score and self.overlay == 0:
            self.best_score = self.price
            self.used.remove((old_x, old_y))
            self.used.append((new_x, new_y))
            self.free.remove((new_x, new_y))
            self.free.append((old_x, old_y))
        else:
            self.matrix[old_x][old_y] = lesson
            self.matrix[new_x][new_y] = None


