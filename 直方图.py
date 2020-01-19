import cv2
import matplotlib.pyplot as plt
#直方图

img = cv2.imread('上海堡垒.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    plt.show()
