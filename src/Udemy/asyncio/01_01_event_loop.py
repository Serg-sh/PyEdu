import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


async def main():
    await asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    # coroutine = main()
    # print(coroutine)
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.run_until_complete(main())
    #     print('coroutine have finished')
    # finally:
    #     loop.close()
    #     print('loop is closed')
