a = 5
b = 8

a, b = b, a

print(a, b)

a, *b = [1, 2, 3, 4]
print(a, b)

points = [{'x': 2, 'y': 3}, {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])

print(points)

listOne = [2, 3, 4]
listTwo = [2 * i for i in listOne if i > 2]
print(listOne)
print(listTwo)
