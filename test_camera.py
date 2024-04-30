import cv2
import imutils

camera = cv2.VideoCapture(0)
# _,image = camera.read()

while True:
    _,image = camera.read()
    # resized = cv2.resize(image, (500, 500))
    resized = imutils.resize(image, height=500, width=500)
    cv2.imshow("Camera Feed", resized)
    key = cv2.waitKey(1)
    if key == 113:
        break

print("Exitted Application successfully")
camera.release()
cv2.destroyAllWindows()