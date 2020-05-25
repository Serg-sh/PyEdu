# list comprehension (listcomp & genexp)
import array
import os
import sys


def print_separator():
    print('======================================================')


from collections import namedtuple

symbols = '!@#$%^&'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)
# OR
codes = [ord(symbol) for symbol in symbols]

print(codes)
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 36]

print(codes)
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]

# GENEXP

print(tshirts)
print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))

# TUPLE

for tshirt in (f'{c}, {s}' for c in colors for s in sizes):
    print(tshirt)
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

travel_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(travel_ids):
    print('%s/%s' % passport)

print_separator()

for country, _ in sorted(travel_ids):
    print(country)

print_separator()

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder, '\n')
path = '/Users/admin/Pictures/vodafon.jpg'
_, filename = os.path.split(path)  # _-фиктивная переменная

print(filename)

print_separator()

metro_areas = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
               ('Dehli NSR', 'IN', 21.935, (28.613889, 77.208889))]

print('|{:15} | {:^9} | {:^9}|'.format('', 'lat.', 'long.'))
fmt = '|{:15} | {:9.4f} | {:9.4f}|'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude >= 0:
        print(fmt.format(name, latitude, longitude))

print_separator()
# NAMEDTUPLE

City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.population)
print(tokyo[1])
print(tokyo.coordinates)
print(tokyo.coordinates[0])
print(City._fields)

# SLICE

l = [10, 20, 30, 40, 50, 60]

print(l[:2])
print(l[2:])
print(l[::2])
print(l[::-1])
print(l[::-2])

DESCRIPTION = slice(6, 40)

l = list(range(10))
print(l)

l[2:5] = [20, 30, 40]
print(l)

weird_board = [['_'] * 3 for i in range(3)]
print(weird_board)
weird_board[1][2] = 'X'
print(weird_board)

t = (1, 2, 3)
print(id(t))
t *= 2
print(t)
print(id(t))

t2 = (1, 2, [30, 40])
try:
    t2[2] += [50, 60]
except TypeError:
    print(sys.exc_info())

print(t2)

# list.sort()
