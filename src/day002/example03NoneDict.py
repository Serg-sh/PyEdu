# None - пустота

def test():
    print('TEST')


azaza = test()
print(azaza)

# Dictionary

test = {
    'ключ1': 'Значение1',
    'ключ2': 'Значение2',
    'ключ3': 'Значение3',
    'ключ4': 'Значение4'
}

print(test['ключ1'])
if 'ключ3' in test:
    print('True')

print(test.get('ключ1'))
print(test.get('0'))
print(test.get('0', '0000'))

