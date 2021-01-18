# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).
import random


def gnome_sort(array):
    i = 1
    while i < len(array):
        if array[i - 1] <= array[i]:
            i += 1
        else:
            array[i - 1], array[i] = array[i], array[i - 1]
            if i > 1:
                i -= 1
    return array


def med_search(array):
    k = len(array) // 2

    def med_split(array, k):
        if len(array) == 1 and k == 0:
            return array[0]

        left = [i for i in array if i < array[0]]
        right = [i for i in array if i > array[0]]
        med = [i for i in array if i == array[0]]

        if k < len(left):
            return med_split(left, k)
        elif k < len(left) + len(med):
            return med[0]
        else:
            return med_split(right, k - len(med) - len(left))

    return med_split(array, k)


m = 5
lst = [random.randint(0, 100) for i in range(2 * m + 1)]

print(f'Исходный массив:\n{lst}\n')
print(f'Медиана в массиве без сортировки: \n{med_search(lst)}\n')

result = gnome_sort(lst)

print(f'Сортированный массив:\n{result}\n')
print(f'Медиана в отсортированном массиве:\n{result[len(result) // 2]}')

