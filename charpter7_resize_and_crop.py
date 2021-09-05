import cv2
import numpy as np

kernal = np.ones((5, 5), np.uint8)

img = cv2.imread("resource/test.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize = cv2.resize(imgGray,(200,300))
cropImg = imgGray[0:200,200:400]
cv2.imshow("img imgGray", imgGray)
cv2.imshow("img resize", resize)
cv2.imshow("img cropImg", cropImg)
cv2.waitKey(0)
