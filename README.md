# An Attendance taking system assisted by AI
# Mainly using Opencv

- Create a program to build databases for recognising faces
- Create a python program to recognise a face
- Build Functionality for exporting the collected data into an excel sheet or something else


# I have created the above basic three programs which fullfill the following functions

- created a program to test the working for camera
created a program which takes a list of students and creates database for each of the students in the list
    - This simply creates a folder with the name of the student in the "database" folder
    - the subfolder contains 60 images of each particular student
    - the model takes these images and trains itself to recognise them later on
    - then we can simply use the "model.predict()" function to run the prediction over the image

## Now comes the enhancement part
I need to arrange all these functionalities into separate functions for later use
- Create a program to take input for the details of the students
so that they can be exported into a csv or an excel sheet
    - This will allow us to manage all the students in a single place
    - we can import these into the program for training and recognisation
- ### We need to create a working interface where the main attendance taker can be turned on, the basic features will be as follows

    1. Take pictures of students in the class at each interval, say 10 minutes.
    2. Run the algorithm to find all the faces in the pictures
    3. Match these faces in the databases, <b>Then create an excel or csv sheet which indicates, if the student is present, the value is 1, and 0 if not. Also mention the date</b>
    4. Also implement a text to speech function <b>which declares the current date and the toatal present studets out of the total strength</b>
    5. If an unknown face is found, it stores them into a folder, <b>and then, sends an email to the teacher informing them to check the attendance and make up for any unknowns.</b>