import cv2
import os
path = "./yolo_distance"
filelist = os.listdir(path)  #读取到对应文件夹下的的文件了
print(filelist)
#white_output = "./test.avi"
fps = 11 #视频每秒1帧
size = (1640, 590)
size_lap = (976,289)
change_size = (1640,470)
video = cv2.VideoWriter("Video_yolo_distance.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)

for item in filelist:
    #print(item)
    item  = path+'/'+item
    if item.endswith('.jpg'):
        #print(item)
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
print('Video has been made.')