# Задание 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def as_code(n=32):
    res = ''
    if n == 127:
        res += f'{n} - {chr(n)}'
    else:
        if n in (42, 52, 62, 72, 82, 92, 102, 112, 122):
            res += '\n'
        res += ' ' + f'{n} - {chr(n) + as_code(n + 1)}'
    return res

print(as_code())
