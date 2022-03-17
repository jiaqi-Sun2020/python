from tqdm import tqdm
import os
import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("--filenames_path", type=str,  help="文件夹地址") #这个str会吧读取的数据自动变成str的形式!!!!
parser.add_argument("--file_extension", default=None,help="文件格式") #
parser.add_argument("--start", type=int, default=0,help="开始数字") #
parser.add_argument("--end", type=int, default=None ,help="结束数字") #
opt = parser.parse_args()

# --filenames_path
# D:\个人资料
# --file_extension
# ".png",".jpg",".JPG"
# --start
# 100
# --end
# 10


classes = []
if opt.file_extension !=None:    #是否存在文件后缀类型
    classes.append(opt.file_extension)
    classes = str(classes[0])
    classes = re.sub('[()" ]', '', classes)  #把' ' 替换成''  作用为消除空格
    classes = classes.split(",") #split分离不同的后缀
    file_extension = tuple(classes)   #('.png', '.jpg')  这个是根据split函数
    print(file_extension)
    print('exist')
else:                           #不存在就是默认了
    file_extension = ('.jpg','.png','JPG')
    print("no exist")


if opt.filenames_path !=None:
    print(opt.filenames_path)
    filenames_path = opt.filenames_path
    filenames=os.listdir(filenames_path)
    start=opt.start  #获取开始序号
    end = opt.end if opt.end!=None else len(filenames)   #如果opt.end存在的话end就是opt.end,如果不存在的话就是整个文件夹的文件数
    for i in tqdm(filenames):
        if i.endswith(file_extension) and start <=opt.start+end:
            #print('1')
            b = i.split('.')      #根据"."分割字符
            b = b[-1]             #获取最后带有文件后缀的一段
            newname = str(start)+"."+b #创立新名字
            os.rename(os.path.join(filenames_path,i),os.path.join(filenames_path,newname))   #替换名字要注意不能有重复的名字
            start+=1                  #记录个数