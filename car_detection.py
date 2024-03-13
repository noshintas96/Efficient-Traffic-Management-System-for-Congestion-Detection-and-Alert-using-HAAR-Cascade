#import libraries of python opencv
import cv2
import numpy as np

#create VideoCapture object and read from video file
cap = cv2.VideoCapture(0)
#use trained cars XML classifiers
car_cascade = cv2.CascadeClassifier('./xmls/cascade_3_good.xml')

def whiteness(gray,x,y,w,h):
    temp = gray[y:y+h,x:x+w]
    whites = temp[np.where(temp>100)]
    if len(whites)>1000:
        return True



#read until video is completed
while True:
    #capture frame by frame
    ret, frame = cap.read()
    #convert video into gray scale of each frames
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #detect cars in the video
    cars = car_cascade.detectMultiScale(gray, 1.10, 1, minSize=(40,40), maxSize=(70,60))

    #to draw arectangle in each cars 
    for (x,y,w,h) in cars:
        if not (whiteness(gray,x,y,w,h) or (x>443 and y<256)) :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #display the resulting frame
    cv2.imshow('video', frame)
    #press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#release the videocapture object
cap.release()
#close all the frames
cv2.destroyAllWindows()
