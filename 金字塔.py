import cv2
import numpy as np

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
高斯金字塔：向下采样-缩小
---将Gi与高斯内核卷积
---将所有偶数行和列去除

高斯金字塔：向上采样-放大
---将图像在每个方向扩大为原来的两倍，新增的行和列以0填充
---使用先前同样的内核-乘以4，与放大后的图像卷积，获得近似值
'''

img = cv2.imread('mycat.png',cv2.IMREAD_GRAYSCALE)
up = cv2.pyrUp(img)
down = cv2.pyrDown(img)
cv_show(down,'res')
