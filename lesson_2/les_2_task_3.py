# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите целое число: '))
n = 0

while number != 0:
    n = n * 10 + number % 10
    number //= 10

print(f'Число обратное введеному: {n}')
