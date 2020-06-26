import threading

from src.Udemy.multithreading.count_triplets import count_three_sum, gen_lst

if __name__ == '__main__':
    print('started main')

    ints = gen_lst(1000)
    ints2 = gen_lst(1500)

    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    # OR with kwargs
    t2 = threading.Thread(target=count_three_sum, daemon=True, kwargs=dict(ints=ints))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('What are we waiting for?')
    print('End main')
