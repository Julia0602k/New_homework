# 5. Красный, синий и желтый называются основными цветами,
# потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
#
# Напишите программу, которая считывает названия двух основных цветов
# для смешивания. Если пользователь вводит что-нибудь помимо названий
# «красный», «синий» или «желтый», то программа должна вывести
# сообщение об ошибке. В противном случае программа должна вывести
# название вторичного цвета, который получится в результате.
#
color1 = input('Введите основной цвет N1 (красный, желтый или синий): ')
color2 = input('Введите основной цвет N2 (красный, желтый или синий): ')
if color1 and color2 not in ['красный', 'желтый', 'синий']:
    print('Ошибка! Введите основные цвета!')
elif color1 == color2:
    print('Ошибка! Введите 2 разных основных цвета!')
else:
    if color1 in ['красный', 'желтый'] and color2 in ['красный', 'желтый']:
# (color1 and color2) in ['красный', 'желтый']:
# (color1 or color2 == 'красный') and (color1 or color2 == 'желтый'):
        print('оранжевый')
    elif color1 in ['красный', 'синий'] and color2 in ['красный', 'синий']:
        print('фиолетовый')
    else:
        print('зеленый')

