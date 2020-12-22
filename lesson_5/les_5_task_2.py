# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

first_number = input('Введите 1 число: ')
second_number = input('Введите 2 число: ')

hex_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def hex_sum(a, b):
    result = deque()
    k = 0
    first = deque(a)
    second = deque(b)
    if len(first) > len(second):
        first, second = second, first

    while len(first) > 0:
        spam = hex_nums.index(second.pop())
        egg = hex_nums.index(first.pop())
        result.appendleft(hex_nums[(spam + egg + k) % 16])
        k = (spam + egg) // 16

    while len(second) > 0:
        sec = second.pop()
        result.appendleft(hex_nums[(hex_nums.index(sec) + k) % 16])
        if hex_nums.index(sec) > 15:
            k = 1
        else:
            k = 0
    if k == 1:
        result.appendleft('1')
    return result


print(hex_sum(first_number, second_number))