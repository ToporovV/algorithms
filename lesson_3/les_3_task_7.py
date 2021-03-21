# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_elem1 = array[0]
min_elem2 = array[0]

for i in array:
    if i < min_elem1:
        min_elem1 = i

if array.count(min_elem1) == 1:
    for i in array:
        if i < min_elem2 and i != min_elem1:
            min_elem2 = i
elif array.count(min_elem1) == 2:
    min_elem2 = min_elem1

print(f'Наименьший элемент массива {min_elem1},второй наименьший элемент {min_elem2}')
