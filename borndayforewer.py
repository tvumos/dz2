"""
МОДУЛЬ 5 - Владимир Трясцын
Дата рождения А.С Пушкина = 26 мая 1799 г.
"""

pushkin_year = 1799
pushkin_day = 27

year_birth = None
while year_birth != pushkin_year:
    year_birth = input('Введите год рождения А.С Пушкина: ')
    while not year_birth.isdigit():
        year_birth = input('Введите год рождения А.С Пушкина: ')
    year_birth = int(year_birth)

day_birth = None
while day_birth != pushkin_day:
    day_birth = input('Введите день рождения А.С Пушкина: ')
    while not day_birth.isdigit():
        day_birth = input('Введите день рождения А.С Пушкина: ')
    day_birth = int(day_birth)

print("Верно")