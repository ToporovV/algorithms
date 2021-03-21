# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib


def count(text):
    str_ = str(text).lower()
    size = len(str_)
    data = set()

    for i in range(1, size):
        for j in range(size - i + 1):
            code = hashlib.sha256(str_[j:j + i].encode('utf-8')).hexdigest()
            data.add(code)
    return len(data)


print(count('papa'))
print(count('sova'))
