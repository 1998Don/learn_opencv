#opencv
import cv2
import matplotlib.pyplot as plt

#图像显示
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#彩色图   
#img = cv2.imread('cat.jpeg')

#图像融合
img_cat = cv2.imread('cat.jpeg')
img_dog = cv2.imread('dog.jpg')
img_cat = cv2.resize(img_cat,(650,407))
#img = img_cat + img_dog
#img = cv2.add(img_cat,img_dog)
img = cv2.addWeighted(img_cat,0.4,img_dog,0.6,0)
cv_show('cat',img)
'''
#边界填充
top_size,bottom_size,left_size,right_size = (50,50,50,50)
replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)#复制法
reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)#反射法
reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)#101反射法
wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)#外包装法
constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=0)#常量法，常数值填充
plt.subplot(231), plt.imshow(img,'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate,'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect,'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101,'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap,'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant,'gray'), plt.title('CONSTANT')
plt.show()
'''

#灰度图
#img = cv2.imread('cat.jpeg',cv2.IMREAD_GRAYSCALE)
#print(img)
#截取部分图像数据
#img = cv2.imread('cat.jpeg')
#cat = img[0:400,0:400]
'''
#颜色通道提取
b,g,r = cv2.split(img)
#颜色通道合成
img = cv2.merge((b,g,r))
'''
'''
#只保留R
cur_img = img.copy()
cur_img[:,:,0]=0
cur_img[:,:,1]=0
cv_show('R',cur_img)
'''
'''
print(type(img))
print(img.size)
print(img.dtype)
print(img.shape)
cv_show('cat',cat)
#保存
cv2.imwrite('mycat.png',img)
'''


