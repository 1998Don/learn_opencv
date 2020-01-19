#opencd_video
import cv2

vc = cv2.VideoCapture('test.mp4')
#检查是否正确打开
if vc.isOpened():
    oepn,frame = vc.read()
else:
    oepn = False

while oepn:
    ret,frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',gray)
        if cv2.waitKey(40) & 0xFF == 27:
            break
vc.release()
cv2.destroyAllWindows()
