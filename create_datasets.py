import cv2
import pandas as pd
import os
from time import sleep


def create_image_database():

    camera = cv2.VideoCapture(0)

    student_names = []

    df = pd.read_csv('BTECHU.csv')

    for index, row in df.iterrows():
        name = str.capitalize(row.Name)
        name = str.replace(name, " ", "_")
        student_names.append(name)

    print("Creating database for each student for model training .....\n\n")
    for i, student in enumerate(student_names):

        print(f"Creating database for {student}")
        path = os.path.join('datasets', student)
        if not os.path.isdir(path):
            os.mkdir(path)

        algo = "haarcascade_frontalface_default.xml"
        haarCascade = cv2.CascadeClassifier(algo)


        count = 1

        while True:
            if count>=1 and count<20:
                print("Please look at the camera...")
            if count>=20 and count<40:
                print("Please look towards your right side...")
            if count>=40 and count<60:
                print("Please look towards your left side...")
            
            # Reading input from the camera
            _,img = camera.read()

            # Converting to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = haarCascade.detectMultiScale(gray, 1.3, 4)

            if count < 61:
                for (x,y,w,h) in faces:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
                    res0 = gray[y:y+h, x:x+w]
                    if res0 is None or res0.size == 0:
                        print("Error: Cropped region is empty or invalid.")
                        continue
                    
                    # Resize the cropped region
                    resized = cv2.resize(res0, (200, 200))
                    img_name = path + "/" + student_names[0] + str(count) + ".jpg"
                    cv2.imwrite(img_name, resized)
                    count = count + 1
            
            # Parametres for the imshow and putting text function
            font = cv2.FONT_HERSHEY_COMPLEX
            fontscale = 1
            color = (255, 255, 0)
            coord = (30, 30)
            thickness = 1

            if count>=1 and count<20:
                texttoput = "Please look at the camera..."
            elif count>=20 and count<40:
                texttoput = "Please look towards your right side..."
            elif count>=40 and count<60:
                texttoput = "Please look towards your left side..."

            cv2.imshow("Creating your face's database", img)
            cv2.putText(img,texttoput, coord, font, fontscale, color, thickness, cv2.LINE_AA)

            if (count == 20 or count == 40 or count == 1):
                sleep(5)

            key = cv2.waitKey(1)
            if key == 113:
                break

            if count >= 61:
                break
        user_input = input("Press any key to continue or enter 'q' to quit: ")
        if user_input == 'q':
            break
        if i < len(student_names)-1:
            print(f"Please call the next student with name : {student_names[i+1]}")

    camera.release()
    cv2.destroyAllWindows()

# created_image_database()