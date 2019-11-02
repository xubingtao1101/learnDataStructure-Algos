import os
'''
    考虑到文件系统表示的递归特性，
    许多常见的行为比如目录的复制、删除，都可以很方便的用递归来实现
    os.path.getsize(path) 
    os.path.isdir(path)
    os.listdir(path)
    os.path.join(path,filename)
'''


def disk_usage(path):
    """返回一个文件夹下所有文件（包括子文件夹）所占空间大小"""
    total = os.path.getsize(path)
    if os.path.isdir(path): 
        for filename in os.listdir(path):
            childPath = os.path.join(path, filename)
            total += disk_usage(childPath)
    # 第15行和第18行是递归关键
    # 第17行用于拼接递归来的本层文件夹的路径和本层文件夹中的文件名，用于给第14行计算大小
    print(f"{total:<7}", path)
    return total

if __name__ == "__main__":
    path = "C:\\Users\\swagg\\Desktop\\Learn"
    disk_usage(path)