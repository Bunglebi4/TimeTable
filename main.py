from TimeTableGenerator.TimeTable import TimeTable

# time_table = Loader()
# time_table.load('input/input.json')
# time_table.make_lessons()

best_solve = None
cost = 10000

for i in range(1000):
    time_table = TimeTable('input/input.json')
    time_table.set_up()
    time_table.start_fill()
    time_table.costs()
    if cost > time_table.price:
        cost = time_table.price
        best_solve = time_table

best_solve.show_timetable()
print(cost)
