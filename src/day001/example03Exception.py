try:
    print(7 / 0)
except ZeroDivisionError:
    print('Поймано исключение - деление на ноль')
except:
    print('Поймано какое-то исключение')

finally:
    print('Блок Finally')

try:
    if True:
        raise TypeError
except TypeError:
    print('Поймано наше исключение')

    print('Программа завершена', 2, 'Qwerty')
