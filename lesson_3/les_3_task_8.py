# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
# последнюю ячейку строки. В конце следует вывести полученную матрицу.
COL = 5
LINE = 4
matrix = []

for i in range(LINE):
    array_line = []
    sum_line = 0

    for j in range(COL - 1):
        number = int(input(f'Введите число для строки {i + 1}: '))
        sum_line += number
        array_line.append(number)

    array_line.append(sum_line)
    matrix.append(array_line)

print(*matrix, sep='\n')
