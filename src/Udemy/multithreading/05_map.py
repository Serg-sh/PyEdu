import concurrent.futures

from src.Udemy.multithreading.count_triplets import gen_lst, count_three_sum

if __name__ == '__main__':
    print('started main')

    data = gen_lst(500)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        for r in results:
            print(f'{r=}')

    print('ended main')
