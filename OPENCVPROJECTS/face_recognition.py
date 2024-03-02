import cv2 as cv
import numpy as np
import os

# CV Built In Recognizer is not too good. Gives Error at some Times


haar_cascade=cv.CascadeClassifier('haar_face.xml')

features=np.load('Features.npy',allow_pickle=True)
labels=np.load('Labels.npy',allow_pickle=True)

p=[]
DIR=r'E:\OLD PC FILES\Mann Files\Game Dev\GIT REPO\OPENCVFILES\OPENCVPROJECTS\Faces\train'
for i in os.listdir(DIR):
    p.append(i)

# Reading .yml file
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img=cv.imread(r'E:\OLD PC FILES\Mann Files\Game Dev\GIT REPO\OPENCVFILES\OPENCVPROJECTS\Faces\val\elton_john\1.jpg')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

# Detect  the face in the image
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces_rect:
    roi=gray[y:y+h,x:x+w]
    
    label,confidence=face_recognizer.predict(roi)

    print(f'Label = {p[label]} with a confidence of {confidence}')

    cv.putText(img,str(p[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv.imshow('Detected Face',img)

cv.waitKey(0)
    