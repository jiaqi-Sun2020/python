
import json
import os

#在此处进行修改标签名
name2id = {'mask':0,'no_mask':1,}  #有多少类别写多少

               
def convert(img_size, box):
    dw = 1./(img_size[0])
    dh = 1./(img_size[1])
    x = (box[0] + box[2])/2.0 - 1
    y = (box[1] + box[3])/2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
 
def decode_json(json_floder_path,json_name):
    #制定好转换好的标签地址
    txt_name = 'D:\\Study-Place\\AI\\YOLO\\第七模块：物体检测-YOLO-实战系列\\训练自己的数据集\\PyTorch-YOLOv3 - 副本\\data\\custom\\labels\\' + json_name[0:-5] + '.txt'
    txt_file = open(txt_name, 'w')
 
    json_path = os.path.join(json_floder_path, json_name)
    #data = json.load(open(json_path, 'r', encoding='gb2312'))
    data = json.load(open(json_path, 'r', encoding='UTF-8'))
 
    img_w = data['imageWidth']
    img_h = data['imageHeight']
 
    for i in data['shapes']:
        
        label_name = i['label']
        if (i['shape_type'] == 'rectangle'):
 
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])
 
            bb = (x1,y1,x2,y2)
            bbox = convert((img_w,img_h),bb)
            txt_file.write(str(name2id[label_name]) + " " + " ".join([str(a) for a in bbox]) + '\n')
    
if __name__ == "__main__":
    #json的路径
    json_floder_path = 'D:\\Study-Place\\AI\\YOLO\\第七模块：物体检测-YOLO-实战系列\\训练自己的数据集\\标注'
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        decode_json(json_floder_path,json_name)
