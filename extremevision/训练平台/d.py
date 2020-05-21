
import random
import requests
from config import Config_cvmat
import time


#登录
def login(username,password):
    data = {
        "username":username,
        "password":password
    }
    a1 = requests.post(Config_cvmat.login_url,json=data,headers=Config_cvmat.headers)
    token = a1.json().get("token_info").get("access_token")
    Config_cvmat.headers["Authorization"] = "Bearer " + token

#获取实例ID

def paginate(username, password):
    login(username, password)
    params = {
        "type":"competition",
        "current":1,
        "pageSize":5

    }
    a1 = requests.get(Config_cvmat.paginate_url,params=params,headers=Config_cvmat.headers)
    shili_id = a1.json().get("list")[0].get("id")
    return shili_id
#发起训练
def generate123(username, password):
    shili_id = paginate(username, password)
    # url = f"/api/online-coding/instance/{shili_id}/generate-train-mirror"
    # a1 = requests.post(Config_cvmat.generate_url+url,headers=Config_cvmat.headers)
    # print(a1.json())
    # time.sleep(60)
    ll_url = f"/api/online-train/instance/train/{shili_id}/model-dir"
    requests.get(Config_cvmat.generate_url+ll_url,headers=Config_cvmat.headers)
    #发起训练
    train_url = f"/api/online-train/instance/{shili_id}/train"
    data = {
        "exec_command":"bash /project/train/src_repo/train.sh"
    }
    a1 = requests.post(Config_cvmat.generate_url+train_url,data=data,headers=Config_cvmat.headers)
    print(a1.json())
    return shili_id


#发起测试
def generate(username, password):
    shili_id = generate123(username, password)
    time.sleep(1500)
    for i in range(10):
        url = f"/api/online-train/instance/{shili_id}/sdk-test"
        data = {
            "has_model": 1,
             "model_dir_ids": [3627], "algorithm_name": f"asdsad{random.randint(555,666)}",
             "algorithm_tag": f"asdasd{random.randint(555,666)}"
        }
        a1 = requests.post(Config_cvmat.generate_url+url,json=data, headers=Config_cvmat.headers)
        time.sleep(100)
        print(a1.json())

if __name__ == "__main__":
    for i in range(60):
        username = "zhong910386943"
        password = "123456"
        generate(username,password)
        time.sleep(10)

