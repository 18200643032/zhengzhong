import sys
import base64
import os
import re
import requests
import json
import time
pattern1 = re.compile("^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4,5}[A-Z0-9挂学警港澳]{1}$")
pattern2 = re.compile("^[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$")

def call(image_name,hphm,wfxw,zpms_detail):
    url = 'http://127.0.0.1:80/api/analysis'
    body = {"recognitionMode": 3,"images":[]}
    headers = {"Content-Type":"application/json;charset=utf-8"}
    for i in range(len(image_name)):
        f=open(image_name[i],'rb')
        image=f.read()
        f.close()
        imgdata = base64.b64encode(image).decode()
        dict_img = {"imageData":imgdata,"imageSyntheticMode":""}
        body["images"].append(dict_img)
    
    
    body["imageMode"]=1  #base64对应的1，url对应2
    body["plateLicense"]=hphm  #车牌
    body["violationAction"]=wfxw  #识别代码
    response = requests.post(url, data = json.dumps(body), headers = headers)
    print(response.text)
   # exit()
    return response.text

def find_group_image(pre_name, images):
    res = []
    for image in images:
        if image.startswith(pre_name):
            res.append(image)
    return res

def test_multi_image(in_folder, wfxw, save_file, zpms_detail):
    f=open(save_file,'a')
    has_test_images = []
    images=os.listdir(in_folder)
    suanfa_id = in_folder.split('/')[-3] #算法ID 
    sumber = 0              #图片总数量
    start_time = time.time()
    for image in images:
        if not image.endswith('jpg'):
            continue
        sumber+=1
        # pre_name, image_form =  image.split('.')
        pre_name = image[:-4]
        if pre_name[:-5] in has_test_images:
            continue
        print('90--->',pre_name[:-5])
        has_test_images.append(pre_name[:-5])
        pos = 0
        for im in image.split("_"):
            print('match ',im)
            res1 = re.search(pattern1, im)
            res2 = re.search(pattern2, im)
            if res1 != None or res2 != None:
                if res1 != None:
                    hphm= res1.group()
                else:
                    hphm= res2.group()
                image_names = find_group_image(pre_name[:-5], images)
                image_names = [os.path.join(in_folder,image_name) for image_name in image_names]
                image_names = sorted(image_names)
                print ('==================================',image_names)
                print("done: ", sumber)
                ret=call(image_names,hphm,wfxw,zpms_detail)
                ret=json.loads(ret)
               # exit()
                result=ret["data"]
                #"data":    {
                    #"deleteResult":    0,
                    #"foundPlateLicense":   "å†€D715BU",
                    #"recallReason":    "R0503",
                    #"recallResult":    1,
                    #"recognitionMode": 3,
                    #"violationAction": "1301"
                #}

                
                if result["deleteResult"]==1:   #删除
                    for image in image_names:
                        f.write(image+'#1#'+result['deleteReason']+'\n')
                elif result["recallResult"]==1:  #找回
                    print("ok")
                    for image in image_names:
                        f.write(image+'#2#'+result['recallReason']+'\n')
                else:
                    print(123)
                    for image in image_names: #未知
                        f.write(image+'#0#0\n')
    stop_time = time.time()     #结束时间
    tol_time = stop_time-start_time
    if int(tol_time) == 0:
        tol_time = 1.0
    with open('time.txt', 'a') as f:
        f.write(str('算法ID：%s 总图片：%s 总时间：%s 每一张图片运行时间%s'%(str(suanfa_id),str(sumber),str(tol_time),str(sumber/int(tol_time)))+'\n'))
    f.close()

if __name__=='__main__':
    in_folder   = sys.argv[1].rstrip('/')+'/'
    wfxw        = sys.argv[2]
    save_file   = sys.argv[3]
    zpms_detail = sys.argv[4] #  "2*2"
    # test_single_image(in_folder, wfxw, save_file, zpms_detail)
    test_multi_image(in_folder, wfxw, save_file, zpms_detail)

