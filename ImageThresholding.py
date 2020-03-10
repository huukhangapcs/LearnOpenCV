import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:\\opencv-master\\opencv-master\\samples\\data\\sudoku.png', 0)
_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11, 2)
#cv2.imshow("Image",img)
#cv2.imshow("threshold",thl)
#cv2.imshow("threshold", th3)
titles = ['image', 'simple', 'mean c', 'gauss c']
images = [img,th1,th2,th3]
for i in range(4):
    plt.subplot(2,2, i+1 ), plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.show()    
#cv2.waitKey(0)
#cv2.destroyAllWindows()