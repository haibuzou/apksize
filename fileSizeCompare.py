import os
from os.path import join, getsize


#文件大小比较
def fileSizeDiff(filePath1, filePath2):
    return getsize(filePath1) - getsize(filePath2)

#文件夹总大小比较
def fileDirSizeDiff(fileDirPath1, fileDirPath2):
    return getFileDirSize(fileDirPath1) - getFileDirSize(fileDirPath2)

#获取文件夹目录的文件总大小
def getFileDirSize(fileDirPath):
    size = 0
    for root, files in os.walk(fileDirPath):
        size += sum([getsize(join(root, name)) for name in files])
    return size
    