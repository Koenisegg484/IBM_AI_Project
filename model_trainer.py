import cv2
import os
import numpy as np
import datetime
import csv
import pandas as pd

face_rec_algo = 'haarcascade_frontalface_default.xml'


def train_model():
    datasets_folder = './dataset'
    (images, labels, names, id) = ([], [], {}, 0)

    # Traverse the dataset folder
    for (subdir, dirs, files) in os.walk(datasets_folder):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets_folder, subdir)
            print(f"printing subjectpath : {subjectpath}")
            for filename in os.listdir(subjectpath):
                path = os.path.join(subjectpath, filename)
                label = id
                img = cv2.imread(path)
                if img is None:
                    print(f"Warning: Could not read image {path}")
                    continue
                images.append(img)
                labels.append(int(label))
            id += 1

    # Convert lists to numpy arrays
    (images, labels) = [np.array(lis) for lis in [images, labels]]

    print(f"Number of images: {len(images)}")
    print(f"Labels: {labels}")

    if len(images) == 0:
        print("Error: No images found for training.")
        return

    # Initialize the model
    model = cv2.face.FisherFaceRecognizer_create()
    # Train the model
    model.train(images, labels)

    # Save the trained model
    model.save("facial_recog_model.xml")
    print("Model trained and saved successfully.")

def take_attendence():
    model = None

    model = cv2.face.FisherFaceRecognizer_create()
    model.read("facial_recog_model.xml")

    names = []
    present_students = []
    for (subdir, dirs, files) in os.walk('dataset'):
        for subdir in dirs:
            names.append(subdir)

    print(names)
    print(present_students)
    facecascade = cv2.CascadeClassifier(face_rec_algo)

    count = 0
<<<<<<< HEAD
    closer = 0
    camera = cv2.VideoCapture(1)
=======
    camera = cv2.VideoCapture(0)
>>>>>>> a47acc58cd588c62d7a0048ca192ccb4114aad73
    unknowns_found = 0
    while closer < 200:
        (_, img) = camera.read()
        # img = cv2.imread("./test1.jpg")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces =  facecascade.detectMultiScale(gray, 1.3, 5)
        print(f"Length of faces {len(faces)}")
        a = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (100, 100))
            cv2.imwrite(f"face{a}.jpg", face)
            a=a+1
            prediction = model.predict(face)
            print(prediction)
            print(names[prediction[0]])

            if prediction[1]<800:
<<<<<<< HEAD
                textpmImg = str.capitalize(str.replace(names[prediction[0]], "_", " "))
                cv2.putText(img, textpmImg, (x, y-20), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  0.5, (0, 255, 0), 2)
                if textpmImg in present_students:
                    continue
                else:
                    present_students.append(textpmImg)
=======
                textonImg = str.capitalize(str.replace(names[prediction[0]], "_", " "))
                cv2.putText(img, textonImg, (x, y-20), cv2.FONT_HERSHEY_PLAIN,  3, (0, 255, 0), 2)
                present_students.append(textonImg)
>>>>>>> a47acc58cd588c62d7a0048ca192ccb4114aad73
                count = 0
            else:
                print("The faces did not match...\nUnkown face")
                count += 1
                if (count > 100):
                    cv2.putText(img, "Unknown person", (x-10, y-20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, float(255), 2, (255,255, 0), 2)
                    # cv2.putText(img, '%s-%.0f' % (names[prediction[0]], prediction[1]), (x-10, y-20), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, float(255), 2, (255,255, 0), 2)

                    unknown_path = os.path.join("Unknowns", str(datetime.date.today().strftime("%d-%m-%Y")))
                    if not os.path.isdir(unknown_path):
                        os.mkdir(unknown_path)
                    unknown_image = os.path.join(unknown_path, f"Unknown{unknowns_found}.jpg")
                    unknowns_found += 1
                    cv2.imwrite(unknown_image, img[y:y+h, x:x+w])

                    count = 0
        while True:
            cv2.imshow("Face recognition", img)
            key = cv2.waitKey(0)
            if key == 113:
                break

<<<<<<< HEAD
    # Creating report of the present student
    report = f"""Date : {datetime.date.today().strftime("%d-%m-%Y")}\nTotal present out of {len(names)} : {len(present_students)}\n"""
    print(report)
    for ind, stdntt in enumerate(present_students):
        print(f"{ind}. {stdntt}")
    camera.release()
    cv2.destroyAllWindows()
    return present_students
=======
        adf = input("Enter q to continue : ")

        # Creating report of the present students
        report = f"""Date : {datetime.date.today().strftime("%d-%m-%Y")}\nTotal present out of {len(names)} : {len(present_students)}\n"""
        print(report)
        for ind, stdntt in enumerate(present_students):
            print(f"{ind+1}. {stdntt}")
        camera.release()
        cv2.destroyAllWindows()
        print(names)
        print(present_students)
        return present_students

>>>>>>> a47acc58cd588c62d7a0048ca192ccb4114aad73

def attendence_report(present_students, all_students):
    attendance_sheet = 'BTECH CSEU Attendance.csv'
    today = str(datetime.date.today().strftime("%D%M%Y"))
    if not os.path.exists(attendance_sheet):
        with open(attendance_sheet, 'w') as attendance_sheet:
            writer = csv.DictWriter(attendance_sheet, fieldnames=["Sr. no", "Student Names", today])
            writer.writeheader()
            for i, st in enumerate(all_students):
                row = {
                    'Sr. no' : i+1,
                    'Student Names' : st
                }
                writer.writerow(row)
<<<<<<< HEAD
    
    df = pd.read_csv(attendance_sheet)
    today = str(datetime.date.today().strftime("%D%M%Y"))
    df[today] = 'A'
    for index, row in df.iterrows():
        if (row['Student Names']) in present_students:
            df.at[index, today] = 'P'
=======
    else:
        df = pd.read_csv(attendance_sheet)
        
        df[today] = 'Absent'
        for index, row in df.iterrows():
            if (row['Student Names']) in present_students:
                df.at[index, today] = 'Present'
>>>>>>> a47acc58cd588c62d7a0048ca192ccb4114aad73

    df.to_csv(attendance_sheet, index=False)