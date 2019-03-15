import os
import time

source = 'source'
targetDir = 'D:\\GitRepos\\PyEdu\\src\\day003\\target_dir\\'
target = targetDir + time.strftime('%Y%m%d_%H%M%S') + '.zip'
zipCommand = '"C:\\Program Files (x86)\\GnuWin32\\bin\\zip.exe" -qr {0} {1}'.format(target, ''.join(source))
if os.system(zipCommand) == 0:
    print(' Резервная копия успешно создана в', target)
else:
    print(' Создание резервной копии НЕ УДАЛОСЬ')

input()
