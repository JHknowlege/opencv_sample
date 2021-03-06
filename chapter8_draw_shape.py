import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.putText(img, "I'M uncle", (300, 200),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),3)
cv2.imshow("window", img)
cv2.waitKey(0)
