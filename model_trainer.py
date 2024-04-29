import cv2
import os
import numpy as np

face_rec_algo = 'haarcascade_frontalface_default.xml'
datasets_folder = 'dataset'
(images, labels, names, id) = ([], [], {}, 0)
camera = cv2.VideoCapture(1)

for (subdir, dirs, files) in os.walk(datasets_folder):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets_folder, subdir)
        for filename in os.listdir(subjectpath):
            path = f"{subjectpath}/{filename}"
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1

(images, labels) = [np.array(lis) for lis in [images, labels]]
width, height = 220, 190
facecascade = cv2.CascadeClassifier(face_rec_algo)
model = cv2.face.LBPHFaceRecognizer_create()
# cv2.face.FisherFaceRecognizer_create()

model.train(images, labels)
count = 0
while True:
    (_, img) = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces =  facecascade.detectMultiScale(gray, 1.3, 5)
    for (x, y,w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
        face = gray[y:y+h, x:x+w]
        prediction = model.predict(face)

        if prediction[1]<800:
            textpmImg = names[prediction[0]]
            cv2.putText(img, textpmImg, (x, y-20), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  0.5, (0, 255, 0), 2)
            count = 0
        else:
            print("The faces did not match...\nUnkown face")
            count += 1
            if (count >150):
                cv2.putText(img, "Unknown face", (x-10, y-10), cv2.putText(img, '%s-%.0f' % (names[prediction[0]], prediction[1]), (x-10, y-20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, float(255), 2), (255,255, 0), 2)
                cv2.imwrite("unknown.png", img)
                count = 0
    
    cv2.imshow("Face recognition", img)
    key = cv2.waitKey(1)
    if key == 113:
        break

camera.release()
cv2.destroyAllWindows()