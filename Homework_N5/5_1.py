# Даны 2 списка:
# a = [4,6,'pу','tell',78]
# b = [44,'hello',56,'exept',['world',5.7],3,6]
#
# Выполнить следующие операции:
# 1. Сложить два списка (решить двумя способами).
# 2. Перенесите 6-ой элемент на 3 позицию уже сложенных списков.
# 3. Посчитать сколько раз встречается число 6 уже в сложенных списках.
# 4. Вывести на экран количество элементов сложенного списка.
# 5. Вывести 1 элемент вложенного списка.
# **6. Посчитать сколько раз в общем всречается 1(единица) в
# следующем списке и его элементах:
# [[1,5.1], 1,'hello1world',51,'exept',['orange1',1.7,1],3,6]
# В ответе кол-во единиц должно равнятся 8.

a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', ['world', 5.7], 3, 6]
len(a+b)

# Задание 1 (сложить 2 списка)
list = a + b
a.extend(b)
print('Ответ 1: \n', list, '\n', a)

# Задание 2 (Перенести 6-ой элемент на 3 позицию уже сложенных списков)
list.insert(3, list[5])
print('Ответ 2: \n', list)
list.pop(6)
print(list)

# Задание 3 (Посчитать сколько раз встречается число 6 в уже сложенных списках)
print('Ответ 3: число 6 встречается', list.count(6), 'раза')

# Задание 4 (Вывести на экран количество элементов сложенного списка)
print('Ответ 4: количество элементов сложенного списка', len(list))

# Задание 5 (Вывести 1 элемент вложенного списка)
print('Ответ 5: 1ый элемент вложенного списка: ', a[9][1])

# Задание 6. (Посчитать сколько раз в общем всречается 1(единица) в новом списке

# list6 = [[1, 5.1], 1, 'hello1world', 51, 'exept', ['orange1', 1.7, 1], 3, 6]
# # print(', '.join(list6[0]))
# count = 0
# for row in list6:
#     for elem in row:
#         elem = str(elem)
#         c = elem.find('1')
#         if c >= 0:
#             count += c
#     row = str(row)
#     d = row.find('1')
#     count += d
# print(count)



