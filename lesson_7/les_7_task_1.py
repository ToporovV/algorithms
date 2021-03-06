# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def bubble_sort(array):
    n = 1
    while n < len(array):
        no_swap = True
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                no_swap = False
        if no_swap:
            break
        n += 1
    return array


SIZE = 10
lst = [random.randint(-100, 99) for item in range(SIZE)]

print(f'Исходный массив:\n{lst}\n')
print(f'Отсортированный массив:\n{bubble_sort(lst)}\n')
