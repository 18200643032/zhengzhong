import os
import sys

# python3 call_demo.py /usr/local/j/delete/1208/dantu2/ 1208 1208.txt 1*2

traffic_code = ['1208', '1301', '1345', '1352', '1357', '1625', '0000']


def count_files(rootDir):
    dirs_all = []
    for root, dirs, files in os.walk(rootDir):
        if dirs != []:
            for d in dirs:
                if d in traffic_code:
                    m = os.path.join(root, d)
                    m1 = m.replace('\\', '/')
                    dirs_all.append(m1)
    return dirs_all


# 遍历改目录下的所有文件
def file_list(path):
    dirs_all = count_files(path)
    delete_text = []
    for file_path in dirs_all:
        path2 = file_path.split('/')[-1]  # 算法ID
        path3_keep = str(file_path.split('/')[-1]) + '_keep.txt'
        path3_delete = str(file_path.split('/')[-1]) + '_delete.txt'
        type_files = os.listdir(file_path)
        for type_file in type_files:
            path1 = os.path.join(file_path, type_file)
            path4 = ""
            if 'keep' in path1:
                print('python3 call_demo.py %s %s %s ""' % (path1, path2, path3_keep))

                os.system('python3 call_demo.py %s %s %s ""' % (path1, path2, path3_keep))

            else:
                print('python3 call_demo.py %s %s %s ""' % (path1, path2, path3_delete))
                os.system('python3 call_demo.py %s %s %s ""' % (path1, path2, path3_delete))
                delete_text.append(path3_delete)

    formatList_delete = list(set(delete_text))
    for d in formatList_delete:
        keep_pic_nums = 0  # 保留总图片
        delete_pic_nums = 0  # 删除总图片
        keep_nums = 0  # 保留误删除
        delete_nums = 0  # 删除实际删除
        delete_not_nums = 0  # 删除未知图片
        keep_not_nums = 0  # 保留未知图片

        delete_num = os.popen('cat %s |grep "#1"|wc -l' % d)  # 漏删除
        delete_num = int(delete_num.read())

        delete_pic_sum = os.popen('cat %s |grep "#"|wc -l' % d)  # # 总图片
        delete_pic_sum = int(delete_pic_sum.read())

        delete_not_pic_sum = os.popen('cat %s |grep "#0"|wc -l' % d)  # 未判定图片
        delete_not_pic_sum = int(delete_not_pic_sum.read())

        delete_not_nums += delete_not_pic_sum
        delete_nums += delete_num
        delete_pic_nums += delete_pic_sum  # 总图片
        a = str(d.split('_')[0]) + '_keep.txt'
        try:
            keep_num = os.popen('cat %s |grep "#1"|wc -l' % a)  # 误删除
            keep_num = int(keep_num.read())

            keep_pic_sum = os.popen('cat %s |grep "#"|wc -l' % a)  # 总图片
            keep_pic_sum = int(keep_pic_sum.read())

            keep_not_pic_sum = os.popen('cat %s |grep "#0"|wc -l' % a)  # 未判定图片
            keep_not_pic_sum = int(keep_not_pic_sum.read())

            keep_not_nums += keep_not_pic_sum
            keep_nums += int(keep_num)
            keep_pic_nums += keep_pic_sum  # 总图片
        except Exception as e:
            pass
        print('\n')
        print('算法ID为%s' % str(d.split('_')[0]))
        # 应该保留总图片：keep_pic_nums
        # 实际保留图片：keep_pic_nums-keep_nums-keep_not_nums  #总图片-误删除-未知=实际
        keep_actual = keep_pic_nums - keep_nums - keep_not_nums
        # 实际删除图片：keep_nums
        # 未判定图片：keep_not_nums
        # ========================================================================
        # 应该删除总图片：delete_pic_nums
        # 实际保留图片：delete_pic_nums - delete_nums - delete_not_nums #总图片-误删除-未知=实际
        delete_actual = delete_pic_nums - delete_nums - delete_not_nums
        # 实际删除图片：delete_nums
        # 未判定图片：delete_not_nums
        print('总图片为%s' % str(keep_pic_nums + delete_pic_nums))
        print("应该保留图片%s张，实际保留图片%s张,实际删除%s张,未判定图片%s" % (keep_pic_nums, keep_actual, keep_nums, keep_not_nums))
        print("应该删除%s图片，实际保留%s张图片,实际删除%s张,未判定图片%s" % (delete_pic_nums, delete_actual, delete_nums, delete_not_nums))
        try:
            print("算法删除检出率为%s/%s=%s" % (delete_nums, delete_pic_nums, delete_nums / delete_pic_nums))
        except Exception as e:
            print("算法删除检出率为%s/%s=%s" % (delete_nums, delete_pic_nums, 0))
        try:
            print("算法删除准确率为%s/%s=%s" % (delete_nums, delete_nums + keep_nums, delete_nums / (delete_nums + keep_nums)))
        except Exception as e:
            print("算法删除准确率为%s/%s=%s" % (delete_nums, delete_nums + keep_nums, 0))

        try:
            print("算法保留检出率为%s/%s=%s" % (keep_actual, keep_pic_nums, keep_actual / keep_pic_nums))
        except Exception as e:
            print("算法保留检出率为%s/%s=%s" % (keep_actual, keep_pic_nums, 0))
        try:
            print("算法保留准确率为%s/%s=%s" % (
                keep_actual, keep_actual + delete_actual, keep_actual / (keep_actual + delete_actual)))
        except Exception as e:
            print("算法保留准确率为%s/%s=%s" % (keep_actual, keep_actual + delete_actual, 0))

            file_list(sys.argv[1])
