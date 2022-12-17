# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def Check_Points(num):
    if num == 1:
        print('x > 0, y > 0')
    elif num == 2:
        print('x < 0, y > 0')
    elif num == 3:
        print('x < 0, y < 0')
    elif num == 4:
        print('x > 0, y < 0')
    else:
        print('Введите допустимое значение')

num = int(input('Введите номер четверти: '))
Check_Points(num)