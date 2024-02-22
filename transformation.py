import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('A cat', img)

#Translation
def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])   #-x goes left, -y goes up
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transmat, dimensions)
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

#Rotation of the image

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('A Rotated Cat', rotated)

#Flipping the image
flip = cv.flip(img, 1)
cv.imshow('A Flipped Cat', flip)
#Resizing and cropping the flipped image
resized = cv.resize(flip, (500,500), interpolation=cv.INTER_CUBIC)
cropped = flip[200:400, 300:400]
cv.imshow('A Resized Cat', cropped)

cv.waitKey(0)