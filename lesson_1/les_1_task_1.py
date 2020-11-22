# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1zz9tWZxJva8FKRbk8uwkW4Bo6ghIm7m7/view?usp=sharing

n = int(input('Введите любое целое трезначное число: '))

a = n // 100
b = n // 10 % 10
c = n % 10

sum = a + b + c
mul = a * b * c

print(f'Сумма цифр трезначного числа {sum}')
print(f'Произведение цифр трезначного числа {mul}')
