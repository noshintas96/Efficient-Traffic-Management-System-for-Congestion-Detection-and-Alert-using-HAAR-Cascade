import cv2
import numpy as np

car_cascade = cv2.CascadeClassifier('./xmls/cascade.xml')

img = cv2.imread('./test_images/back_37.jpg')

h,w,c = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray,1.10,1, minSize = (70,60), maxSize=(80,70))



for (x, y, w, h) in cars:
    #
    if not (x<220 and y<190) or (x>400 and y<90):
        # cv2.circle(img,(x,y), 3, (255,0,0), -1)
        # cv2.putText(img, str(x)+','+str(y), (x,y),cv2.FONT_HERSHEY_SIMPLEX,.5,(0,0,0), 1)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(len(cars))

# import matplotlib.pyplot as plt
# plt.imshow(img)
# plt.show()