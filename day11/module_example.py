import cv2
imagePath = "/Users/shashisharma/Desktop/sampleimage.jpeg"
image = cv2.imread(imagePath)

cv2.imshow("My Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()