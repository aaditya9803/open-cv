import numpy as np
import cv2 as cv
import os

face_cascade = cv.CascadeClassifier('haar-cascade.xml')

people = []
for i in os.listdir('Faces/train'):
    people.append(i)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread('Faces/val/elton_john/2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
face_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected face', img)

cv.waitKey(0)