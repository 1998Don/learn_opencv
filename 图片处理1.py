#图片处理
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('dog.jpg')

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #超过阀值部分取最大值，否则取0
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)#反转
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)#大于阀值部分设为阀值，否则不变
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#大于阀值部分不改变，否则设为0
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)#反转

titles = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1,thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
    
