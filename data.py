class TimeTable:
    def __init__(self):
        ...

    @staticmethod
    def set_up(num_of_columns):
        """
        Sets up the timetable matrix and dictionary that stores free fields from matrix.
        :param num_of_columns: number of classrooms
        :return: matrix, free
        """
        w, h = num_of_columns, 36  # 6 (workdays) * 6 (work hours) = 36
        matrix = [[None for x in range(w)] for y in range(h)]
        free = []

        # initialise free dict as all the fields from matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                free.append((i, j))
        return matrix, free

    @staticmethod
    def show_timetable(matrix):
        """
        Prints timetable matrix.
        """
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
        hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        hours = ['8:00', '9:50', '11:40', '13:10', '15:30', '17:20']

        # print heading for classrooms
        for i in range(len(matrix[0])):
            if i == 0:
                print('{:23s} C{:6s}'.format('', '0'), end='')
            else:
                print('C{:6s}'.format(str(i)), end='')
        print()

        d_cnt = 0
        h_cnt = 0
        for i in range(len(matrix)):
            day = days[d_cnt]
            hour = hours[h_cnt]
            print('{:12s} {:6s} ->  '.format(day, hour), end='')
            for j in range(len(matrix[i])):
                print('{:6s} '.format(str(matrix[i][j])), end='')
            print()
            h_cnt += 1
            if h_cnt == 6:
                h_cnt = 0
                d_cnt += 1
                print()


matrix, free = TimeTable.set_up(15)
TimeTable.show_timetable(matrix)
