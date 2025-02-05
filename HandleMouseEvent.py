import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x,', ',y)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #strXY = str(x) + ", " + str(y)
        #cv2.putText(img, strXY, (x,y), font, 1, (0,255,255), 1, cv2.LINE_AA)
        #cv2.circle(img,(x,y), 3, (0,0,255),-1)
        #points.append((x,y))
        #if len(points) > 1:
            #cv2.line(img, points[-1], points[-2], (255,255,0),1,cv2.LINE_AA)
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        cv2.circle(img,(x,y), 3, (0,0,255),-1)
        mycolor = np.zeros((512,512,3), np.uint8)    
        mycolor[:] = [blue, green, red]
        cv2.imshow('color',mycolor)

    #elif event == cv2.EVENT_RBUTTONDOWN:
        #blue = img[y,x, 0]
        #green = img[y,x,1]
        #red = img[y,x,2]
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #bgr = str(blue) + ", " + str(green) + ", " + str(red)
        #cv2.putText(img, bgr, (x,y), font, 1, (0,255,255), 1, cv2.LINE_AA)
        #cv2.imshow('img',img)    

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread('D:\\opencv-master\\opencv-master\\samples\\data\\lena.jpg', 1)
cv2.imshow('img',img)
points = []
cv2.setMouseCallback('img',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

