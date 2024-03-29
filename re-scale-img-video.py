import cv2 as cv
cat = cv.imread('Photos/cat.jpg')
cv.imshow('cat',cat)

def rescaleFrame(frame, scale = 0.75): #For the Captured video and Photos
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension =  (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeResolution(width,height): #For the Live video
    capture.set(3,width) #3 reference width and 4 reference the height
    capture.set(4,height)

cv.imshow('Image',rescaleFrame(cat))
capture = cv.VideoCapture("Videos/dog.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('resized', frame_resized)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0)