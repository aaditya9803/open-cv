import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('A Cat', img)

#Converrting to gray and blur
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('A Cat Gray and Blur', gray)
#Canny
canny = cv.Canny(gray,125,175)
cv.imshow('A Canny cat', canny)


#Contours

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
#RETR_LIST - retrieves all of the contours in the canny image
#CHAIN_APPROX_NONE - retrieves all of the contours points
print(f'{len(contours)} No. contours found')

cv.waitKey(0)