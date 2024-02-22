import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('A Cat', img)
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
# #Converrting to gray and blur
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# gray = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('A Cat Gray and Blur', gray)
# #Canny
canny = cv.Canny(gray,125,175)
cv.imshow('A Canny cat', canny)


#Contours
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded Image', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
#RETR_LIST - retrieves all of the contours in the canny image
#CHAIN_APPROX_NONE - retrieves all of the contours points
print(f'{len(contours)} No. contours found')


cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Cat', blank)

cv.waitKey(0)