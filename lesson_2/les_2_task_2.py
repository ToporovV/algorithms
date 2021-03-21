# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def rec(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        n = number % 10
        number //= 10
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        return rec(number, even, odd)


number = int(input('Введите любое натуральное число: '))

result = rec(number)

print(f'В числе содержится {result[0]} четных чисел и {result[1]} нечетных')
