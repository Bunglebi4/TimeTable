from teacher import *
from group import *

teacher1 = Teacher("Аббаев Абба Аббаевич", "Математический анализ Л", [1301, 1302, 1303, 1304, 1305, 2301, 2302, 2303, 2304, 2305], 15)
group_1305 = Group(1305, ["Матанализ Л",
                           "Матанализ П",
                           "АиГ Л",
                           "АиГ П",
                           "Физика Л",
                           "Физика ЛБ",
                           "Физика П"], 2, 5, [])


print(teacher1, '\n', teacher1.is_group_suitable(1310))
print()
print(group_1305)
