import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()


#make gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Hue Saturation Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

#HSV to BGR to lab
hsvbgR = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
bgrlab = cv.cvtColor(hsvbgR, cv.COLOR_BGR2LAB)
cv.imshow('HSV to BGR to lab', bgrlab)


cv.waitKey(0)