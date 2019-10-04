"""
МОДУЛЬ 2 - Владимир Трясцын
Год рождения А.С Пушкина = 1799
"""

pushkin_year = 1799

year_birth = input('Введите год рождения А.С Пушкина: ')
while not year_birth.isdigit():
    year_birth = input('Введите год рождения А.С Пушкина: ')

year_birth = int(year_birth)
if year_birth == pushkin_year:
    print("Верно")
    print("Год рождения А.С Пушкина = {}, Тип объекта = {}".format(year_birth, type(year_birth)))
else:
    print("Неверно")
