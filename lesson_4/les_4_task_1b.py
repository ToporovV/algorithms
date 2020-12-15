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
# Вариант 2

import random
import timeit
import cProfile


def find_min(n):
    array = [random.randint(1, 100) for _ in range(n)]
    min_elem_1 = min(array)
    array.pop(array.index(min_elem_1))

    min_elem_2 = min(array)
    return min_elem_1, min_elem_2


print(timeit.timeit('find_min(2000)', number=100, globals=globals())) # 0.5745068620003622
print(timeit.timeit('find_min(4000)', number=100, globals=globals())) # 1.0415379639998719
print(timeit.timeit('find_min(8000)', number=100, globals=globals())) # 1.9703089570002703
print(timeit.timeit('find_min(16000)', number=100, globals=globals())) # 3.9667220609999276

cProfile.run('find_min(1000)')

# 5316 function calls in 0.005 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.000    0.000    0.005    0.005 les_4_task_1b.py:19(find_min)
#         1    0.001    0.001    0.005    0.005 les_4_task_1b.py:20(<listcomp>)
#      1000    0.002    0.000    0.003    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.004    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1307    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

cProfile.run('find_min(2000)')

# 10603 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.000    0.000    0.010    0.010 les_4_task_1b.py:19(find_min)
#         1    0.002    0.002    0.010    0.010 les_4_task_1b.py:20(<listcomp>)
#      2000    0.004    0.000    0.007    0.000 random.py:200(randrange)
#      2000    0.002    0.000    0.008    0.000 random.py:244(randint)
#      2000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      2000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2594    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}

cProfile.run('find_min(4000)')

# 21246 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.000    0.000    0.021    0.021 les_4_task_1b.py:19(find_min)
#         1    0.004    0.004    0.021    0.021 les_4_task_1b.py:20(<listcomp>)
#      4000    0.007    0.000    0.014    0.000 random.py:200(randrange)
#      4000    0.003    0.000    0.017    0.000 random.py:244(randint)
#      4000    0.005    0.000    0.007    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#      4000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      5237    0.001    0.000    0.001    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
