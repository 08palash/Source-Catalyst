import cv2
img_loc = '' #enter your file location
filename = '' #enter your file

#read the img

img = cv2.imread(img_loc+filename)

#convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



#to show image
cv2.imshow('original image', img)
cv2.imshow('Gray image', gray_img)
cv2.waitKey()