import os

def rename():
    i = 0
    path = (r'C:\Users\Administrator\Desktop\handpick_test_data\handpick_test_data')
    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）
    for files in filelist:  # 遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)  # 原来的文件路径

        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue
        filename = os.path.splitext(files)[0]  # 文件名

        filetype = '.avi'  # 文件扩展名 这里以图片为例 可以顺便修改格式
        Newdir = os.path.join(path, filename+str(i) + filetype)  # 新的文件路径
        os.rename(Olddir,Newdir)  # 重命名