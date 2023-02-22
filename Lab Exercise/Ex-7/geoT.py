import numpy as np
import cv2 as cv
#Give image
#getting input image 
im = cv.imread('joker.jpg',1)
img = cv.resize(im,(480,720))

#scale function resize the image
def scale(img,r,c):
    res = cv.resize(img,None,fx=r, fy=c, interpolation = cv.INTER_CUBIC)
    return res
#translate move image inside the frame
def trans(img):
    rows,cols = img.shape[:2]
    M = np.float32([[1,0,10],[0,1,50]])
    res = cv.warpAffine(img,M,(cols,rows))
    return res
#it Rotate the image with degree
def rotate(img,deg):
    rows,cols = img.shape[:2]
    # cols-1 and rows-1 are the coordinate limits.
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),deg,1)
    res = cv.warpAffine(img,M,(cols,rows))
    return res
#tilt the image into slanting
def tilt(img):
    rows,cols,ch = img.shape[:3]
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,200]])
    M = cv.getAffineTransform(pts1,pts2)
    res = cv.warpAffine(img,M,(cols,rows))
    return res
#it magnify the image and get the image focused
def zoom(img):
    rows,cols,ch = img.shape[:3]
    pts1 = np.float32([[46,65],[300,65],[46,300],[300,300]])
    pts2 = np.float32([[10,10],[350,10],[10,350],[350,350]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    res = cv.warpPerspective(img,M,(cols,rows))
    return res

cv.imshow('Actual',img)
cv.waitKey()
cv.imshow('Scaled Image',scale(img,1,2))
cv.waitKey()
cv.imshow('Image Translation',trans(img))
cv.waitKey()
cv.imshow('Rotated Image',rotate(img,25))
cv.waitKey()
cv.imshow('Tilted Image',tilt(img))
cv.waitKey()
cv.imshow('Focused Image',zoom(img))
cv.waitKey()
cv.destroyAllWindows()
