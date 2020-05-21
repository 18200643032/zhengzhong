import requests

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

#
