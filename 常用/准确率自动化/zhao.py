from bs4 import BeautifulSoup
import os,re,json
from iou import compute_iou2

IOU_SET = 0.2

path = r"C:/Users/Administrator/Desktop/r/res"
with open(r"C:\Users\Administrator\Desktop\hat_testdata.xml", "rb") as f:
    a1 = f.read()
soup = BeautifulSoup(a1, "lxml")
objects = soup.find_all("image")

# 戴安全帽总数

all_colors_right = 0
# 未带安全帽的准确率
all_heads_right = 0
# 忽略颜色准确率,识别正确,颜色错误
all_without_colors_right = 0
# 不是安全帽识别为安全帽
all_not_hats = 0
all_heads_right1 = 0
all_colors_right1 = 0





#识别错误的
error_pic = 0
#识别安全帽正确的
true_hat_pic = 0
#识别head正确的
true_head_pic = 0


for xmls in objects:
    jpg = xmls.get("name").split("/")[1]
    txt = xmls.get("name").split("/")[1].split(".")[0] + '.txt'
    xmls_list = xmls.find_all("box")
    xml_persons = []

    for i in xmls_list:
        name = i.get("label")
        x = i.get("xtl")
        y = i.get("ytl")
        xmax = i.get("xbr")
        ymax = i.get("ybr")
        if name != "person":
            xml_persons.append({name: (int(float(x)), int(float(y)), int(float(xmax)), int(float(ymax)))})
            if name == "head":
                all_heads_right1 += 1
            else:
                all_colors_right1 += 1

    try:
        with open(path + "/" + txt, 'r') as f:
            con = f.read().splitlines()
        # print(con)
        pattern_xmin = 'json:.\{(.*)\}'
        res_xmins = "{" + re.findall(pattern_xmin, str(con))[0].replace("\\t", "").replace(" ", "").replace("','", "") + "}"
        res = json.loads(res_xmins)
        res_indexs = res.get("headInfo")
        pic_persons = []
        for res in res_indexs:
            x = res.get('x')
            y = res.get('y')
            xmax = res.get('width') + x
            ymax = res.get('height') + y
            color = res.get('color')

            if color == "Null":
                pic_persons.append({color: (int(x), int(y), int(xmax), int(ymax))})
            else:
                pic_persons.append({"helmet": (int(x), int(y), int(xmax), int(ymax))})


        pic_realize_nums = len(pic_persons)
        print(xml_persons)
        print(pic_persons)
        # print(all_colors_right)
        # print(all_heads_right)
        # exit()

        for pic_person in pic_persons:
            # 获取每一个的类型:color head之类
            pic_which_kind = list(pic_person.keys())[0]


            # 获取坐标pic
            pic_coordinate = pic_person.get(pic_which_kind)
            # print(pic_coordinate)

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


                    # if pic_which_kind != xml_which_kind:
                    #     error_pic +=1
                    #     print(jpg)
                    #     continue
                    # print(xml_which_kind,pic_which_kind)
                    if pic_which_kind == 'Null' and xml_which_kind=="head":
                        true_head_pic += 1
                        pic_realize_nums -= 1
                        break
                    elif pic_which_kind == "helmet" and xml_which_kind =="helmet":
                        print(pic_which_kind)
                        print(xml_which_kind)
                        true_hat_pic += 1
                        pic_realize_nums -= 1
                        break

        if pic_realize_nums > 0:
            print(jpg)
        error_pic += pic_realize_nums
    except:

        continue
print("总的安全帽数量为={},未佩戴安全帽数量为={}".format(all_colors_right1,all_heads_right1))
print("包含戴安全帽以及安全帽颜色识别正确的个数={}, 识别未带安全帽正确的个数={}, 识别错误个数={}".format
      (true_hat_pic, true_head_pic, error_pic))