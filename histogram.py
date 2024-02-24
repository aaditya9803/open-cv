import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('A circle', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

mask2 = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask2', mask2)


#Histogram - Grayscale
gray_histogram = cv.calcHist([gray], [0], mask, [256], [0, 256])
# cv.imshow('Gray Histogram', gray_histogram)
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
plt.plot(gray_histogram)
plt.xlim([0, 256])

#Color Histogram
color = ('b', 'g', 'r')
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
for i, col in enumerate(color):
    histogram2 = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(histogram2, color=col)
    plt.xlim([0, 256])


plt.show()



cv.waitKey(0)