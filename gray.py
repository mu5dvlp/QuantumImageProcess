import cv2

fileName = "sample.jpg"
image = cv2.imread(fileName)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg', gray_image)