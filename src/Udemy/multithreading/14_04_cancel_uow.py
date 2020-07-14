import threading
import time

from src.Udemy.multithreading.count_triplets import gen_lst


class ThreeSumUnitOfWork(threading.Thread):
    def __init__(self, ints, name='TestThread'):
        super().__init__(name=name)
        self.ints = ints
        self.stop_event = threading.Event()

    def run(self):
        print(f'{self.getName()} starts')
        self.count_three_sum_m2(self.ints)
        print(f'{self.getName()} ends')

    def cancel(self):
        self.stop_event.set()

    def count_three_sum_m2(self, ints):
        print(f'started count_three_sum')
        n = len(ints)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.stop_event.is_set():
                        print('Task was Cancelled')
                        counter = -1
                        return counter
                    if ints[i] + ints[j] + ints[k] == 0:
                        counter += 1
                        print(f'Triple found: {ints[i]}, {ints[j]}, {ints[k]}', end='\n')

        print(f'ended count_three_sum. Triplets counter={counter}')
        return counter


if __name__ == '__main__':
    print('Started main')

    ints = gen_lst(5000)

    task = ThreeSumUnitOfWork(ints)
    task.start()

    time.sleep(5)

    task.cancel()
    task.join()

    print('ended main')
