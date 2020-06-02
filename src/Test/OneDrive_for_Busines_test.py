from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

authcookie = Office365('https://rgorgua.sharepoint.com/', username='shpak@astrella.com.ua',
                       password='33Gjhncbufhf').GetCookies()
print(authcookie)
site = Site('https://rgorgua.sharepoint.com/sites/astrella/', version=Version.v365, authcookie=authcookie)
# print(site.get_list_collection())
sp_list = site.GetListCollection
# print(sp_list)
folder = site.Folder('Shared Documents/TestFolderByPython/')
with open('D:\\ВоронцоваА_В.rar', 'rb') as f:
    data = f.read()
    file_name = f.name.split('\\')[-1]
    folder.upload_file(data, file_name)





