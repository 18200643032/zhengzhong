#巡检计划模块
import json
import datetime
import requests
from config.config import Plan_management_Config
import time
from config.login import login
headers = login()

#查看计划，参数的计划名，返回id
def look_now(name):
    params= {
        "1":"1",
        "type":"1,2,3,4"
    }
    a1 = requests.get(Plan_management_Config.look_now_url,params=params,headers=headers)
    res_list = a1.json().get("responseContent")
    for i in res_list:
        if i["name"] == name:
            return i["id"]
# print(look_now("e1"))
#发布计划
def put_task(id):
    params = {
        "planId":id
    }
    requests.put(Plan_management_Config.put_task_url,headers=headers,params=params)

#添加计划
def add_task(number):
    #参数是要巡检的次数
    now = time.time() + 600
    start_time = []
    for i in range(int(number)):
        now += 600
        now_date_time = datetime.datetime.fromtimestamp(now)
        res_time = now_date_time.strftime("%H:%M")
        print('%s' % res_time)
        start_time.append(res_time)

    a = '{"type": "1","setting": "[{\\"field\\": 1,\\"startTime\\": %s}]","count": %s}' % (start_time, len(start_time))
    b = a.replace("\'", "\\\"")
    data = {
        "id":"",
        "name": "e1",
        "starttime": "2020-06-04 00:00:00",
        "type": 1,
        "endtime": "2020-06-04 23:59:59",
        "lineOfPlanList": [{"lineid": "320682185440616448"}],
        "operatgroup": "320682557207212032",
        "state": 1,
        "operator": "320678669951430656",
        "calendarid": 1,
        "autorenewal": True,
        "enable": False,
        "usehour": 1,
        "autorenewalday": 0,
        "grouptype": 1,
        "frequency": json.loads(b)

    }
    a1 = requests.post(Plan_management_Config.add_task_url,headers=headers,json=data)
    print(a1.json())
    #发布计划
    id = look_now(data["name"])
    put_task(id)

#10个测试时间
add_task(10)