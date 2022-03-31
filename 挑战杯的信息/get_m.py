import cv2
import os
import numpy as np

# xyxy = [212,100,700,400]
# xyxy = np.array([0,0,700,400])
xyxy = [1115,137,1161,159]
K = 8/(1.01**104)  #指数为1.2防止过大造成溢出  (默认为255-151的灰度值为800毫米)

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def get_min_distance(xyxy,img):
    roi = img[ xyxy[1]:xyxy[3],xyxy[0]:xyxy[2]]
    max_ = np.max(roi)
    print(max_)
    if(max_>200):
        y=99999
    else:
        y = K * (1.01 ** (255 - max_))

    print(20*"=======")
    print(y)
    return y




img = cv2.imread("./laplace_change_size/00890.jpg")

img_gary = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv_show("test",img_gary)


distance = get_min_distance(xyxy,img_gary)