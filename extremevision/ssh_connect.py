import paramiko
class SSH_demo():
    """docstring for ClassName"""
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname="192.168.1.103",port=22,username="extremevision",password="123")




    #执行命令
    def set_com(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command("%s /"%cmd,get_pty=True)
        res = stdout.read().decode("utf-8")
        return res


    def dowm(self):
        self.ssh.close()





demo = SSH_demo()
# print(demo.set_com("top \n"))
print(demo.set_com("python3 /home/extremevision/zz/docker_run.py ccr.ccs.tencentyun.com/source/dev_crowd_gpu_sdk3.0_modj_lic1b:v1.1.2"))

demo.dowm()