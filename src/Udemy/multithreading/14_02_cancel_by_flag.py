import threading
import time

from src.Udemy.multithreading.count_triplets import gen_lst

should_stop = False


def count_three_sum_m(ints, name_threads='t'):
    print(f'started count_three_sum in {name_threads}')
    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if should_stop:
                    print('Task was Cancelled')
                    counter = -1
                    return counter
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in {name_threads}: {ints[i]}, {ints[j]}, {ints[k]}', end='\n')

    print(f'ended count_three_sum in {name_threads}. Triplets counter={counter}')
    return counter


if __name__ == '__main__':
    print('Started main')

    ints = gen_lst(5000)

    p = threading.Thread(target=count_three_sum_m, args=(ints,))
    p.start()
    time.sleep(5)

    should_stop = True
    time.sleep(2)

    print('ended main')
