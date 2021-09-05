import cv2

img = cv2.imread("resource/test.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("output", imgGray)
cv2.waitKey(0)
