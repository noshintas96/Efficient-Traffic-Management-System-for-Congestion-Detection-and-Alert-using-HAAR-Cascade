#import libraries of python opencv
import cv2
import numpy as np

car_cascade = cv2.CascadeClassifier('cars.xml')


img = cv2.imread('./haar/test images/test1.jpg')
img = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray,1.3,2)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()