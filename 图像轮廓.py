import cv2

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
图像轮廓
cv2.findContours(img,mode,method)
mode:轮廓检索模式
--RETR_EXTERNAL：只检测最外面的轮廓
--RETR_LIST：检索所有的轮廓，并将其保存到一条链表当中
--RETR_CCOMP：检索所有的轮廓，并将他们组织为两层：顶层是各部分的外部边界，第二层是空洞的边界
--RETR_TREE：检索所有的轮廓，并重构嵌套轮廓的整个层次
method:轮廓逼近方法
--CHAIN_APPROX_NONE：以Freeman链码的方式输出轮廓，所有其他方法输出多边形-顶点的序列
--CHAIN_APPROX_SIMPLE：压缩水平的、垂直的和斜的部分，也就是，函数只保留他们的终点部分
'''
'''
#为了更高的准确率，使用二值图像
img = cv2.imread('cicle.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#得到灰度图
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#得到二值图
#cv_show(thresh,'thresh')
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #contours-轮廓信息
#绘制轮廓
draw_img = img.copy()
res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
cv_show(res,'res')

#轮廓特征
cnt = contours[0]
cv2.contourArea(cnt) #面积
cv2.arcLength(cnt,True) #周长，True表示闭合
'''
'''
#轮廓近似
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#得到灰度图
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#得到二值图
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #contours-轮廓信息
cnt = contours[1]

epsilon = 0.01*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
draw_img = img.copy()
res = cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)
cv_show(res,'res')
'''
'''
#边界矩形
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#得到灰度图
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#得到二值图
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #contours-轮廓信息
cnt = contours[1]
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv_show(img,'img')
'''
#外接圆
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#得到灰度图
ret, thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#得到二值图
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #contours-轮廓信息
cnt = contours[1]
(x,y),radius= cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,0,255),2)
cv_show(img,'img')
