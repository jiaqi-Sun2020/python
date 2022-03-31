import cv2
import os
path = "./picture_laplace"
save_dir ="./laplace_change_size"
filelist = os.listdir(path)  #读取到对应文件夹下的的文件了
print(filelist)

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# for lap_path in filelist:
#     read_path = path+"/"+lap_path
#     img = cv2.imread(read_path)
#
#     img = cv2.resize(img,((1640, 470)))
#
#     #cv_show("test",img)
#
#     save_path = (save_dir +"/"+lap_path)
#     print(save_path)
#     cv2.imwrite(save_path,img)
#     print(lap_path)

img = cv2.imread("oringe_lap.jpg")
img = cv2.resize(img,((1640, 618)))
cv2.imwrite("change_lap.jpg",img)
    
    
    
    
    
    

    
    

    

    
    

    

    

    

    

    
    

    
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    

    
    
    
    


    
    
    
    
    
    

    

    
    
    

    

    


    
    

    
    
    

    
    


    
    







# img_in = cv2.imread("./picture/00020.jpg")
# img_out = cv2.imread("./picture_laplace/00020.jpg")
# img_in = img_in[120: ,: ,: ]   #差不多470的样子
# print(img_in.shape)
# cv_show("in",img_in)
