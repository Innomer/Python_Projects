import cv2 as cv
#RESIZING AND SCALING
img=cv.imread('Photos/cat_large.jpg')
#cv.imshow('Cat',img)

#Rescale for only Live Videos
def changeRes(width,height):
    capture.set(3,width) #3 for width and 4 for height property numbers
    capture.set(4,height)

#Rescale Func (for images videos and live vids)
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale) #shape[1] is width and 0 is for height
    height=int(frame.shape[0]*scale)
    
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#Reading videos
capture=cv.VideoCapture('Videos/dog.mp4') #uses integers for physical cams.. or '' for paths
#we use a while to read video frame by frame
while True:
    isTrue,frame=capture.read() #Returns the frame and whther frame was successfully read or not

    frame_resized=rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized )

    if cv.waitKey(20) & 0xFF==ord('d'): #To Break and Stop Infinite Repeation of Video
        #0xFF says if d is pressed or not
        break
img=cv.imread('Photos/cat_large.jpg')
resized_image=rescaleFrame(img)
cv.imshow('Cat Resized',resized_image)

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)