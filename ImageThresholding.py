import cv2
import numpy as np

img = cv2.imread('D:\\opencv-master\\opencv-master\\samples\\data\\sudoku.png', 0)
_, thl = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11, 2)
cv2.imshow("Image",img)
#cv2.imshow("threshold",thl)
cv2.imshow("threshold", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()