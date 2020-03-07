import cv2

img = cv2.imread('D:\\opencv-master\\opencv-master\\samples\\data\\aero1.jpg', 1)
print(img)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('aero1_copy.jpg',img)
    cv2.destroyAllWindows()