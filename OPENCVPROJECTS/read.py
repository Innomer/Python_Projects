import cv2 as cv
#Reading Images
#img = cv.imread('Photos/cat_large.jpg')

#cv.imshow('Cat',img)

#Reading videos
capture=cv.VideoCapture(0) #uses integers for physical cams.. or '' for paths
#we use a while to read video frame by frame
while True:
    isTrue,frame=capture.read() #Returns the frame and whther frame was successfully read or not
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #To Break and Stop Infinite Repeation of Video
        #0xFF says if d is pressed or not
        break

capture.release()
cv.destroyAllWindows()



cv.waitKey(0)