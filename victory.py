"""
МОДУЛЬ 6 - Владимир Трясцын

А.С Пушкина = 26 мая 1799 г
М.Ю. Лермонтова = 15 октября 1814
Николай Васильевич Гоголья = 31 марта 1809
Лев Николаевич Толстого = 9 сентября 1828
Фёдор Миха́йлович Достоевский = 11 ноября 1821
Михаил Михайлович Жванецкий = 6 марта 1934
Борис Натанович Стругацкий = 15 апреля 1933
Аркадий Натанович Стругацкий = 28 августа 1925
Андре́й Арсе́ньевич Тарко́вский = 4 апреля 1932
"""

fio = ["Александра Сергеевича Пушкина", "Михаила Юрьевича Лермонтова", "Николайя Васильевича Гоголья",
       "Льва Николаевича Толстого", "Фёдора Миха́йловича Достоевского", "Михаила Михайловича Жванецкого",
       "Бориса Натановича Стругацкого", "Аркадия Натановича Стругацкого", "Андрея Арсеньевича Тарковского"]
correct = [1799, 1814, 1809, 1828, 1821, 1934, 1933, 1925, 1932]
good_answer = 0
bad_answer = 0
index = 0

while True:
    # Удобней использовать цикл for в данном примере, но так как пока используем while, то
    while index < len(fio):
        index += 1
        year_birth = input('Введите год рождения {}: '.format(fio[index - 1]))
        if not year_birth.isdigit():
            bad_answer += 1
            continue
        year_birth = int(year_birth)
        if year_birth == correct[index - 1]:
            good_answer += 1
        else:
            bad_answer += 1

    # Вывод результатов викторины
    print("Количество правильных ответов = {}".format(good_answer))
    print("Количество ошибок = {}".format(bad_answer))
    print("Процент правильных ответов = {:0.2f} %".format(good_answer * 100 / len(correct)))
    print("Процент ошибочных ответов = {:0.2f} %".format(bad_answer * 100 / len(correct)))

    # Вы хотите повторить викторину?
    next_answer = input('Вы хотите повторить викторину? (Да/Нет): ')
    while not next_answer.upper() in ["ДА", "НЕТ"]:
        next_answer = input('Повторите Ваш ответ. Вы хотите повторить викторину? (Да/Нет): ')
    if next_answer.upper() == "ДА":
        good_answer = 0
        bad_answer = 0
        index = 0
    else:
        break

