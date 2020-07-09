import multiprocessing
import time

from src.Udemy.multithreading.count_triplets import gen_lst, count_three_sum

if __name__ == '__main__':
    print('Started main')

    ints = gen_lst(5000)

    p= multiprocessing.Process(target=count_three_sum, args=(ints,))
    p.start()
    time.sleep(5)
    p.terminate()
    print('ended main')