"""
Задание 2.
Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""

words = [b'class', b'function', b'method']
for word in words:
    print(f'{type(word)} {word} {len(word)}')
    print()