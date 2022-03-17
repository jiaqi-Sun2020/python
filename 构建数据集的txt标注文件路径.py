from tqdm import tqdm
import os
import argparse


# --output_train_pat
# D:\Study-Place\AI\YOLO\第七模块：物体检测-YOLO-实战系列\训练自己的数据集\PyTorch-YOLOv3data\custom\train.txt
# --output_valid_path
# D:\Study-Place\AI\YOLO\第七模块：物体检测-YOLO-实战系列\训练自己的数据集\PyTorch-YOLOv3data\custom\valid.txt
# --input_label_path
# D:\Study-Place\AI\YOLO\第七模块：物体检测-YOLO-实战系列\训练自己的数据集\PyTorch-YOLOv3\data\custom\images
# --vt_proportion
# 0.25



parser = argparse.ArgumentParser()
parser.add_argument("--output_train_path", type=str,default=None,  help="训练集地址") #这个str会吧读取的数据自动变成str的形式!!!!
parser.add_argument("--output_valid_path", type=str,default=None,help="验证集地址") #
parser.add_argument("--input_label_path", type=str, default=None,help="txt的标注地址") #
parser.add_argument("--vt_proportion", type=float, default=0.25 ,help="训练集与验证集比例") #
opt = parser.parse_args()
print(opt)

input_label_path = opt.input_label_path    #获取标注文件地址
input_label = os.listdir(input_label_path) #获取标注文件数据
filenumber = len(input_label)               #获取标注文件量
tv_number  =int(filenumber*opt.vt_proportion)
print(input_label)

#建立txt文件
train= input_label               #获取训练集数据
valid = input_label[:tv_number]  #获取验证集数据


#写入训练集
with open(opt.output_train_path,'w') as f:
    for data in tqdm(train):
         f.write(input_label_path+'\\'+data+'\n')
#写入验证集
with open(opt.output_valid_path, 'w') as f:
    for data in tqdm(valid):
        f.write(input_label_path + '\\' + data + '\n')



