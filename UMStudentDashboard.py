
#Final-Project aka UMStudentDashboard

#UMStudentDashboard

#Imports
import pandas as pd
import matplotlib.pyplot as plt


#A function to collect school year
def input_school_year():
    return input("Enter School Year (YYYY-YYYY): ")


#A function to collect basic student data
def input_student_data():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    return student_id, name


#A function to input classes
def input_classes():
    while True:
        try:
            class_list = input("Enter Classes (seperated by commas, or 'done' to finish): ")
            if class_list.lower == 'done':
                return []
            classes = [class_name.strip() for class_name in class_list.split(',')]
            if len(classes) == 0:
                raise ValueError("No classes entered. Please enter at least one class.")
            return classes
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter the classes again.")


#A function to input grades -- taking parameters like classes, student_id, name, and school_year
def input_grades(classes, student_id, name, school_year):
    student_data = {
        "School Year": [],
        "Student ID": [],
        "Name": [],
        "Class": [],
        "Q1": [],
        "Q2": [],
        "Q3": [],
        "Q4": []
    }
    for class_name in classes:
        while True:
            try:
                grades = input(f"Enter grades for {class_name} (4 quarters, sep. by commas): ")
                grades = [float(grade.strip()) for grade in grades.split(',')]
                if len(grades) != 4:
                    raise ValueError("Please enter exactly 4 grades.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter the grades again.")
        student_data["School Year"].append(school_year)
        student_data["Student ID"].append(student_id)
        student_data["Name"].append(name)
        student_data["Class"].append(class_name)
        student_data["Quarter 1"].append(grades[0])
        student_data["Quarter 2"].append(grades[1])
        student_data["Quarter 3"].append(grades[2])
        student_data["Quarter 4"].append(grades[3])
    return student_data

#A function to start creating data visualizations
def create_dataframe(student_data):
    return pd.DataFrame(student_data)

