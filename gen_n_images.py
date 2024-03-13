import os
from PIL import Image
import cv2

img = cv2.imread('./images/haar_11.jpg')
h,w,c = img.shape
size = 400

c=89
for i in range(0,h,size):
    for j in range(0,w,size):
        temp = img[i:i+size,j:j+size]
        cv2.imwrite('./haar/n/%d.jpg'%c, temp)
        c+=1
        print('done', c)

##angle

angles = range(-10,10)
c=21
for a in angles:
    img = Image.open('./haar/n/n_1.jpg')
    img = img.rotate(a)
    img.save('./haar/n/%d.jpg'%c)
    c+=1
    print('done', c)


##shape correction

files = os.listdir('./haar/n/')

for f in files:
    img = cv2.imread('./haar/n/'+f)
    h,w,c = img.shape
    if h != size or w != size:
        os.remove('./haar/n/'+f)
        print('removed', f)