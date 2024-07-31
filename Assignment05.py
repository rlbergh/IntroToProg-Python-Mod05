# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Rebecca Bergh,7/28/2024,Commentify old code, add try function, import json
#   Rebecca Bergh,7/29/2024,Add nested if/then statement and the rest of the menu choices
#   Rebecca Bergh,7/29/2024,Deleted old code
#   Rebecca Bergh,7/30/2024,Added error handling for first name, last name and menu_choice 3
# ------------------------------------------------------------------------------------------ #

#Import json

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict[str, str] = {}  # one row of student data
students: list = []  # a table of student data
file_exists: bool = True
first_char: str = ''  # first character of existing json file

# test whether the json file exists
try:
    file = open(FILE_NAME,'r')
    file.close()
# if it doesn't, set variable to false
except FileNotFoundError:
    file_exists = False
# if the file exists, read it
if file_exists:
    # if the file exists, see if it's empty or not
    file = open(FILE_NAME,'r')
    # read first character
    first_char = file.read(1)
    # if it's empty, do nothing
    if not first_char:
        pass
    else:
        file = open(FILE_NAME, 'r')
        students = json.load(file)
        file.close()
        for student_data in students:
            print(f'{student_data["FirstName"]} {student_data["LastName"]\
                } is registered for {student_data["CourseName"]}.')

# if the file doesn't exist, create it and close it
else:
    print('Setting up enrollment file...')
    file = open(FILE_NAME,'w')
    file.close()

# gather and process data
while True:

    print(MENU)
    menu_choice = input('What would you like to do? ')

    # Get data inputs and show result
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name can only have alphabetic characters")
        except ValueError as e:
            print(e)
            student_first_name = input("Try entering the student's first name again: ")
        finally:
            try:
                student_last_name = input("Enter the student's last name: ")
                if not student_last_name.isalpha():
                    raise ValueError("Last name can only have alphabetic characters")
            except ValueError as e:
                print(e)
                student_last_name = input("Try entering the student's last name again: ")
            finally:
                course_name = input("Enter the course name: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name,"CourseName": course_name}
            students.append(student_data)
            # print result
        print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        continue

    # print current data, including what was loaded in at the beginning (if applicable)
    elif menu_choice == "2":
        for row in students:
            print(f'{row["FirstName"]} {row["LastName"]\
                } is registered for {row["CourseName"]}.')
        continue

    # save data to the json file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME,"w")
            json.dump(students, file, indent=1)
        except AttributeError as e:
            print(e, e.__doc__)
        finally:
            file.close()

    # End loop
    elif menu_choice == "4":
        print("Exiting program...")
        break

    # result if anything other than 1, 2, 3, or 4 is typed.
    else:
        print("Please select a valid menu choice")