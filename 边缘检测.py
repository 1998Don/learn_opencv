import cv2
import numpy as np

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
Canny边缘检测
1、使用高斯滤波器，以平滑图像、滤除噪声
2、计算图像中每个像素点的梯度强度和方向
3、应用非极大值抑制，以消除边缘检测带来的杂散响应-线性插值法
4、应用双阀值检测来确定真实的和潜在的边缘
5、通过抑制孤立的弱边缘最终完成边缘检测
'''
img = cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)
v1 = cv2.Canny(img,80,150)
v2 = cv2.Canny(img,50,100)
res = np.hstack((v1,v2))
cv_show(res,'res')

