from fileSizeCompare import fileDirSizeDiff, fileSizeDiff
from sizeFormat import sizeFormat
import os

oldApkPath = '/Users/liulei/StudioProjects/apksize/oldapk/TPPcn227200vc10.0.6vn1006'
newApkPath = '/Users/liulei/StudioProjects/apksize/newapk/TPPcn228200vc10.1.1vn1011'

def arscFileSizeDiff(oldFile, newFile):
    return fileSizeDiff(oldFile, newFile)

def resDirSizeDiff(oldResFileDir, newResFileDir):
    return fileDirSizeDiff(oldResFileDir, newResFileDir)    


