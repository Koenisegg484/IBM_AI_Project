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

import create_datasets
import model_trainer

menu = """

This is an ML Application which has been created to take attendance of an ongoing class, without disrupting the flow between teachers and students.
It has the following functions :\n



"""