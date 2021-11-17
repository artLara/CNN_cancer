from os import walk
from shutil import copyfile
# tipo = 'maligno'
tipo = 'benigno'
path = 'D:\\Documentos\\cancerCNN\\DataSet\\' + tipo
# f = []
# dirpath, dirnames, filenames = walk(path)

# print(dirpath)
dst = 'D:\\Documentos\\cancerCNN\\DataSet\\'
for (dirpath, dirnames, filenames) in walk(path):
    # f.extend(filenames)
    for name in filenames:
        # print(name)
        elements = name.split('-')
        zoom = elements[3]
        num = elements[4]
        # print(dirpath+'\\'+name)
        # print('zoom = {} num={}'.format(zoom, num))
        # print(dst+zoom+'x\\maligno\\'+name)
        copyfile(dirpath+'\\'+name, dst+zoom+'x\\'+tipo+'\\'+name)

        # break

print('Finish!!')
