# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума 
#  и не больше заданного максимума)

number_list = [int(i) for i in input('Введите элементы значений массива(списка): \n').split()]
max = int(input('Введите максимальное значение: \n'))
min = int(input('Введите минимальное значение: \n'))

print(*number_list)
print(*[i for i in range(0, len(number_list) - 1) if (number_list[i] >= min) and number_list[i] <= max])
