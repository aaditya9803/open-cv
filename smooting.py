import cv2 as  cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

#Averaging
#takes square of 9 pixels (3*3) 
#and takes average of intensity of surrounding pixels with respect to center pixel
average = cv.blur(img, (3,3))
cv.imshow('Average', average)


#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss)

#Median Blur
Median = cv.medianBlur(img, 3)
cv.imshow('Median', Median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)