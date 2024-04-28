import cv2
import imutils

camera = cv2.VideoCapture(1)
image = camera.read()

while True:
    image = camera.read()
    resized = imutils.resize(image, (500, 500))
    cv2.imshow("Camera Feed", resized)
    key = cv2.waitKey("1")
    if key == 'q':
        break

print("Exitted Application successfully")
camera.release()
cv2.destroyAllWindows()