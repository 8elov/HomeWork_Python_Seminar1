# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

import math

def Get_Distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(result, 2)

x1 = int(input('Введите X 1ой точки: '))
y1 = int(input('Введите Y 1ой точки: '))

x2 = int(input('Введите X 2ой точки: '))
y2 = int(input('Введите Y 2ой точки: '))

print('Расстояние между точками =', Get_Distance(x1, y1, x2, y2))
