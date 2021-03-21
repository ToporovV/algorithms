# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_part = array[:middle]
    right_part = array[middle:]

    left_part = merge_sort(left_part)
    right_part = merge_sort(right_part)

    i, j = 0, 0
    result = []

    while i < len(left_part) or j < len(right_part):

        if i >= len(left_part):
            result.append(right_part[j])
            j += 1

        elif j >= len(right_part):
            result.append(left_part[i])
            i += 1

        elif left_part[i] < right_part[j]:
            result.append(left_part[i])
            i += 1

        else:
            result.append(right_part[j])
            j += 1

    return result


SIZE = 10
lst = [round(random.uniform(0, 49.99), 2) for i in range(SIZE)]

print(f'Исходный массив:\n{lst}\n')
print(f'Сортированный массив:\n{merge_sort(lst)}')
