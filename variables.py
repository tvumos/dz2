"""
МОДУЛЬ 1 - Владимир Трясцын
Объект: Параллелепипед - parallelepiped
"""

""" Наименование объекта"""
name = "Параллелепипед"

""" Длина основания, см"""
base_length = 5.7

""" Ширина основания, см"""
base_width = 3.4

""" Высота объекта, см"""
height = 7

""" Площадь основания, см2"""
base_square = base_length * base_width

""" Объём обекта, см3"""
volume = base_square * height

""" Пустотелый объект"""
is_hollow = True

""" Прозрачный объект"""
is_transparent = False

# Вывод результатов
print("Наименование объекта:", name, "Тип объекта:", type(name))
print("Длина основания, (см) = {:0.2f}, Тип объекта = {}".format(base_length, type(base_length)))
print("Ширина основания, (см) = {:0.2f}, Тип объекта = {}".format(base_width, type(base_width)))
print("Высота объекта, (см) = {:0.2f}, Тип объекта = {}".format(height, type(height)))
print("Площадь основания, (см2) = {:0.2f}, Тип объекта = {}".format(base_square, type(base_square)))
print("Объём обект, (см2) = {:0.2f}, Тип объекта = {}".format(volume, type(volume)))
print("Пустотелый объект? = {}, Тип объекта = {}".format(is_hollow, type(is_hollow)))
print("Прозрачный объект? = {}, Тип объекта = {}".format(is_transparent, type(is_transparent)))



