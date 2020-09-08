#文件大小格式化
def sizeFormat(size):
    if size < 1000:
        return size + 'B'
    elif size < 1000000:
        return float(size/1000) + 'KB'
    elif size < 1000000000:
        return float(size/1000000) + 'MB'
    elif size < 1000000000000:
        return float(size/1000000000) + 'GB'


