
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
            
