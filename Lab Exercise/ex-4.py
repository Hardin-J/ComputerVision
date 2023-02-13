import cv2
import numpy as np

im = cv2.imread("husky.jpg")
img = cv2.resize(im,(400,480))
cv2.imshow('image',img)
cv2.waitKey(0)

#Gaussian Blur
gBlur = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Gaussian Blur",gBlur)
cv2.waitKey(0)

#Median Blur
med = cv2.medianBlur(img,5)
cv2.imshow("Median",med)
cv2.waitKey(0)

#Bilateral Blur
Blat = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Blat",Blat)
cv2.waitKey(0)
cv2.destroyAllWindows()
