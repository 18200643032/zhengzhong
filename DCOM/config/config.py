import os

Config = "http://192.168.1.142/"
class Inspection_tasks_Config():

    #搜索的url
    search_url = Config+"api/v1/inspection/inspection_order"
    #创建任务的url
    creat_task_url = Config+"api/v1/inspection/inspection_order/manualAddOrder"

class Plan_management_Config():
    #添加任务的url
    add_task_url = Config+"api/v1/inspection/inspection_plan"
    #查询的url
    look_now_url = Config +"api/v1/inspection/inspection_plan"
    #发布计划
    put_task_url = Config +"api/v1/inspection//inspection_plan/publishPlan"