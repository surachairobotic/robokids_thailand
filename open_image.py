import numpy as np
import cv2

fname = '/home/probook/Downloads/IMG_20220604_123413.jpg'

# Load an color image in grayscale
img = cv2.imread(fname)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

height, width, layers = img.shape
new_h = int(height / 6)
new_w = int(width / 6)
resize = cv2.resize(img, (new_w, new_h))

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
    

# show image
cv2.imshow('rgb',resize)
cv2.imshow('image',imagemask)
cv2.waitKey(0)
cv2.destroyAllWindows()
