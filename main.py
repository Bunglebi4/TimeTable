from TimeTableGenerator.TimeTable import TimeTable
from TimeTableGenerator.models import *

# time_table = Loader()
# time_table.load('input/input.json')
# time_table.make_lessons()

time_table = TimeTable('input/input.json')
time_table.set_up()
time_table.start_fill()
time_table.show_timetable()

time_table.costs()

print(time_table.price)
