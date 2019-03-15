set1 = set([3, 1, 5, 4, 7, 7, 1])
set2 = set([2, 1, 5, 3, 7, 8, 1])


print(set1.issuperset(set2))

print(set1.intersection(set2))
print(set1 & set2)

set3 = set1.copy()
set3.add(9)
print(set3.issuperset(set1))

a = str(5)