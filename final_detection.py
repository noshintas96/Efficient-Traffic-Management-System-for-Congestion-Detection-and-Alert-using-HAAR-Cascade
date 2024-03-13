import cv2
import numpy as np

# img = cv2.imread('./backs/final_back_9.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

car_cascade = cv2.CascadeClassifier('./xmls/cascade_very_good.xml')
car_cascade_2 = cv2.CascadeClassifier('./haar/classifier/cascade.xml')



cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if ret:
        left_lane = gray[279:380,:204]
        mid_lane = gray[220:314,324:465]
        right_lane = gray[300:400,465:]

        right_car = car_cascade_2.detectMultiScale(right_lane,1.10,3, minSize = (40,30), maxSize=(80,70))
        # for (x, y, w, h) in right_car:
        #     cv2.rectangle(right_lane, (x, y), (x + w, y + h), (0, 0, 0), 3)

        left_car = car_cascade_2.detectMultiScale(left_lane,1.10,3, minSize = (40,30), maxSize=(80,70))
        # for (x, y, w, h) in left_car:
        #     cv2.rectangle(left_lane, (x, y), (x + w, y + h), (0, 0, 0), 3)

        mid_car = car_cascade_2.detectMultiScale(mid_lane,1.10,1, minSize = (40,30), maxSize=(80,70))
        # for (x, y, w, h) in mid_car:
        #     cv2.rectangle(mid_lane, (x, y), (x + w, y + h), (0, 0, 0), 3)

        cars = [len(left_car), len(mid_car), len(right_car)]

        # max = cars.index(max(cars))
        # cv2.imshow('lef', left_lane)
        # cv2.imshow('right', right_lane)
        # cv2.imshow('mid', mid_lane)
        #
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

        print(cars.index(max(cars)))

# for (x,y,w,h) in mid_car:
#     cv2.rectangle(mid_lane, (x, y), (x + w, y + h), (0, 0, 0), 3)

cv2.imshow('image', mid_lane)
        # cv2.imshow(str(p), i[y:y + h, x:x + w])
        # p+=1
# print(len(right_car), len(mid_car),len(left_car))

# cars = car_cascade.detectMultiScale(gray,1.10,1, minSize = (40,30), maxSize=(80,70))
#
# split = [left_lane,mid_lane,right_lane]
# # i = 0
# p = 0
# max = 0
# for i in split:
#     cars = car_cascade.detectMultiScale(i,1.10,1,minSize=(50,40), maxSize=(70,50))
#     for (x,y,w,h) in cars:
#
#         if  not whiteness(i,x,y,w,h):
#             cv2.rectangle(i, (x, y), (x + w, y + h), (0, 0, 0), 3)
#             num_car = len(cars)
#
#             # cv2.imshow(str(p), i[y:y + h, x:x + w])
#             # p+=1
#
#         #
#     cv2.imshow(str(p), i)
#     p+=1
#
# car_left = car_cascade.detectMultiScale(left_lane, 1.10, 1, minSize=(50,40), maxSize=(70,50))
# num_left_car = 0
# for (x,y,w,h) in car_left:
#     if not whiteness(left_lane, x,y,w,h):
#         cv2.rectangle(left_lane,(x,y), (x+w,y+h),(0,0,0), 3)
#         num_left_car+=1
#         print(num_left_car)
#
#
#
# car_right = car_cascade.detectMultiScale(right_lane, 1.10, 1, minSize=(50,40), maxSize=(70,50))
# num_right_car = 0
# for (x,y,w,h) in car_right:
#     if not whiteness(right_lane, x,y,w,h):
#         cv2.rectangle(right_lane,(x,y), (x+w,y+h),(0,0,0), 3)
#         num_right_car+=1
#
# car_mid = car_cascade.detectMultiScale(mid_lane, 1.10, 1, minSize=(50, 40), maxSize=(70, 50))
# num_mid_car = 0
# for (x, y, w, h) in car_mid:
#     if not whiteness(mid_lane, x, y, w, h):
#         cv2.rectangle(mid_lane, (x, y), (x + w, y + h), (0, 0, 0), 3)
#         num_mid_car += 1
#
#
# print(num_left_car, 'left car')
# print(num_right_car,'right car')
# print(num_mid_car,'mid lane')
#
