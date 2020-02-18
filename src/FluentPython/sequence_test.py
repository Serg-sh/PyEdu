# list comprehension (listcomp & genexp)
import array

symbols = '!@#$%^&'
codes =[]
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
print(tshirts)

# GENEXP

print(tuple(ord(symbol) for symbol in symbols))
print(array.array('I', (ord(symbol) for symbol in symbols)))
for tshirt in (f'{c}, {s}' for c in colors for s in sizes):
    print(tshirt)

# TUPLE

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travel_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(travel_ids):
    print('%s/%s' % passport)
