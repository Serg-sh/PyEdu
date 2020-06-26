import random
from typing import List


def gen_lst(count) -> List:
    return [random.randint(-100000, 100000) for _ in range(count)]


def count_three_sum(ints, name_threads ='t'):
    print(f'started count_three_sum in {name_threads}')
    n = len(ints)
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in {name_threads}: {ints[i]}, {ints[j]}, {ints[k]}', end='\n')
    print(f'ended count_three_sum in {name_threads}. Triplets counter={counter}')
