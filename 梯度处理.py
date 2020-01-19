#梯度处理
import cv2
import numpy as np

img = cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)

def cv_show(img,name):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Sobel算子-右减左，下减上
#dst = cv2.Sobel(src,ddepth,dx,dy,ksize)
#ddepth:图片的深度
#dx和dy分别表示水平和竖直方向
#ksize是Sobel算子的大小
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobely = cv2.convertScaleAbs(sobely)
#分别计算x和y，再求和
sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)


#Scharr算子
scharrlx = cv2.Scharr(img,cv2.CV_64F,1,0)
scharrlx = cv2.convertScaleAbs(scharrlx)
scharry = cv2.Scharr(img,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)
#分别计算x和y，再求和
scharrxy = cv2.addWeighted(scharrlx,0.5,scharry,0.5,0)

#laplacian算子
laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((sobelxy,scharrxy,laplacian))
cv_show(res,'res')
