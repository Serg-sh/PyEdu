import logging
import os
import sys
import warnings
import platform

print(sys.version_info)
if sys.version_info[0] < 3:
    warnings.warn("Для выполнения этой программы необходима как минимум версия Python 3.0", RuntimeWarning)
else:
    print('Нормальное продолжение')

if platform.platform().startswith('Windows'):
    loggingFile = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    loggingFile = os.path.join(os.getenv('HOME'), 'test.log')
print("Сохраняем лог в", loggingFile)
logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s : %(levelname)s : %(message)s',
    filename=loggingFile,
    filemode='w',
)
logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")

