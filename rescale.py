import cv2 as cv

# rescaling function for video and image
def rescaleFrame(frame,scale=0.75):
    
    width = int(frame.shape[1] * scale)         # shape[1] is width
    height = int(frame.shape[0] * scale)        # shape[0] is height
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# rescaling function for live video
def changeRes(width,height):
    # only works for live video
    capture.set(3,width)                        # 3 is the width
    capture.set(4,height)                       # 4 is the height

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------

# reading image for rescaling
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)                           # original image

resized_image = rescaleFrame(img)               # resizing image
cv.imshow('Cat-Resized', rescaleFrame(img))     # resized image

# ------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------
   
# capturing video for rescaling
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()              # isTrue is a boolean value if video present, frame is the image
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Dog-Video', frame)
    cv.imshow('Dog-Video-Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):       # if letter d is pressed, break from loop
        break
    
capture.release()                               # release the capture variable  
cv.destroyAllWindows()                          # destroy all windows
       
