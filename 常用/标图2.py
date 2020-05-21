import cv2
import os,shutil
from bs4 import BeautifulSoup
p1 = r'C:\Users\Administrator\Desktop\xml'  #xml
p3 = r'C:\Users\Administrator\Desktop\jpg'   #jpg
# p4 = r'C:\Users\Administrator\Desktop\res_jpg'   #jpg
# p2 = r'F:\各类算法\占道识别\demo\jpg\1.txt'   #jpg
m = 0
path = os.listdir(p1)
for pa in path:

    ll = pa.split('.')[0]
    a = open(os.path.join(p1,pa),'rb')
    soup = BeautifulSoup(a.read(),features="lxml")
    s1 = soup.find_all('bndbox')
    for i in s1:

        a1 = i.find_all('xmin')[0].string
        a2 = i.find_all('ymin')[0].string
        a3 = i.find_all('xmax')[0].string
        a4 = i.find_all('ymax')[0].string
        m += 1
        print(ll)
        cv2.namedWindow("Image")  # 创建窗口

        img = cv2.imread(os.path.join(p3, ll+'.jpg'))  # 读取图像

        try:
            cv2.rectangle(img, (int(a1), int(a2)), (int(a3), int(a4)), (0, 255, 0), 2)
            cv2.imshow('Image', img)
            cv2.imwrite(os.path.join(p3, ll+'.jpg'), img)
            # print(os.path.join(p2, ll+'.jpg'))

        except Exception as f:
            print(f)
            continue

