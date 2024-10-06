"""

Building a command line MENU for the following funtionings

    To take the details of a class and add students of the class

    Create a database consisting of 60 images of each student in a separate folder, the folders are named with the student

    Create a model trainig function, this will output a model-dump file
    which can later be used as pre-built and pre-trained models

    Create the main system

        take input of the whole class image
        recognise faces
        map them to their respective names
        create or append an existing excel file
        Add a date column and mark the present students

    if any unknown person is found, send an email to the teacher



"""


menu = """

This is an ML Application which has been created to take attendance of an ongoing class, without disrupting the flow between teachers and students.
It has the following functions :\n

1. Create a Class and input Student details\n
2. Create image database for each student\n
3. Train the model on taken student images\n
4. Take Attendance\n
5. Print Menu again
"""

import create_datasets
import model_trainer
import take_student_inputs
import os

def print_menu():
    print("\nMenu:")
    print("1. Create a Class and input Student details")
    print("2. Create image database for each student")
    print("3. Train the model on taken student images")
    print("4. Take Attendance")
    print("5. Print Menu again")
    print("6. Exit application")

def report_generator():
    present_students = model_trainer.take_attendence()
    names = []
    for (subdir, dirs, files) in os.walk('dataset'):
        for subdir in dirs:
            textpmImg = str.capitalize(str.replace(subdir, "_", " "))
            names.append(textpmImg)
    
    model_trainer.attendence_report(present_students, names)
    print("\n... The report has been generated, please check your email ...\n")

# Define the menu options and corresponding functions
# Main loop
print_menu()
choice = int(input("Enter your choice: "))
while choice != 6:
    
    # Check if the choice is a valid menu option
    if choice == 1:
        take_student_inputs.create_class()

    elif choice == 2:
        create_datasets.create_image_database(),
     
    elif choice == 3:
        model_trainer.train_model(),

    elif choice == 4:
        report_generator(),

    elif choice == 5:
        print_menu(),

    else:
        print("Invalid choice. Please enter a valid menu option.")

    choice = int(input("Enter your choice: "))
print("\n###Exitting application###\n")
