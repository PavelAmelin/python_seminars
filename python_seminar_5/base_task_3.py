def reverse_num(n):
    if n < 10:
        return n
    return int(str(n % 10) + str(reverse_num(n // 10)))

num = int(input('Введите число: '))
print(reverse_num(num))