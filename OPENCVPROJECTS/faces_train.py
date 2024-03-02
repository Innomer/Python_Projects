import os
from typing import Dict
import cv2 as cv
import numpy as np

# Training and Using OpenCV built in face recognizer

# Either type names manually or use method below

p=[]
DIR=r'E:\OLD PC FILES\Mann Files\Game Dev\GIT REPO\OPENCVFILES\OPENCVPROJECTS\Faces\train'
for i in os.listdir(DIR):
    p.append(i)

haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=[] # features of face
labels=[] # Name of face
# loop over each image and grab it and add to training list
def create_train():
    for person in p:
        # Entering folder of person
        path=os.path.join(DIR,person)
        label=p.index(person)

        # Looping over each image of person
        for img in os.listdir(path):
            img_path=os.path.join(path,img)

            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

            for(x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w] #faces region of interest(features of face)
                features.append(faces_roi)
                labels.append(label)


create_train()

features=np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()

# Training Recognizer on features and labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')

np.save('Features.npy',features)
np.save('Labels.npy',labels)

print('Training done---------------------')

# Now if i want to use this model in another file, i Will have to retrain it all over again.
# but OpenCV allows us to save this trained model and use it in another file just by using a YML source File.

# NOW WE ARE USING THIS MODEL IN FACE_RECOGNITION