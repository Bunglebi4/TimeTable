from TimeTableGenerator.TimeTable import TimeTable
import matplotlib.pyplot as plt

time_table = TimeTable('input/input.json')
time_table.loader.make_lessons()
time_table.set_up()
time_table.start_fill()
score = []
iterations = 10000
for i in range(iterations):
    if i % 100 == 0:
        print(f"{i}/{iterations}")
    time_table.make_mutation()
    score.append(time_table.best_score)

plt.plot(score)
plt.xlabel('Iteration')
plt.ylabel('TimeTable cost')
plt.show()
