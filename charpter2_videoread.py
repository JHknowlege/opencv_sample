import cv2

cap = cv2.VideoCapture("resource/testvideo.mp4")
while True:
    success, img = cap.read()
    if success:
        cv2.imshow("player", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
