# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Введите размер массива: '))
nums = [i for i in range(1, n + 1)]
x = int(input('Введите число для сравнения с элементами массива: '))
print(nums.count(x))
