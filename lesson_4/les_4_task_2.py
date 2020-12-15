# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
# его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».

import timeit
from math import sqrt

SIZE = 10000


def sieve(n):
    sieve = [i for i in range(SIZE)]
    sieve[1] = 0

    for i in range(2, SIZE):
        if sieve[i] != 0:
            j = i + i
            while j < SIZE:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    number = res[n - 1]
    return number


# print(sieve(7))

def prime(n):
    prime = []
    for i in range(2, SIZE):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)
    number = prime[n - 1]
    return number


# print(prime(7))

print(timeit.timeit('sieve(100)', number=100, globals=globals()))  # 0.9472390390001237
print(timeit.timeit('sieve(200)', number=100, globals=globals()))  # 0.9085051649999514
print(timeit.timeit('sieve(400)', number=100, globals=globals()))  # 0.9280273099993792
print(timeit.timeit('sieve(800)', number=100, globals=globals()))  # 0.9260087989996464

print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 11.292087286999958
print(timeit.timeit('prime(200)', number=100, globals=globals()))  # 11.128593337999519
print(timeit.timeit('prime(400)', number=100, globals=globals()))  # 11.297867145000055
print(timeit.timeit('prime(800)', number=100, globals=globals()))  # 11.165992875000484
