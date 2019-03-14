# filename = input('Укажите файл: ')
file = open('test.txt', 'r')

# r - Чтение файла
# w - Перезапись файла
# a - Добавление в файла

print(file.read(6))
print('В данном файле', len(file.read()), 'символов')
file.close()

file = open('test1.txt', 'w')
file.write('Привет, Мир!')
file.close()

file = open('test2.txt', 'a')
file.write(" TEST")
file.close()
