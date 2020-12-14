from time import sleep

from tqdm import trange, tqdm


def main():
    for i in tqdm([1, 2, 3, 4, 5, 6, 7, 9]):
        sleep(0.2)


if __name__ == '__main__':
    main()
