import asyncio

import aiofiles

from src.Udemy.multithreading.decorators import measure_time, async_measure_time


@measure_time
def read_lagre_file():
    with open('..\\data\\big_file.txt') as f:
        return f.read()


@async_measure_time
async def async_read_lagre_file():
    async with aiofiles.open('..\\data\\big_file.txt', mode='r') as f:
        return await f.read()


def count_words(text):
    return len(text.split(' '))


async def async_main():
    text = await async_read_lagre_file()
    print(count_words(text))


def main():
    text = read_lagre_file()
    print(count_words(text))


if __name__ == '__main__':
    asyncio.run(async_main())
    main()
