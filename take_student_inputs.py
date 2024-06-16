import csv

class Student:
    def __init__(self,firstname, lastname, age, email):
        self.firstname = str.capitalize(firstname)
        self.lastname = str.capitalize(lastname)
        self.age = age
        self.email = email



class Class_of_students:
    def __init__(self, department, year, section, Students) -> None:
        self.department = str.upper(department)
        self.year = year
        self.section = str.capitalize(section)
        self.students = Students
        self.total = len(self.students)

# Taking inputs and creating the students database
def create_class():
    print("...First enter the details of the Class...")
    dept = input("Enter the department : ")
    year = input("Enter the year  : ")
    section = input("Enter the section : ")
    total_students = int(input("Enter the number of total students : "))
    Students = []
    for i in range(0, total_students):
        fname = input("Enter first name of the student : ")
        lname = input("Enter last name of the student : ")
        age = int(input("Enter age of the student : "))
        email = (input("Enter email of the student : "))
        print(f"\nNow for Student number : {i+1}\n\n")

        stdnt = Student(fname, lname, age, email)
        Students.append(stdnt)

    cls1 = Class_of_students(dept, year, section, Students)

    filename = cls1.department + cls1.section + ".csv"
    fields = ['Name', 'Branch', 'Year', 'Section', 'Email', 'Age']
    with open (filename, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        writer.writeheader()
        for std in cls1.students:
            row = {
                'Name' : f"{std.firstname} {std.lastname}", 
                'Branch' : cls1.department, 
                'Year' : cls1.year,
                'Section' : cls1.section,
                'Email' : std.email,
                'Age' : std.age
            }
            writer.writerow(row)