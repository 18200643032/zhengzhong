import requests
from config import Config
import time

#登录
def login(username,password):
    data = {
        "username":username,
        "password":password
    }
    a1 = requests.post(Config.login_url,json=data,headers=Config.headers)
    token = a1.json().get("token_info").get("access_token")
    Config.headers["Authorization"] = "Bearer " + token

#获取实例ID

def paginate(username, password):
    login(username, password)
    params = {
        "type":"competition",
        "current":1,
        "pageSize":5

    }
    a1 = requests.get(Config.paginate_url,params=params,headers=Config.headers)
    shili_id = a1.json().get("list")[1].get("id")
    return shili_id

#构建训练镜像
def generate(username, password):
    shili_id = paginate(username, password)
    url = f"/api/online-coding/instance/{shili_id}/generate-train-mirror"
    a1 = requests.post(Config.generate_url+url,headers=Config.headers)
    print(a1.json())
    time.sleep(60)
    ll_url = f"/api/online-train/instance/train/{shili_id}/model-dir"
    requests.get(Config.generate_url+ll_url,headers=Config.headers)
    #发起训练
    train_url = f"/api/online-train/instance/{shili_id}/train"
    data = {
        "exec_command":"bash /project/train/src_repo/train.sh"
    }
    a1 = requests.post(Config.generate_url+train_url,data=data,headers=Config.headers)
    print(a1.json())
    exit()

if __name__ == "__main__":
    for i in range(1,11):
        username = f"zheng{i}"
        print(username)
        password = "123456"
        generate(username,password)





