import cv2 as cv
import numpy as np 
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2),100, 255, -1)
cv.imshow('circle', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)
circleandrectangle = cv.bitwise_and(circle, rectangle)
cv.imshow('Circle and Rectangle', circleandrectangle)

masked = cv.bitwise_and(img, img, mask=circleandrectangle)
cv.imshow('Masked Image', masked)


cv.waitKey(0)