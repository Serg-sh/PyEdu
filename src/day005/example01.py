from time import sleep


def countDown(i):
    print(i)
    sleep(1)
    if i <= 0:
        return
    else:
        countDown(i-1)


countDown(10)
