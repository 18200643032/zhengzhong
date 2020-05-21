import requests
import random
from config import Config

#登录
def login(username,password):
    data = {
        "username":username,
        "password":password
    }
    a1 = requests.post(Config.login_url,json=data,headers=Config.headers)
    token = a1.json().get("token_info").get("access_token")
    Config.headers["Authorization"] = "Bearer "+token


#获取邮箱验证码
def email_code():

    params = {
        "email":f"{random.randint(888888,9999999)}@qq.com"
    }
    # print(Config.headers)
    a1 = requests.get(Config.email_url,params=params,headers=Config.headers)
    email_state = a1.json().get("email_code")
    return [email_state,params["email"]]

#报名实例
def baoming(username,password):
    a = email_code()
    data = {
        "actual_name":"测试22123",
        "id_number":"1112321321",
        "email":a[-1],
        "verification_code":a[0],
        "is_college_recommend":0,
        "check":True
    }

    # print(Config.headers)
    a1 = requests.post(Config.baoming_url,data=data,headers=Config.headers)
    print(a1.json().get("msg"))

#创建实例
def instance(username,password):
    baoming(username,password)
    print(Config.headers)
    data = {
        "frame_id":2,
        "project_id":Config.baoming_url.split("/")[-1]
    }
    a1 = requests.post(Config.instance_url,data=data,headers=Config.headers)
    print(a1.json())
    #{'id': 650, 'name': '世界人工智能大赛菁英挑战赛-防疫赛题', 'status': 'disable_online_coding', 'created_at': '2020-05-16 12:04:42', 'updated_at': '2020-05-16 12:04:42', 'code': 20000, 'msg': '实例创建成功'}

#注册
def register():
    for i in range(1,51):
        data = {
            "username":f"zheng{i}",
            "password":"123456"
        }
        # data = {
        #     "username":f"zheng{i}",
        #     "mobile":f"182{random.randint(111111,999999)}21",
        #     "password":"123456",
        #     "verification_code":"123"
        # }
        # a1 = requests.post(Config.register_url,json=data,headers=Config.headers)
        instance(data["username"],data["password"])

register()

#构建训练镜像
#https://test.cvmart.net/api/online-coding/instance/658/generate-train-mirror
def generate(shili_id):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9lYWdsZS1uZXN0LWJhY2tlbmQtc2VydmljZS5kZXZsb3Auc3ZjLmNsdXN0ZXIubG9jYWxcL2FwaVwvbG9naW4iLCJpYXQiOjE1ODk2MTM2NjIsImV4cCI6MTU4OTYyMDg2MiwibmJmIjoxNTg5NjEzNjYyLCJqdGkiOiJaOWNrWXQ3aG9LdElMR082Iiwic3ViIjoxMjE2LCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.YotQPCZG1nbEN-XzPhA5v-NRHO50Q7jQRPIV3dy9x04"}
    url = f"https://test.cvmart.net/api/online-coding/instance/{shili_id}/generate-train-mirror"
    a1 = requests.post(url,headers=headers)
    print(a1.json())



#获取训练ID
#https://test.cvmart.net/api/online-train/instance/paginate?type=competition&current=1&pageSize=5
def paginate():
    url = "https://test.cvmart.net/api/online-train/instance/paginate"
    params = {
        "type":"competition",
        "current":1,
        "pageSize":5

    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9lYWdsZS1uZXN0LWJhY2tlbmQtc2VydmljZS5kZXZsb3Auc3ZjLmNsdXN0ZXIubG9jYWxcL2FwaVwvbG9naW4iLCJpYXQiOjE1ODk2MTM2NjIsImV4cCI6MTU4OTYyMDg2MiwibmJmIjoxNTg5NjEzNjYyLCJqdGkiOiJaOWNrWXQ3aG9LdElMR082Iiwic3ViIjoxMjE2LCJwcnYiOiIyM2JkNWM4OTQ5ZjYwMGFkYjM5ZTcwMWM0MDA4NzJkYjdhNTk3NmY3In0.YotQPCZG1nbEN-XzPhA5v-NRHO50Q7jQRPIV3dy9x04"}
    a1 = requests.get(url,params=params,headers=headers)
    shili_id = a1.json().get("list")[1].get("id")
    return shili_id

