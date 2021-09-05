import cv2
import numpy as np

kernal = np.ones((5, 5), np.uint8)

img = cv2.imread("resource/test.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(imgGray, 100, 100)
imgDialate = cv2.dilate(imgCanny, kernal, iterations=1)
imgEroded = cv2.erode(imgCanny, kernal, iterations=1)

cv2.imshow("img imgCanny", imgCanny)
cv2.imshow("img imgDialate", imgDialate)
cv2.imshow("img imgEroded", imgEroded)
cv2.waitKey(0)
