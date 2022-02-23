import cv2
img_loc = '' #enter your file location
filename = '' #enter your file

#read the img

img = cv2.imread(img_loc+filename)

#convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#to invert the image
inverted_gray_img = 255 - gray_img

#blur the img by gaussin func
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21,21), 0)

#invert the blurred img
inverted_blurred_img = 255 - blurred_img

#creating pencil sketch img
pencil_sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

#to show image
cv2.imshow('original image', img)
cv2.imshow('Gray image', pencil_sketch_img)
cv2.waitKey()