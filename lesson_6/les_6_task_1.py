# Для каждого упражнения написать программную реализацию.
# Код пишите в файлах с расширением .py в кодировке UTF-8 (в PyCharm работает по умолчанию).
# Каждую задачу необходимо сохранять в отдельный файл.
# Рекомендуем использовать английские имена, например, les_6_task_1.
# Для оценки «Отлично» необходимо выполнить все требования, указанные в задании и примечаниях.
#
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
#
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
#
# ● написать 3 варианта кода (один у вас уже есть);
#
# ● проанализировать 3 варианта и выбрать оптимальный;
#
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
#
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import sys
import platform
import random

print(sys.version)  # Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)]
print(platform.architecture()) # ('64bit', 'WindowsPE')


def show_size(item):
    size = sys.getsizeof(item)
    if hasattr(item, '__iter__'):
        if hasattr(item, 'keys'):
            for key, value in item.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(item, str):
            for i in item:
                size += sys.getsizeof(i)
    return size


MIN_ITEM = 0
MAX_ITEM = 100


def find_min_1(n):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    min_elem_1 = array[0]
    min_elem_2 = array[0]
    for i in array:
        if i < min_elem_1:
            min_elem_1 = i

    if array.count(min_elem_1) == 1:
        for i in array:
            if i < min_elem_2 and i != min_elem_1:
                min_elem_2 = i
    elif array.count(min_elem_1) == 2:
        min_elem_2 = min_elem_1

    _sum = 0
    var_lst = (MIN_ITEM, MAX_ITEM, n, array, min_elem_1, min_elem_2, i)
    for i in var_lst:
        _sum += show_size(i)
    return f'Под переменные выделено {_sum} байт памяти'


def find_min_2(n):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    min_elem_1 = min(array)
    array.pop(array.index(min_elem_1))

    min_elem_2 = min(array)

    _sum = 0
    var_lst = (MIN_ITEM, MAX_ITEM, n, array, min_elem_1, min_elem_2)
    for i in var_lst:
        _sum += show_size(i)
    return f'Под переменные выделено {_sum} байт памяти'


def find_min_3(n):
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(n)]
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    _sum = 0
    var_lst = (MIN_ITEM, MAX_ITEM, n, array, array[0], array[1], i, j)
    for i in var_lst:
        _sum += show_size(i)
    return f'Под переменные выделено {_sum} байт памяти'


print(find_min_1(10))  # Под переменные выделено 628 байт памяти
print(find_min_2(10))  # Под переменные выделено 572 байт памяти
print(find_min_3(10))  # Под переменные выделено 656 байт памяти

# ВЫВОД: наименее затратным с точки зрения памяти является 2й способ (find_min_2)т.к. в данном способе используется
# меньшее количество переменных и отсутсвует цикл.
