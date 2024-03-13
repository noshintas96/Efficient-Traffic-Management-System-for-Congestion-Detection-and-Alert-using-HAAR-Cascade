import cv2

cap = cv2.VideoCapture(1)
c = 0
while True:
    ret, frame = cap.read()
    img = frame
    if ret:
        cv2.line(frame, (176, 414), (458, 417), (255, 0, 0), 3)
        cv2.line(frame, (204, 314), (239, 236), (255, 0, 0), 3)
        cv2.line(frame, (458, 311), (433, 233), (255, 0, 0), 3)
        cv2.line(frame, (60, 237), (591, 239), (255, 0, 0), 3)
        cv2.circle(img, (324, 235), 3, (0, 0, 255), -1)
        cv2.circle(img, (183, 360), 3, (0, 0, 255), -1)

        # cv2.line(frame, (443, 214), (606, 164), (255, 0, 0), 3)
        # cv2.line(frame, (443, 214), (417, 73), (255, 0, 0), 3)
        # cv2.line(frame, (210, 221), (227, 75)o, (255, 0, 0), 3)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()


# import matplotlib.pyplot as plt
#
# frame = cv2.imread('./backs/back_40.jpg')
#
# cv2.line(frame, (15,166),(210,221), (255,0,0), 3)
# cv2.line(frame, (1,317),(210,388), (255,0,0), 3)
# cv2.line(frame, (210,388),(471,386), (255,0,0), 3)
# cv2.line(frame, (471,386),(637,338), (255,0,0), 3)
#
# cv2.line(frame, (443,214),(606,164), (255,0,0), 3)
# cv2.line(frame, (443,214),(417,73), (255,0,0), 3)
# cv2.line(frame, (210,221),(227,75), (255,0,0), 3)
#
#

# plt.imshow(frame)
# plt.show()