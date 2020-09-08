import os
import sizeFormat

oldApkPath = '/Users/liulei/StudioProjects/apksize/oldapk/TPPcn227200vc10.0.6vn1006'


def test():
    for root, dirs, files in os.walk(oldApkPath):
        print(root)
        for name in files:
            if (name.endswith('arsc')):
                print(name)
                print(sizeFormat.sizeFormat(os.path.getsize(os.path.join(root, name))))
       


test()