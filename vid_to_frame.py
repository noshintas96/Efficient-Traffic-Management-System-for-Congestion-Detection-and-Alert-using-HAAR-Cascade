import cv2
import os

vid = cv2.VideoCapture('output_3.avi')
# os.mkdir('frames')
c = 477
while True:
    ret, frame = vid.read()
    if ret:
        cv2.imwrite('./frames/frame_%d.jpg'%c, frame)
        c+=1
        print('done', c)
    if not ret:
        print('finished')

        break