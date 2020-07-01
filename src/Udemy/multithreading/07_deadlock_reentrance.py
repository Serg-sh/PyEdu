import threading

lock_obj = threading.RLock()

print('Aquaire 1st time')
lock_obj.acquire()

print('Aquaire 2st time')
lock_obj.acquire()

print('Releasing')
lock_obj.release()

# def reentrance():
#     print('start')
#     lock_obj.acquire()
#     print('Acquaired')
#     reentrance()
#
#
# reentrance()


