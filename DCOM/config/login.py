import requests


def login():
    url = "http://192.168.1.142/authentication"
    data = {
        "username":"admin",
        "password":"12345678"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
    a1 = requests.post(url,headers=headers,json=data)
    authen = a1.json().get("responseContent").get("token")
    headers["token"] = authen
    return headers