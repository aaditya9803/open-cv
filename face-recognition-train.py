import os
import cv2 as cv
import numpy as np

people = []
for i in os.listdir(r'Faces/train'):
    people.append(i)
print(people)

features = []
labels = []

face_cascade = cv.CascadeClassifier('haar-cascade.xml')


def create_train():
    for person in people:
        path = os.path.join(r'Faces/train', person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            #Face detection
            face_rect = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x, y, w, h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()


print(f'No. of the features = {len(features)}')
print(f'No. of the labels = {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
features = np.array(features, dtype='object')
labels = np.array(labels)
face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
print('Training done ---------------')
