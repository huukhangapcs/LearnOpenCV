import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200,0),(300,100), (255,255,255),-1)
img2 = cv2.imread('D:\\opencv-master\\opencv-master\\samples\\data\\image_1.png', 1)

#bitand = cv2.bitwise_and(img2,img1)
bitor = cv2.bitwise_or(img2, img1)
cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)
cv2.imshow('image',bitor)
cv2.waitKey(0)
cv2.destroyAllWindows()