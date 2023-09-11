# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
# 10 -> 1 2 4 8

N = int(input('Введите число N '))
res = 0
degree = 0
while True:
    res = 2**degree
    if (res >= N):
        break
    degree = degree + 1
    print(res)