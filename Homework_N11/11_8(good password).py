# 8. Good password 🌶️
# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое
# значение пароля password и возвращает значение True если пароль является надежным и False
# в противном случае.
#
# Пароль является надежным если:
#
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.
# Примечание. Следующий программный код:
#
# print(is_password_good(‘aabbCC11OP’))
# print(is_password_good(‘abC1pu’))
# должен выводить:
#
# True
# False
def is_password_good(password):
    a = 0
    b = 0
    c = 0
    for i in password:
        if i.isupper():
            a += 1
        if i.islower():
            b += 1
        if i.isdigit():
            c += 1
    return len(password) >= 8 and a >= 1 and b >= 1 and c >= 1
password = input('''Введите надежный пароль:
его длина не менее 8 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру.
Введите пароль: ''')
print(is_password_good(password))
while not is_password_good(password):
    password = input('Ошибка! Введите пароль правильно: ')
else:
    print(is_password_good(password))
