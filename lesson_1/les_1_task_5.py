# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.


a, b = input('Введите два символа латинского алфавита от a до z через пробел: ').split()

pos_a = ord(a) - 96
pos_b = ord(b) - 96

num = abs(pos_a - pos_b) - 1

print(f'Позиция первого символа в алфавите: {pos_a}')
print(f'Позиция второго символа в алфавите: {pos_b}')
print(f'Количество символов межну ними: {num}')
