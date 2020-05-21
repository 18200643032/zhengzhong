import os
import json

# 运行的接口
# 传入参数是接口对应的数字
def run_connector(num):
    state = os.system(
        f"./test-ji-api -f {num} -i /zhengzhong/1.jpg -o /zhengzhong/res1.jpg 2>&1 | tee /zhengzhong/res_{num}.txt")
    return state

#写入结果接口的方法
def write_res(res):
    with open("/zhengzhong/project_res.txt","a") as f:
        f.write(res)
# 计算内存显存的方法
def save_top():
    top = {}
    nvidia_list = []
    internal_list = []
    pid_list = []
    for i in range(200):
        pid_name = "test-ji-api"
        # 获取进程pid
        a1 = str(os.popen("pidof {}".format(pid_name)).read().replace('\n', ""))
        # 查询进程的内存情况
        a2 = str(os.popen("top -n 1 -p %s |grep %s  |awk '{print $11}'" % (a1, pid_name)).read().replace('\n', "").replace(" ", ""))
        # 查询显存占用
        a3 = str(os.popen("nvidia-smi |grep Default|awk '{print $9}'").read().split('M')[0].replace('\n', "").replace(" ",""))
        pid_list.append(a1)
        internal_list.append(a2)
        nvidia_list.append(a3)

    top["pid"] = int(max(pid_list))
    top["nvidia"] = int(max(nvidia_list))
    top["internal"] = float(max(internal_list))
    return top


# 配置文件修改类
class Config_file_set(object):
    """docstring for Config_file_set"""

    # 初始化方法。每次执行里面的方法，都会重新加载配置文件
    def __init__(self):
        self.path = "/usr/local/ev_sdk/config/algo_config.json"
        os.system("cp /zhengzhong/config/algo_config.json /usr/local/ev_sdk/config/")

    # 修改不同的配置，生成不同的结果文件,参数为配置的名称以及修改的值,为字典，例如{"draw_roi_area":1}
    def update_file_jpg(self, name):
        with open(self.path, "r") as f:
            a = f.read()
        json_str = json.loads(a)
        for key, vaule in name.items():
            json_str[key] = vaule
        with open(self.path, "w") as f2:
            json.dump(json_str, f2)


    # 更换GPUID
    def run_gpu_id(self):
        os.system("cd /usr/local/ev_sdk/bin;./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res2.jpg 2>&1 | tee /zhengzhong/res_2.txt ")
        with open("/zhengzhong/res_2.txt","r") as f:
            state = f.read()
        if "error" in state:
            write_res("gpu_id配置不生效")
        else:
            pass
        self.__init__()

    # 运行不同的配置，生成不同的结果文件
    def run_save_jpg(self, file_name):
        state = os.system(
            f"cd /usr/local/ev_sdk/bin;./test-ji-api -f 1 -i /zhengzhong/1.jpg -o /zhengzhong/res_jpg/{file_name}.jpg 2>&1 | tee /zhengzhong/res_2.txt")
        if state == 0:
            pass
        else:
            write_res(f"{file_name}图片保存失败")
        self.__init__()

    # 验证GPU id是否生效 {"gpu_id":1}
    def update_gpu_id(self, name):
        self.update_file_jpg(name)
        self.run_gpu_id()

    # 验证ROI和绘制结果图片的函数
    def update_roi_res0(self, name):
        self.update_file_jpg(name)
        jpg_name = ''
        for a, b in name.items():
            jpg_name += a + "_" + str(b)
        self.run_save_jpg(jpg_name)

    # 默认值,传入初始配置文件
    def default(self, primay_file):
        with open(self.path, "r") as f:
            a = f.read()
        json_str = json.loads(a)
        primay_file = json.loads(json.dumps(primay_file))
        for dic in primay_file:
            name = primay_file[dic]
            try:
                name1 = json_str[dic]
                if name != name1:
                    print(name,name1)
                    write_res("{}默认值有误:\n".format(dic))
                else:
                    pass
            except Exception as e:
                write_res("默认值没有{}----\n".format(dic))
