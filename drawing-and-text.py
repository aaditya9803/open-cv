import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow("a blank pic", blank)

# pic of certain color
# blank[:] = 0,255,0
# cv.imshow('', blank)

# A rectangle
cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=1)
cv.imshow('A rectangle', blank)


# A circle
cv.circle(blank, (250,250), 50, (0,0,255), thickness=2)
cv.imshow('A circle', blank)

#A line
cv.line(blank, (50,50), (250,250), (0,0,255), thickness=3)
cv.imshow('A line', blank)

# Text
cv.putText(blank, "Neupane", (255,255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), 1)
cv.imshow('Text', blank)
cv.waitKey(0)