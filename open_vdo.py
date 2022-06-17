import numpy as np
import cv2

fname = '/home/probook/Downloads/VID_20220604_123445.mp4'

cap = cv2.VideoCapture(fname)
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    height, width, layers = frame.shape
    new_h = int(height / 2)
    new_w = int(width / 2)
    resize = cv2.resize(frame, (new_w, new_h))
    
    #gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    
    resize = cv2.blur(resize, (5,5))

    #defining the lower bounds and upper bounds
    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([255,50,50])

    #masking the image using inRange() function
    imagemask = cv2.inRange(resize, lower_bound, upper_bound)

    contours, hierarchy = cv2.findContours(imagemask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(resize, contours, -1, (0,255,0), 3)

    for con in contours:
        area = cv2.contourArea(con)
        print('area : ' + str(area))
        if area > 10000:
            cv2.fillPoly(resize, pts =[con], color=(0, 255,255))

    
    cv2.imshow('frame123', resize)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
