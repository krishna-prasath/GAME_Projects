import cv2
import random
import numpy as np
a=[]
ob=cv2.imread("1.jpg",-1)
#cv2.imshow("display",ob)
for i in range(10):
    a.append(cv2.imread(str(str(i+1)+".jpg"),-1))
random.shuffle(a)
for i in range(10):
    a[i]=cv2.resize(a[i],(200,200))
#cv2.imshow("df",a[0])
r1=np.concatenate((a[0],a[1],a[2]),axis=1)
r2=np.concatenate((a[3],a[4],a[5]),axis=1)
r3=np.concatenate((a[6],a[7],a[8]),axis=1)
vis=np.concatenate((r1,r2,r3),axis=0)
cv2.imshow("new",vis)
