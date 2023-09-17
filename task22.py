# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во чисел первого множества: "))
setNumbers1 = list() # numbers = []
for i in range(n):
    print("Введите число", {i+1}, " множества 1: ")
    setNumbers1.append(input())

m = int(input("Введите кол-во чисел второго множества: "))
setNumbers2 = list() # numbers = []
for i in range(m):
    print("Введите число", {i+1}, " множества 2: ")
    setNumbers2.append(input())

print("Множество 1 : ")
print(*setNumbers1)

print("Множество 2 : ")
print(*setNumbers2)

setFinal = sorted(set(setNumbers1).intersection(set(setNumbers2)))
print("Множество пересекающихся значений в порядке возростания: \n", *setFinal)
