from fileSizeCompare import fileDirSizeDiff
from sizeFormat import sizeFormat
import os
from os.path import join, getsize

oldApkDirPath = '/Users/liulei/StudioProjects/apksize/oldapk/TPPcn227200vc10.0.6vn1006'
newApkDirPath = '/Users/liulei/StudioProjects/apksize/newapk/TPPcn228200vc10.1.1vn1011'
oldApkFilePath = '/Users/liulei/StudioProjects/apksize/oldapk/TPPcn227200vc10.0.6vn1006.apk'
newApkFilePath = '/Users/liulei/StudioProjects/apksize/newapk/TPPcn228200vc10.1.1vn1011.apk'

def arscFileSizeDiff():
    print(sizeFormat(getFileSizeBySuffix(newApkPath, 'arsc') - getFileSizeBySuffix(oldApkPath, 'arsc')))
        

def resDirSizeDiff():
    print(sizeFormat(getFileSizeByDir(newApkPath, 'res') - getFileSizeByDir(oldApkPath, 'res')))  
 
def dexSizeDiff():
    print(sizeFormat(getFileSizeBySuffix(newApkPath, 'dex') - getFileSizeBySuffix(oldApkPath, 'dex'))) 


def apkSizeDiff():
    print(sizeFormat(getsize(newApkFilePath) - getsize(oldApkFilePath)))
  


#通过后缀查询文件并统计总size
def getFileSizeBySuffix(path, suffix):
    size = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            if (name.endswith(suffix)):
                size = getsize(join(root, name))
    return size 

#通过文件夹名字查询文件并统计总size
def getFileSizeByDir(path, dirName):
    size = 0
    for root, dirs, files in os.walk(path):
        if (root.find(dirName) != -1):
            for name in files:
                size += getsize(join(root, name))
    return size 


apkSizeDiff()
