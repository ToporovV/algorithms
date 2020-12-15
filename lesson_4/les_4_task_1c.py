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
# Вариант 3

import random
import timeit
import cProfile


def find_min(n):
    array = [random.randint(1, 100) for _ in range(n)]
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array[0], array[1]


print(timeit.timeit('find_min(200)', number=100, globals=globals()))  # 0.595845351999742
print(timeit.timeit('find_min(400)', number=100, globals=globals()))  # 2.1147109550001915
print(timeit.timeit('find_min(800)', number=100, globals=globals()))  # 7.638728283000091
print(timeit.timeit('find_min(1600)', number=100, globals=globals()))  # 28.631802657999287

cProfile.run('find_min(100)')
# 634 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 les_4_task_1c.py:19(find_min)
#         1    0.000    0.000    0.001    0.001 les_4_task_1c.py:20(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       128    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('find_min(200)')
# 1254 function calls in 0.007 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.007    0.007 <string>:1(<module>)
#         1    0.006    0.006    0.007    0.007 les_4_task_1c.py:19(find_min)
#         1    0.000    0.000    0.001    0.001 les_4_task_1c.py:20(<listcomp>)
#       200    0.000    0.000    0.001    0.000 random.py:200(randrange)
#       200    0.000    0.000    0.001    0.000 random.py:244(randint)
#       200    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
#       201    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       200    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       248    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('find_min(400)')
# 2501 function calls in 0.024 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#         1    0.022    0.022    0.024    0.024 les_4_task_1c.py:19(find_min)
#         1    0.000    0.000    0.002    0.002 les_4_task_1c.py:20(<listcomp>)
#       400    0.001    0.000    0.002    0.000 random.py:200(randrange)
#       400    0.000    0.000    0.002    0.000 random.py:244(randint)
#       400    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#       401    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       400    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       495    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('find_min(800)')
# 5017 function calls in 0.088 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.088    0.088 <string>:1(<module>)
#         1    0.083    0.083    0.088    0.088 les_4_task_1c.py:19(find_min)
#         1    0.001    0.001    0.005    0.005 les_4_task_1c.py:20(<listcomp>)
#       800    0.002    0.000    0.003    0.000 random.py:200(randrange)
#       800    0.001    0.000    0.004    0.000 random.py:244(randint)
#       800    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.088    0.088 {built-in method builtins.exec}
#       801    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       800    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1011    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

