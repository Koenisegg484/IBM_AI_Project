import cv2
import pandas as pd
import os
# import numpy as np
# import imutils
# from time import sleep

face_detection_algo = 'haarcascade_frontalface_default.xml'

datasets_folder = 'datasets'

# Defining the resolution of images to be stored
(width, height) = (260, 200)
# Face detection algorithm
face_cascade = cv2.CascadeClassifier(face_detection_algo)
# Initialising camera object
camera = cv2.VideoCapture(1)

student_names = []

df = pd.read_csv('BTECH CSEU.csv')

# for index, row in df.iterrows():
#     name = str.lower(row.Name)
#     name = str.replace(name, " ", "")
#     student_names.append(name)
# for std in student_names:
#     print(std)

print("Creating database for each student for model training .....\n\n\n")
for i, student in enumerate(student_names):

    print(f"Creating database for {student}")
    path = os.path.join(datasets_folder, student)
    if not os.path.isdir(path):
        os.mkdir(path)


    count = 1

    while True:
        if count>=1 and count<20:
            print("Please look at the camera...")
        if count>=20 and count<40:
            print("Please look towards your right side...")
        if count>=40 and count<60:
            print("Please look towards your left side...")
        
        # Reading input frm the camera
        _, img = camera.read()
        # Converting to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)

        if count < 61:
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
                resized = gray[y:y+5][x:x+w]
                resized = cv2.resize(resized, (width, height))
                img_name = path + "/" + student_names[0] + str(count) + ".jpg"
                cv2.imwrite(img_name, resized)
                count = count + 1
        
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        fontscale = 1
        color = (255, 0, 0)
        coord = (10, 10)
        thickness = 2

        if count>=1 and count<20:
            texttoput = "Please look at the camera..."
        elif count>=20 and count<40:
            texttoput = "Please look towards your right side..."
        elif count>=40 and count<60:
            texttoput = "Please look towards your left side..."

        cv2.putText(img,texttoput, coord, font, fontscale, color, thickness, cv2.LINE_AA)
        cv2.imshow("Creating your face's database", img)

        key = cv2.waitKey(1)
        if key == 113 and count > 51:
            break

        if count >= 61:
            break
        user_input = input("Press any key to continue or enter 'q' to quit: ")
        if user_input == 'q':
            break
        if i < len(student_names):
            print(f"Please call the next student with name : {student_names[i+1]}")

camera.release()
cv2.destroyAllWindows()