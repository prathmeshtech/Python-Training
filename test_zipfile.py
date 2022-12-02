import zipfile

my_zip = zipfile.ZipFile(r'D:\files.zip', 'w', compression = zipfile.ZIP_DEFLATED)

my_zip.write(r'D:\cctech\test.txt')

my_zip.close()