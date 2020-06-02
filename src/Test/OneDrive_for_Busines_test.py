import os

from shareplum import Site
from shareplum import Office365
from shareplum.site import Version


def ConnectToO365():
    global folder
    authcookie = Office365('https://rgorgua.sharepoint.com/', username='shpak@astrella.com.ua',
                           password='33Gjhncbufhf').GetCookies()
    print(authcookie)
    site = Site('https://rgorgua.sharepoint.com/sites/astrella/', version=Version.v365, authcookie=authcookie,
                timeout=10)
    # sp_list = site.GetListCollection
    folder = site.Folder('Shared Documents/TestFolderByPython/')

ConnectToO365()
with open('//10.123.11.10/DB_backups/astrella/astrella_backup_2020_06_01_231713_7753403.trn', 'rb') as f:
    data = f.read()
    file_name = f.name.split('/')[-1]
    print(file_name)
    folder.upload_file(data, file_name)

with open('//10.123.11.10/DB_backups/astrella/astrella_backup_2020_06_01_231240_1933367.bak', 'rb') as f:
    data = f.read()
    file_name = f.name.split('/')[-1]
    print(file_name)
    folder.upload_file(data, file_name)


# //10.123.11.10/DB_backups/astrella/astrella_backup_2020_06_01_231713_7753403.trn


