import cv2 as cv
# ------------------------------------------------------------------------------------------------------------------------
# reading image and saving it in a variable
img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)       # Diplay window with image and name of window
cv.waitKey(0)               # 0 means infinite time to wait for a key to be pressed

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
# reading videos and saving it in a variable
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()              # isTrue is a boolean value if video present, frame is the image
    
    cv.imshow('Dog-Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):       # if letter d is pressed, break from loop
        break

capture.release()                               # release the capture variable
cv.destroyAllWindows()                          # destroy all windows