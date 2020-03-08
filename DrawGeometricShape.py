import numpy as np
import cv2

#img = cv2.imread('D:\\opencv-master\\opencv-master\\samples\\data\\lena.jpg', 1)
#img = cv2.line(img, (0,0),(255,255),(255,0,0),5)
#img = cv2.arrowedLine(img, (10,10),(10,255),(255,0,0),5)
img = np.zeros([512,512,3],np.uint8)
img = cv2.rectangle(img,(0,0),(255,255),(0,0,255),5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,2,(255,255,255),4, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()