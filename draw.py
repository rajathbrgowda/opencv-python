import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')     # blank image of size 500x500 with 3 channels
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[:] = 0,255,0                                  # green color
blank[200:300, 300:400] = 0,0,255                 # red color inside blank image
cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)                                  # thickness=-1 oe cv.FILLED fills the rectangle
# or
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)      # gives same result as above by scale factor
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=-1)            # gives a circle in the middle of the image
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)        # gives a line from top left to middle of the image
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello !!! My name is Raj', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (150,255,0), 2)     # gives a text in the middle of the image
cv.imshow('Text', blank)

cv.waitKey(0)
cv.destroyAllWindows()