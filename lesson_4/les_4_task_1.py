# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
# задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
# для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Анализ алгоритма поиска двух наименьших чисел списка из задачи 7 урока 3
# Вариант 1

import random
import timeit
import cProfile

MIN_ITEM = 0
MAX_ITEM = 100


def find_min(n):
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

    return min_elem_1, min_elem_2


print(timeit.timeit('find_min(2000)', number=100, globals=globals()))  # 0.6033265899995968
print(timeit.timeit('find_min(4000)', number=100, globals=globals()))  # 1.0416011700003764
print(timeit.timeit('find_min(8000)', number=100, globals=globals()))  # 2.055350960999931
print(timeit.timeit('find_min(16000)', number=100, globals=globals()))  # 4.226951760999782

cProfile.run('find_min(1000)')

# 5263 function calls in 0.005 seconds

# Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#      1    0.000    0.000    0.005    0.005 les_4_task_1.py:22(find_min)
#      1    0.001    0.001    0.005    0.005 les_4_task_1.py:23(<listcomp>)
#   1000    0.002    0.000    0.003    0.000 random.py:200(randrange)
#   1000    0.001    0.000    0.004    0.000 random.py:244(randint)
#   1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#   1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      2    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#   1256    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('find_min(2000)')

# 10511 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.000    0.000    0.011    0.011 les_4_task_1.py:22(find_min)
#         1    0.002    0.002    0.011    0.011 les_4_task_1.py:23(<listcomp>)
#      2000    0.004    0.000    0.007    0.000 random.py:200(randrange)
#      2000    0.002    0.000    0.009    0.000 random.py:244(randint)
#      2000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#      2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         2    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2504    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}

cProfile.run('find_min(4000)')

# 21042 function calls in 0.024 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#         1    0.000    0.000    0.024    0.024 les_4_task_1.py:22(find_min)
#         1    0.005    0.005    0.024    0.024 les_4_task_1.py:23(<listcomp>)
#      4000    0.008    0.000    0.015    0.000 random.py:200(randrange)
#      4000    0.004    0.000    0.019    0.000 random.py:244(randint)
#      4000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#      4000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         2    0.000    0.000    0.000    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      5035    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
