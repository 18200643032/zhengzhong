import requests
from config.login import login
#任务处理
from config.config import Inspection_tasks_Config
headers = login()
#搜索
def search():
    params = {
        "1":1,
        "keyvalue":"aaa",  #搜索关键字
        "starttime":"",#开始时间
        "endtime":"",#结束时间
        "state":1 ,  #状态选择，1,2,3
        "isabort":False,
        "showdeadline":False,
        "pageCount":10,
        "pageIndex":1
    }
    a1 =requests.get(Inspection_tasks_Config.search_url,params=params,headers=headers)
    print(a1.json())

#手动创建巡检任务
def creat_task():
    data = {
        "id":"",
        "name": "测试2",#任务名称
        "starttime": "2020-06-03 16:31:52",#执行时间
        "type": 1,#执行组
        "operatgroup": "320682557207212032",
        "operator": "320678669951430656",
        "grouptype": 1,
        "planid": 0,
        "lineid": "320682185440616448",
    }
    a1 = requests.post(Inspection_tasks_Config.creat_task_url,headers=headers,json=data)
    print(a1.json())
