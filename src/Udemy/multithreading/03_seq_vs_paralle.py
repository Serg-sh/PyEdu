import threading

from src.Udemy.multithreading.count_triplets import count_three_sum, gen_lst
from src.Udemy.multithreading.decorators import measure_time


@measure_time
def run_in_parallel(ints1, ints2):
    t1 = threading.Thread(target=count_three_sum, args=(ints1, f't1'), daemon=True)
    t2 = threading.Thread(target=count_three_sum, args=(ints2, f't2'), daemon=True)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


@measure_time
def run_in_seq(ints1, ints2):
    count_three_sum(ints1, f'main 1')
    count_three_sum(ints2, f'main 2')


if __name__ == '__main__':
    print('started main')

    ints1 = gen_lst(300)
    ints2 = gen_lst(300)

    run_in_parallel(ints1, ints2)
    run_in_seq(ints1, ints2)

    print('What are we waiting for?')
    print('End main')
