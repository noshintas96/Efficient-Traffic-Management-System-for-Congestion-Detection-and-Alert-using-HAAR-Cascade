import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./test_images/back_4.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.imshow(img)

plt.show()