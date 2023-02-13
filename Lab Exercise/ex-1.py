import cv2

#reading image from the local
img = cv2.imread('akatsuki.jpg')

#Resizing the image to our convenient
idn = cv2.resize(img,(400,480))

#Real Image
cv2.imshow('image',idn)
cv2.waitKey(0)

#image from BGR-to-RGB
id1 = cv2.cvtColor(idn,cv2.COLOR_BGR2RGB)
cv2.imshow('image',id1)
cv2.waitKey(0)

#image from BGR-to-GRAY
id2 = cv2.cvtColor(idn,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',id2)
cv2.waitKey(0)

#image from BGR-to-HSV
id3 = cv2.cvtColor(idn,cv2.COLOR_BGR2HSV)
cv2.imshow('image',id3)
cv2.waitKey(0)

#image from BGR-to-YUV
id3 = cv2.cvtColor(idn,cv2.COLOR_BGR2YUV)
cv2.imshow('image',id3)
cv2.waitKey(0)
cv2.destroyAllWindows()
