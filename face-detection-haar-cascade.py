import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('A lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar-cascade.xml')

faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w , y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', img)

print(f'Number of faces found = {len(faces)}')


cv.waitKey(0)
