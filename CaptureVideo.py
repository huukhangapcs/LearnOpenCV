import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc,24, (640,480))
# file name or device index (0 or -1, 1,2)
cap.set(3,1208)
cap.set(4,720)
while cap.isOpened():
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret == True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break    
        
cap.release()
out.release()
cv2.destroyAllWindows()
