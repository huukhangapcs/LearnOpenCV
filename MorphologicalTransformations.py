import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt

img = cv.imread('D:\\opencv-master\\opencv-master\\samples\\data\\smarties.png', cv.IMREAD_GRAYSCALE)
_,mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)
dilation = cv.dilate(mask,kernel, iterations = 2)
erosion = cv.erode(mask, kernel, iterations = 1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
titles = ['image', 'mask','kernel','erosion', 'opening','closing']
images = [img, mask, dilation,erosion, opening, closing]

for i in range(len(images)):
    plt.subplot(math.ceil(len(images)/2),2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()