import cv2 as cv
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#if the pixel value is greater than 150, it will be converted to 255, otherwise 0
cv.imshow('Simple Thresholded Image', thresh)

# Inverse Simple Thresholding
threshold, thresh_inv= cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#if the pixel value is greater than 150, it will be converted to 0, otherwise 255
cv.imshow('Inverse Simple Thresholded Image', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)