import os
import sys

#python3 call_demo.py /usr/local/j/delete/1208/dantu2/ 1208 1208.txt 1*2

res_dict = {
    "dantu2":"1*1",
    "dantu3":"1*1",
    "shang2xia2":"2*2",
    "shang3xia3":"3*2",
    "zuo1you1":"2*1",
    "shang1xia1":"1*2",
    "heng3he1":"3*1",
    "heng4he1":"4*1"

}
traffic_code = ['1208', '1301','1345','1352','1357','1625','0000']
def count_files(rootDir):
    dirs_all = []
    for root, dirs, files in os.walk(rootDir):
        if dirs != [] :
            for d in dirs:
                if d in traffic_code:
                    m = os.path.join(root,d)
                    m1 = m.replace('\\','/')
                    dirs_all.append(m1)
    return dirs_all
#遍历改目录下的所有文件
def file_list(path):
    dirs_all = count_files(path)
    delete_text = []
    #delete_text = ['1357_delete.txt', '1357_delete.txt', '1352_delete.txt', '1352_delete.txt', '1208_delete.txt', '1208_delete.txt', '1208_delete.txt', '1208_delete.txt', '1208_delete.txt', '1301_delete.txt', '1301_delete.txt', '1301_delete.txt', '1301_delete.txt', '1345_delete.txt', '1345_delete.txt', '1345_delete.txt', '1345_delete.txt', '1345_delete.txt', '1625_delete.txt', '1625_delete.txt', '1625_delete.txt']
    
    keep_pic_sums = 0  # 漏删除总图片
    for file_path in dirs_all:
        path2 = file_path.split('/')[-1] #算法ID
        path3_keep = str(file_path.split('/')[-1])+'_keep.txt'
        path3_delete = str(file_path.split('/')[-1])+'_delete.txt'
        type_files = os.listdir(file_path)
        for type_file in type_files:
            path1 = os.path.join(file_path,type_file)
            path4 = ""
            if 'keep' in path1:
                print('python3 call_demo.py %s %s %s %s'%(path1,path2,path3_keep,path4))

                os.system('python3 call_demo.py %s %s %s %s'%(path1,path2,path3_keep,path4))

            else:
                print('python3 call_demo.py %s %s %s %s'%(path1,path2,path3_delete,path4))
                os.system('python3 call_demo.py %s %s %s %s'%(path1,path2,path3_delete,path4))
                delete_text.append(path3_delete)

    formatList_delete = list(set(delete_text))
    for d in formatList_delete:
        keep_pic_nums = 0  # 总图片
        delete_pic_nums = 0  # 总图片
        keep_nums = 0  # 误删除
        delete_nums = 0  # 漏删除
        delete_not_nums = 0  #未知图片
        keep_not_nums = 0
        delete_pic_sum1s = 0
        keep_pic_sum1s = 0
        delete_num = os.popen('cat %s |grep "#1"|wc -l' %d)  # 漏删除
        delete_num = int(delete_num.read())

        delete_pic_sum = os.popen('cat %s |grep "#"|wc -l' %d)  # # 总图片
        delete_pic_sum = int(delete_pic_sum.read())

        delete_not_pic_sum = os.popen('cat %s |grep "#0"|wc -l' %d)  # 未判定图片
        delete_not_pic_sum = int(delete_not_pic_sum.read())

        delete_not_nums += delete_not_pic_sum
        delete_nums += delete_num
        delete_pic_nums += delete_pic_sum  # 总图片
        a = str(d.split('_')[0])+'_keep.txt'
        try:
            keep_num = os.popen('cat %s |grep "#1"|wc -l' %a)  # 误删除
            keep_num = int(keep_num.read())
            
            keep_pic_sum = os.popen('cat %s |grep "#"|wc -l' %a)  # 总图片
            keep_pic_sum = int(keep_pic_sum.read())

            keep_not_pic_sum = os.popen('cat %s |grep "#0"|wc -l' %a)  # 未判定图片
            keep_not_pic_sum = int(keep_not_pic_sum.read())
            
            keep_not_nums += keep_not_pic_sum
            keep_nums += int(keep_num)
            keep_pic_nums += keep_pic_sum  # 总图片
        except Exception as e:
            pass
        print('\n')
        print('算法ID为%s'%str(d.split('_')[0]))
        print('总图片为%s'%str(keep_pic_nums+delete_pic_nums))
        print("应该保留图片%s张，实际保留图片%s张,实际删除%s张,未判定图片%s" % (str(keep_pic_nums), str(int(keep_pic_nums) - int(keep_nums)-int(keep_not_nums)), str(keep_nums),str(keep_not_nums)))
        print("应该删除%s图片，实际保留%s张图片,实际删除%s张,未判定图片%s" % (str(delete_pic_nums), str(int(delete_pic_nums) - int(delete_nums)-int(delete_not_nums)),str(delete_nums), str(delete_not_nums)))
        print(str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)),str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)+int(int(delete_pic_nums) - int(delete_nums)-int(delete_not_nums))),str(int(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums))/int(int(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)+int(int(delete_pic_nums) - int(delete_nums)-int(delete_not_nums))))))
        try:
            print("算法删除检出率为%s/%s=%s"%(str(delete_nums),str(delete_pic_nums),str(int(delete_nums)/int(delete_pic_nums))))
        except Exception as e:
            print("算法删除检出率为%s/%s=%s"%(str(delete_nums),str(delete_pic_nums),str('0')))
        try:
            print("算法删除准确率为%s/%s=%s"%(str(delete_nums),str(int(delete_nums)+int(keep_nums)),str(int(delete_nums)/int(int(delete_nums)+int(keep_nums)))))
        except Exception as e:
            print("算法删除准确率为%s/%s=%s"%(str(delete_nums),str(int(delete_nums)+int(keep_nums)),str('0')))

        try:
            print("算法保留检出率为%s/%s=%s"%(str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)),str(keep_pic_nums),str(int(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums))/int(keep_pic_nums))))
        except Exception as e:
            print("算法保留检出率为%s/%s=%s"%(str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)),str(keep_pic_nums),str('0')))
        try:
            print("算法保留准确率为%s/%s=%s"%(str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)),str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)+int(keep_nums)),str(int(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums))/int(int(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)+int(keep_nums))))))
        except Exception as e:
            print("算法保留准确率为%s/%s=%s"%(str(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)),str(int(int(keep_pic_nums)-int(keep_nums)-int(keep_not_nums)+int(keep_nums)),str('0')))


file_list(sys.argv[1])
