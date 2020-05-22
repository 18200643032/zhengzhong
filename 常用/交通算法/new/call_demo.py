# import requests
# import json
# import base64
# path = r"C:\Users\Administrator\Desktop\川R6D885_0.24051137535651856_R0201.jpg"
# url = "http://192.168.1.136:37751/api/analysis"
# #川R6D885

# headers = {"Content-Type":"application/json;charset=utf-8"}

# f = open(path,"rb")
# image = f.read()
# f.close()

# imgdata = base64.encodebytes(image).decode()
# body = {
# "recognitionMode":3,
# "plateLicense":"川R6D885",
# "violationAction":"1208",
# "imageMode":1,
# "images":[
# {
# "imageData":imgdata,
# "imageSyntheticMode":""}]
# }

# response = requests.post(url,data=json.dumps(body),headers=headers)
# print(response.text)

# images.append(
#     {
# "imageData":imgdata,
# "imageSyntheticMode":""})

# 3
# "images":[
# {
# "imageData":imgdata,
# "imageSyntheticMode":""},
# {
# "imageData":imgdata,
# "imageSyntheticMode":""},
# {
# "imageData":imgdata,
# "imageSyntheticMode":""},
# ]


# import os
# a1 = os.listdir("/usr/local/ev_sdk/demo")
# for i in a1:
#     a = "./test-ji-api -f 1 -i ../demo/%s -o ../res/%s 2>&1 | tee %s.txt"%(i,i,i.split(".")[0])
#     print(a)
#     #os.system(a)

# ['\', \'\\t"alert_flag":\\t1,\', \'\\t"alert_num":\\t1,\', \'\\t"info":\\t[{\', \'\\t\\t\\t"x":\\t535,\', \'\\t\\t\\t"y":\\t146,\', \'\\t\\t\\t"width":\\t73,\', \'\\t\\t\\t"height":\\t133,\', \'\\t\\t\\t"confidence":\\t0.919455,\', \'\\t\\t\\t"name":\\t"helmet",\', \'\\t\\t\\t"color":\\t"null",\', \'\\t\\t\\t"alert_tag":\\t0\', \'\\t\\t']
# res_xmin=','
# "alert_flag":1,
# "alert_num":1,
# "info":[{','"x":535,','"y":146,','"width":73,','"height":133,','"confidence":0.919455,','"name":"helmet",','"color":"null",','"alert_tag":0','

import os
import re
import json
# # with open(r"C:\Users\Administrator\Desktop\DZ6V0243.log","r") as f:
# with open(r"C:\Users\Administrator\Desktop\DZ6V0243.log", 'r') as f:
#     con = f.read().splitlines()
#     # print(con)
#     pattern_xmin = 'json:.\{(.*)\}'
#     res_xmins = "{"+re.findall(pattern_xmin, str(con))[0].replace("\\t","").replace(" ","").replace("','","")+"}"
#     res = json.loads(res_xmins)
#     res_indexs = res.get("info")
#     pic_persons = []
#     for res in res_indexs:
#         x = res.get('x')
#         y = res.get('y')
#         xmax = res.get('width') + x
#         ymax = res.get('height') + y
#         name = res.get('name')
#         pic_persons.append({name: (int(x), int(y), int(xmax), int(ymax))})

#      # 得到图片中总共识别的数目
#     pic_realize_nums = len(pic_persons)

#     xml_persons = []
#     with open(xml_with_dir, 'r',encoding='utf-8') as f:
#         soup = BeautifulSoup(f, 'lxml')
#         objects = soup.find_all("object")
#         for obj in objects:
#             kinds = list(obj.children)[1].get_text()

#             # print(obj.bndbox)
#             x = obj.bndbox.xmin.get_text()
#             y = obj.bndbox.ymin.get_text()
#             width = int(obj.bndbox.xmax.get_text())
#             height = int(obj.bndbox.ymax.get_text())
    

#     print(type(res_xmins))
#     exit()
 

from bs4 import BeautifulSoup
import os
from 

path = r"C:/Users/Administrator/Desktop/r/res"
with open(r"C:\Users\Administrator\Desktop\hat_testdata.xml","rb") as f:
    a1 = f.read()
soup = BeautifulSoup(a1,"lxml")
objects = soup.find_all("image")

#戴安全帽总数
all_colors_right = 0
# 未带安全帽的准确率
all_heads_right = 0
# 忽略颜色准确率,识别正确,颜色错误
all_without_colors_right = 0
# 不是安全帽识别为安全帽
all_not_hats = 0
for xmls in objects:
    txt = xmls.get("name").split("/")[1].split(".")[0]+'.txt'
    print(txt)
    # print(xmls)
    xmls_list = xmls.find_all("box")
    # print(xmls_list)
    xml_persons = []
    for i in xmls_list:
        name = i.get("label")
        x = i.get("xtl")
        y = i.get("ytl")
        xmax = i.get("xbr")
        ymax = i.get("ybr")
        # print(xmax,ymax)
        if name != "person":
            xml_persons.append({name: (int(float(x)), int(float(y)), int(float(xmax)), int(float(ymax)))})
            if name == "head":
                all_heads_right+=1
            else:
                all_colors_right+=1

    with open(path+"/"+txt, 'r') as f:
        con = f.read().splitlines()
    # print(con)
    pattern_xmin = 'json:.\{(.*)\}'
    res_xmins = "{" + re.findall(pattern_xmin, str(con))[0].replace("\\t", "").replace(" ", "").replace("','", "") + "}"
    res = json.loads(res_xmins)
    res_indexs = res.get("info")
    pic_persons = []
    for res in res_indexs:
        x = res.get('x')
        y = res.get('y')
        xmax = res.get('width') + x
        ymax = res.get('height') + y
        name = res.get('name')
        pic_persons.append({name: (int(x), int(y), int(xmax), int(ymax))})

    # print(xml_persons)
    print(pic_persons)
    print(all_colors_right)
    print(all_heads_right)


    for pic_person in pic_persons:
        # 获取每一个的类型:color head之类
        pic_which_kind = list(pic_person.keys())[0]
        print(pic_which_kind)

        # 获取坐标pic
        pic_coordinate = pic_person.get(pic_which_kind)
        print(pic_coordinate)
        exit()
        for xml_person in xml_persons:
            # 这个是xml类型包括 head color
            xml_which_kind = list(xml_person.keys())[0]
            # 获取xml坐标
            xml_coordinate = xml_person.get(xml_which_kind)

  
            iou = compute_iou2(pic_coordinate, xml_coordinate)
            print(iou)
     
            # 第一步先比较iou占比,如果iou大于0在比较类型
            if iou > IOU_SET:
                xml_which_kind = xml_which_kind.lower()
                # 判断pic是否是head 图片中没有戴安全帽则为Null
                if pic_which_kind == 'Null':
                    all_heads_right += 1
                    pic_realize_nums -= 1
                    continue
                # 判断颜色是否识别正确
                elif xml_which_kind.startswith(pic_which_kind):
                    all_colors_right += 1
                    pic_realize_nums -= 1
                    continue
                else:
                    all_without_colors_right += 1
                    pic_realize_nums -= 1
    all_not_hats += pic_realize_nums





import requests
import base64



url = "http://127.0.0.1:80/vehicle/v1/recognize"
path = '/usr/ev_sdk/demo/'
# a1 = listdir(path)
# for img in a1:
#     f=open(os.path.join(path,img),'rb')
#     image=f.read()
#     f.close()
body = {"sid":"123456","images":[{"trackId":"1"},]}
# imgdata = base64.b64encode(image).decode()

body["images"][0]["base64"] ="12345"
print(body)