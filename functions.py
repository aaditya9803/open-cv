import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('A cat', img)

# convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
cv.imshow('A Gray Cat', gray)

#Blur - level 1
blur = cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('A Blurred Cat', blur)

#Blur - level 2
blur2 = cv.GaussianBlur(img, (21,21), cv.BORDER_DEFAULT)
cv.imshow('A Blurred Cat 2', blur2)

# Edge Cascade
canny = cv.Canny(img,  125, 175)
cv.imshow('A Canny Cat', canny)

# Edge Cascade and blur
canny2 = cv.Canny(blur,  125, 175)
cv.imshow('A Canny Cat 2', canny2)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('A Dilated Cat', dilated)

# Eroding the dilated image
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Edroding the Dilated Cat', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('A Resized Cat', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('A Cropped Cat', cropped)
cv.waitKey(0)