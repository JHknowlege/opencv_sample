import cv2

img = cv2.imread("resource/two_circle.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(imgGray, 100, 100)
cv2.imshow("img canny", imgCanny)
cv2.imshow("img gray", imgGray)
cv2.imshow("img blur", imgBlur)
cv2.waitKey(0)
