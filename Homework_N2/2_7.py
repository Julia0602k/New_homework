# 7. Назовем число красивым, если оно является четырехзначным
# и делится нацело на 7 или на 17.
# Напишите программу, определяющую, является ли введённое число красивым.
# Программа должна вывести «YES», если число является красивым,
# или «NO» в противном случае.

num4 = int(input('Введите число: '))
if num4 >= 1000 and num4 < 10000 and not num4 % 7 and not num4 % 17:
    print('YES')
else:
    print('NO')