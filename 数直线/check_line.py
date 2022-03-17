import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def hough_lines(image):
    # 输入的图像需要是边缘检测后的结果
    # minLineLengh(线的最短长度，比这个短的都被忽略)和MaxLineCap（两条直线之间的最大间隔，小于此值，认为是一条直线）
    # rho距离精度,theta角度精度,threshod超过设定阈值才被检测出线段
    return cv2.HoughLinesP(image, rho=0.1, theta=np.pi / 10, threshold=15, minLineLength=9, maxLineGap=4)

def stored_lines( lines,img):
    # 过滤霍夫变换检测到直线
    image = np.copy(img)
    cleaned = []
    all_y = []
    for line in lines:
        for x1,y1,x2,y2 in line:
            if abs(y2-y1) <=4  :
               cleaned.append((x1,y1,x2,y2))
               all_y.append(y1)
               cv2.line(image, (x1, y1), (x2, y2), [255,0,0], 1)
    print(" No lines detected: ", len(cleaned))
    return cleaned,all_y ,image


img = cv2.imread('check_line.jpg')
cv_show('1',img)
width = img.shape[0]

img = cv2.transpose(img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv_show('2',gray)

#开运算 先腐蚀再膨胀
kernel=np.ones((3,3),np.uint8)  #建立核 意思就是在图片数组中分割成5x5的数组
opening=cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)
opening=cv2.morphologyEx(opening,cv2.MORPH_OPEN,kernel)
cv_show('3',opening)

# ret1, thresh1 = cv2.threshold(opening, 94, 255, cv2.THRESH_BINARY)
# cv_show('4',thresh1)
#canny边缘检测
v1=cv2.Canny(opening,10,80) #图片,minval=80,maxval=150
cv_show('4',v1)

#霍夫直线检测
Hline=cv2.HoughLinesP(v1, rho=0.1, theta=np.pi / 10, threshold=10, minLineLength=25, maxLineGap=4)
cleaned,all_y,img2 = stored_lines(Hline,img)
cv_show('5',img2)
all_y = sorted(all_y) #从小到大排序
print(all_y)


#剔除小于y相距4的直线
cleaned_y = []
for i,y in enumerate(all_y):
    if i == 0:
        pre_y = y
        cleaned_y.append(y)
    else:
        if abs(pre_y- y) >4:
            cleaned_y.append(y)
            pre_y = y

print(cleaned_y)
image = np.copy(img)
for y in cleaned_y:
    cv2.line(image, (0, y), (width, y), [0,255,0], 1)
print(len(cleaned_y))
cv_show('6',image)

cv2.imwrite('checked_line.jpg',image)







