# имя файла, в котором мы сохраним объект
import pickle

shoplistfile = ' shoplist.data'
# список покупок
shoplist = [' яблоки', ' манго', ' морковь']
# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)  # помещаем объект в файл
f.close()
del shoplist  # уничтожаем переменную shoplist
# Считываем из хранилища
# f = open(shoplistfile, 'rb')
# storedlist = pickle.load(f)  # загружаем объект из файла
with open(shoplistfile, 'rb') as f:
    storedlist = pickle.load(f)  # загружаем объект из файла
print(storedlist)
