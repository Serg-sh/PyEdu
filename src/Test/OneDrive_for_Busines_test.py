import base64
import os
import sys
import time
import traceback

from datetime import datetime
from shareplum import Office365
from shareplum import Site
from shareplum.site import Version


def time_log():
    return datetime.now().strftime('%Y-%m-%d %H:%M')


try:
    authcookie = Office365('https://rgorgua.sharepoint.com/',
                           username=base64.b64decode('c2hwYWtAYXN0cmVsbGEuY29tLnVh').decode('utf-8'),
                           password=base64.b64decode('MzNHamhuY2J1Zmhm').decode('utf-8')).GetCookies()
    site = Site('https://rgorgua.sharepoint.com/sites/astrella/', version=Version.v365, authcookie=authcookie)

    print(time_log(), '    Login to O365 by Astrella Capital successful!')

    folder_shared_o365 = site.Folder('Shared Documents/ИТ Служба/BackUps/Astrella/1C_UTP/')
    file_dir_local = '//10.123.11.10/DB_backups/astrella/'
    files_local = [f for f in os.listdir(file_dir_local)]

    for file in sorted(files_local, key=lambda f: os.path.getatime(os.path.join(file_dir_local, f)), reverse=True)[:2]:
        file_abs_path = os.path.join(file_dir_local, file)
        print(time_log(), '    File: ', file_abs_path)
        print(time_log(), '    Created: ', time.ctime(os.path.getatime(file_abs_path)))
        print(time_log(), '    File size:', os.path.getsize(file_abs_path) // 1024 // 1024, 'Mb')

        with open(file_abs_path, 'rb') as f:
            data = f.read()
            folder_shared_o365.upload_file(data, file)
            print(time_log(), '    File:', file, 'copied successful.')
except Exception as e:
    print(time_log(), '    Script is end with error.')
    print(time_log(), '   ', e)
    print(time_log(), '   ', traceback.format_exc())
    sys.exit()

# e = base64.b64encode(b'33Gjhncbufhf')
# print(e)
#
# d = base64.b64decode('MzNHamhuY2J1Zmhm')
#
# print(d.decode('utf-8'))
