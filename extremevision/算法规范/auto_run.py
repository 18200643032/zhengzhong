import os
import time
import re
import json
import unittest
from top_config import save_top, write_res, Config_file_set
from config import Config_file

# 未授权返回-999
def not_function():
    os.system("cd /usr/local/ev_sdk/bin;./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1 | tee /zhengzhong/res_2.txt")
    with open("/zhengzhong/res_2.txt", 'r') as f:
        con1 = f.read().splitlines()
    pattern_xmin = 'return (\D?\d*)'
    a = int(re.findall(pattern_xmin, str(con1))[0])
    if a == -999:
        pass
    else:
        write_res("未实现未授权返回-999:ERROR\n")
#授权
def authorization():
    os.system("bash /zhengzhong/sh/1.sh")
not_function()
authorization()
class Auto_run(unittest.TestCase):


    def testmd5(self):
        os.popen("md5sum /usr/local/")

# 验证工程路径与规范一致
    def test_project_path(self):
        path_sdk = "/usr/local/ev_sdk/"
        if os.path.exists(path_sdk):
            pass
        else:
            write_res("验证工程路径与规范不一致:ERROR\n")
            exit()
    # 验证test.cpp和makefile
    def test_make_file(self):
        os.system("rm -rf /usr/local/ev_sdk/test/* ")
        os.system("cp /zhengzhong/sdk3_0/* /usr/local/ev_sdk/test/")
        code = os.system("cd /usr/local/ev_sdk/test;make clean;make -j8")
        if code == 0:
            pass
        else:
            write_res("test.cpp和makefile:ERROR\n")
    # test-ji-api和license.txt移动到任意目录，都需要能够正常运行catalogue目录
    def test_catalogue(self):
        a1 = os.system("cp /usr/local/ev_sdk/bin/test-ji-api /root/;cp /usr/local/ev_sdk/bin/license.txt /root/;cd /root/;./test-ji-api -f 1 -i /zhengzhong/1.jpg")
        if a1 == 0:
           pass
        else:
            write_res("移动到任意目录:ERROR\n")

    # libjo.so链接所有库
    def test_libji_connect(self):
        a1 = os.popen("ldd /usr/local/ev_sdk/lib/libji.so|grep not")
        a2 = a1.readlines()
        if a2:
            write_res("libji.so链接所有库:ERROR\n")
        else:
            pass

    # 方法结果是否一致,结果分辨率是否一致
    def test_resolution(self):
        # 调用运行的方法。
        os.system(f"cd /usr/local/ev_sdk/bin/;./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res1.jpg 2>&1 | tee /zhengzhong/res_1.txt")
        os.system(f"cd /usr/local/ev_sdk/bin/;./test-ji-api -f 2 -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1 | tee /zhengzhong/res_2.txt")
        with open("/zhengzhong/res_1.txt", 'r') as f:
            con1 = f.read().splitlines()
        pattern_xmin = 'json:.\{(.*)\}'
        res_xmins1 = "{" + re.findall(pattern_xmin, str(con1))[0].replace("\\t", "").replace(" ", "").replace("','","") + "}"
        res1 = json.loads(res_xmins1)
        with open("/zhengzhong/res_2.txt", 'r') as f:
            con2 = f.read().splitlines()
        pattern_xmin2 = 'json:.\{(.*)\}'
        res_xmins2 = "{" + re.findall(pattern_xmin2, str(con2))[0].replace("\\t", "").replace(" ", "").replace("','","") + "}"
        res2 = json.loads(res_xmins2)
        if res1 == res2:
            a = os.popen("file /zhengzhong/res1.jpg").read()
            b = re.findall("[1-9]*x[1-9]*", a)
            a1 = os.popen("file /zhengzhong/res2.jpg").read()
            b1 = re.findall("[1-9]*x[1-9]*", a1)
            if b == b1:
                pass
            else:
                write_res("结果分辨率一致:ERROR\n")
        else:
            write_res("不同方法结果一致:ERROR\n")


    # 测试显存或者内存泄露
    def test_divulge(self):
        os.system("nohup; /usr/local/ev_sdk/bin/test-ji-api -f 5 -l /usr/local/ev_sdk/bin/license.txt -i /zhengzhong/1.jpg -r 33333 > run.log 2>&1 &")
        time.sleep(120)
        a = save_top()
        # 执行查询内存和显存的方法，返回值对比
        nvidia = a["nvidia"]
        internal = a["internal"]
        pid = a["pid"]
        n1 = 0
        i1 = 0
        for i in range(10):
            time.sleep(20)
            numbs = save_top()
            if numbs["nvidia"] > int(nvidia * 1.2):
                n1 += 1
            elif numbs["internal"] > float(internal * 1.2):
                i1 += 1
            else:
                pass
        if n1 > 5:
            write_res("有显存泄露:ERROR\n")
            if i1 > 5:
                write_res("有内存泄露:ERROR\n")
                os.system("kill -9 {}".format(pid))
            else:
                os.system("kill -9 {}".format(pid))
        else:
            if i1 > 5:
                write_res("有内存泄露:ERROR\n")
                os.system("kill -9 {}".format(pid))
                return False
            else:
                os.system("kill -9 {}".format(pid))
                return True


    # 未实现的函数返回 -2,已实现的返回 0 ，已实现的异常判断返回 -3
    def test_function(self):
        for i in range(1, 5):
            if i == 4:
                os.system("cd /usr/local/ev_sdk/bin;./test-ji-api -f {} -i /zhengzhong/1.mp4 -o /zhengzhong/1.avi 2>&1 | tee /zhengzhong/res_2.txt".format(i))
                with open("/zhengzhong/res_2.txt", 'r') as f:
                    con1 = f.read().splitlines()
                pattern_xmin = 'return (\D?\d*)'
                a = int(re.findall(pattern_xmin, str(con1))[0])
                write_res("已实现接口{}:返回{}\n".format(i, a))
                if os.path.exists("/zhengzhong/1.avi.txt"):
                    pass
                else:
                    write_res("video_file接口已实现:ERROR")

            os.system("cd /usr/local/ev_sdk/bin;./test-ji-api -f {} -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1 | tee /zhengzhong/res_2.txt".format(i))
            with open("/zhengzhong/res_2.txt", 'r') as f:
                con1 = f.read().splitlines()
            pattern_xmin = 'return (\D?\d*)'
            a = int(re.findall(pattern_xmin, str(con1))[0])
            write_res("已实现接口{}:返回{}\n".format(i, a))

    # 报警的code和alert_flag
    def test_police_check(self):
        # 准备两张图片，一个报警一个不报警
        os.system("cd /usr/local/ev_sdk/bin;./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1 | tee /zhengzhong/res_2.txt")
        with open("/zhengzhong/res_2.txt", 'r') as f:
            con1 = f.read().splitlines()
        code_state_pattern = 'code: (\D?\d*)'  # code获取
        code_state = int(re.findall(code_state_pattern, str(con1))[0])  # 0  1
        pattern_json = 'json:.\{(.*)\}'
        res_xmins1 = "{" + re.findall(pattern_json, str(con1))[0].replace("\\t", "").replace(" ", "").replace("','","") + "}"
        res1 = json.loads(res_xmins1)
        if code_state == 0:
            if res1["alert_flag"] == 1:
                pass
            else:
                write_res("code和alert_flag返回正常:ERROR\n")
        else:
            if res1["alert_flag"] == 0:
                pass
            else:
                write_res("code和alert_flag返回正常:ERROR\n")

    # 参数配置路径验证，是否存在readme，命名规范
    def test_config_path(self):
        name_config = "algo_config.json"
        name_readem = "README.md"
        path = "/usr/local/ev_sdk/config/"
        if os.path.exists(path):
            write_res("配置文件路径正确:OK\n")
            if os.path.exists(os.path.join(path, name_readem)):
                # 打开配置文件验证命令规范
                with open(os.path.join(path, name_config), "r") as f:
                    str_res = f.read()
                json_res = json.loads(str_res)
                state = True
                for i in json_res:
                    # 判断是不是全是小写
                    if i.islower():
                        pass
                    else:
                        state = False
                if state:
                    pass
                else:
                    write_res("配置文件内容命名规范错误:ERROR\n")

            else:
                write_res("配置文件readme路径错误:ERROR\n")

        else:
            write_res("配置文件路径错误:ERROR\n")


    # 配置文件修改是否生效

    def test_update_congfig_file(self):
        config_file = Config_file_set()
        # 验证GPU_id是否生效
        config_file.update_gpu_id(Config_file.config["gpu_id"])
        # 保存绘制roi区域绘制结果
        config_file.update_roi_res0(Config_file.config["draw_roi_draw_res"])
        # 绘制roi未绘制结果图片
        config_file.update_roi_res0(Config_file.config["draw_roi_not_res_path"])
        # 未绘制roi绘制结果的地址
        config_file.update_roi_res0(Config_file.config["draw_not_roi_draw_res"])
        # 都不绘制的地址
        config_file.update_roi_res0(Config_file.config["draw_not"])
        # 报警文字显示
        config_file.update_roi_res0(Config_file.config["words_true"])
        # 报警文字不显示
        config_file.update_roi_res0(Config_file.config["words_false"])
        # 默认值验证
        config_file.default(Config_file.algo_config_primay_json)
        # roi位置正确保存
        config_file.update_roi_res0(Config_file.config["roi_save_true"])
        # roi绘制多边型
        config_file.update_roi_res0(Config_file.config["roi_save_polygon"])
        # roi传入空默认分析全部区域
        config_file.update_roi_res0(Config_file.config["roi_save_null"])


    # 公私钥位置，名称验证
    def test_verification_pem(self):
        path1 = "/usr/local/ev_sdk/authorization/privateKey.pem"
        path2 = "/usr/local/ev_sdk/authorization/pubKey.pem"
        if os.path.exists(path1):
            if os.path.exists(path2):
                pass
            else:
                write_res("公私钥位置，名称验证:ERROR\n")
        else:
            write_res("公私钥位置，名称验证:ERROR\n")


    # 模型路径，名称验证
    def test_verification_modle(self):
        path = "/usr/local/ev_sdk/model/"
        if os.path.exists(path):
            a = os.popen("ls {}|grep .dat".format(path))
            b = a.readlines()
            if b == []:
                write_res("模型路径，名称验证:ERROR\n")
            else:
                pass

if __name__ == "__main__":
    unittest.main()