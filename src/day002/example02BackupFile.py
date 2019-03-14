filename1 = '201803.pdf'
filename2 = 'backup_' + filename1

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')
file2.write(file1.read())
file1.close()
file2.close()
