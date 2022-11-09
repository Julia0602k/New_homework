# 1. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот
# месяц принадлежит (зима, весна, лето или осень). Номер месяца вводить с клавиатуры

# Решение
def season(a):
    for k, v in dict1.items():
        if a in v:
            return k
dict1 = {'зима': ('1', '2', '12'), 'весна': ('3', '4', '5'), 'лето': ('6', '7', '8'), 'осень': ('9', '10', '11')}
start = 1
while start:
    b = input('Введите номер месяца (от 1 до 12): ')
    for v in dict1.values():
        if b in v:
            print(f'''Месяц принадлежит сезону "{season(b)}"''')
            start = 0


# # Вариант 2 (без проверки)
# def season(a):
#     for k, v in dict1.items():
#         if a in v:
#             return k
# dict1 = {'зима': ('1', '2', '12'), 'весна': ('3', '4', '5'), 'лето': ('6', '7', '8'), 'осень': ('9', '10', '11')}
# print(season(input('Введите номер месяца (от 1 до 12): ')))

# Вариант 3
# def season():
#     a = input('Введите номер месяца (от 1 до 12): ')
#     while not a in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
#         a = input('Ошибка! Введите номер месяца (от 1 до 12): ')
#     a = int(a)
#     if a in [1, 2, 12]:
#         s = 'зима'
#     elif a in [3, 4, 5]:
#         s = 'весна'
#     elif a in [6, 7, 8]:
#         s = 'лето'
#     else:
#         s = 'осень'
#     return s#
# print(season())


