# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

n = int(input('Введите номер буквы в латинском алфавите: '))

const = 96
s = chr(const + n)

print(f'Данный символ: {s}')