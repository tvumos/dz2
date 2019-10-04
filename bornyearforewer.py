"""
МОДУЛЬ 4 - Владимир Трясцын
Дата рождения А.С Пушкина = 26 мая 1799 г.
"""

pushkin_year = 1799
year_birth = None
while year_birth != pushkin_year:
    year_birth = input('Введите год рождения А.С Пушкина: ')
    while not year_birth.isdigit():
        year_birth = input('Введите год рождения А.С Пушкина: ')
    year_birth = int(year_birth)
print("Верно")

