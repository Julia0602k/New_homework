#
# 11. Правильная скобочная последовательность 🌶️
# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую
# строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход
# строка является правильной скобочной последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только
# из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
#
# Примечание 2. Следующий программный код:
#
# print(is_correct_bracket(‘()(()())’))
# print(is_correct_bracket(‘)(())(‘))
# должен выводить:
#
# True
# False

def is_correct_bracket(text):
    count1 = 0
    for i in text[count1:]:
        if i == '(':
            count1 += 1
        else:
            break
    for i in text[count1:]:
        if i == ')':
            count1 += 1
    return count1
    # for i in text:
    #     if i == '(' and
    #
text = input('''Введите строку, состоящую из символов "(" и ")" : ''')
print(is_correct_bracket(text))
# start = 1
# count = 0
# while start:
#     for i in text:
#         if i in ['(', ')']:
#             count += 1
#     if count == len(text):
#         start = 0
#         print('ok')
#     else:
#         text = input('''Ошибка! Введите строку, состоящую из символов "(" и ")" : ''')
