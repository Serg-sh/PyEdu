# # list comprehension (listcomp & genexp)
# import array
# import os
# from collections import namedtuple
#
# symbols = '!@#$%^&'
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))
# print(codes)
# # OR
# codes = [ord(symbol) for symbol in symbols]
# print(codes)
#
# codes = [ord(symbol) for symbol in symbols if ord(symbol) > 36]
# print(codes)
#
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts)
#
# # GENEXP
#
# print(tuple(ord(symbol) for symbol in symbols))
# print(array.array('I', (ord(symbol) for symbol in symbols)))
# for tshirt in (f'{c}, {s}' for c in colors for s in sizes):
#     print(tshirt)
#
# # TUPLE
#
# lax_coordinates = (33.9425, -118.408056)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# travel_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
#
# for passport in sorted(travel_ids):
#     print('%s/%s' % passport)
# print()
# print()
# print()
#
# print(divmod(20, 8))
# t = (20, 8)
# print(divmod(*t))
# quotient, remainder = divmod(*t)
# print(quotient, remainder, '\n')
# path = 'D:\\Google Диск\\Books\\Programming\\Python\\AByteofPythonRussian-2.01.pdf'
# _, filename = os.path.split(path)  # _-фиктивная переменная
#
# print(filename)
#
#
# print('|{:15} | {:^9} | {:^9} |'.format('*', 'lat.', 'long.'))
#
# # NAMEDTUPLE
#
# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)
# print(tokyo.population)
# print(tokyo[1])
# print(tokyo.coordinates)
# print(tokyo.coordinates[0])
# print(City._fields)
#

# SLICE

l = [10, 20, 30, 40, 50, 60]

print(l[:2])
print(l[2:])
print(l[::2])
print(l[::-1])
print(l[::-2])
