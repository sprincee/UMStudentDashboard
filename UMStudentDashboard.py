
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


#A function to input classes into a list
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
        student_data["Q1"].append(grades[0])
        student_data["Q2"].append(grades[1])
        student_data["Q3"].append(grades[2])
        student_data["Q4"].append(grades[3])
    return student_data

#A function to start creating data visualizations
def create_dataframe(student_data):
    return pd.DataFrame(student_data)


def boxplot(df):
    df_melted = df.melt(id_vars=["School Year", "Student ID", "Name", "Class"], 
                        value_vars=["Q1", "Q2", "Q3", "Q4"], 
                        var_name="Quarter", value_name="Grade")
    df_melted.boxplot(by='Quarter', column='Grade', grid=True)
    plt.title("Grade-Distribution by Quarter")
    plt.suptitle('')
    plt.xlabel('Quarter')
    plt.ylabel('Grade')
    plt.show()

def indvidual_class_performance_line(df, classes):
    for class_name in classes:
        class_df = df[df['Class'] == class_name]
        class_df.set_index('Class')[["Q1","Q2","Q3","Q4"]].T.plot()
        plt.title(f"Performance in {class_name} over Quarters")
        plt.xlabel("Quarter")
        plt.ylabel("Grade")
        plt.legend([class_name])
        plt.show()

def display_summary(df):
    df['Average'] = df[["Q1","Q2","Q3","Q4"]].mean(axis=1)
    print("\nSummary Statistics:")
    print(f"Overall Average Grade: {df['Average'].mean()}")
    print(f"Highest Grade: {df[['Q1','Q2','Q3','Q4']].max().max()}")
    print(f"Lower Grade: {df[['Q1','Q2','Q3','Q4']].min().min()}")

def main():
    school_year = input_school_year()
    student_id, name = input_student_data()
    classes = input_classes()
    student_data = input_grades(classes, student_id, name, school_year)

    df = create_dataframe(student_data)

    while True:
        print("\nWhat information would you like to see?")
        print("1. Grade Box Plot by Quarter")
        print("2. Individual Class Performance Over Time")
        print("3. Summary Statistics")
        print("4. EXIT!")
        user_choice = input("Enter choice (1-4): ")

        if user_choice == '1':
            boxplot(df)
        elif user_choice == '2':
            indvidual_class_performance_line(df, classes)
        elif user_choice == '3':
            display_summary(df)
        elif user_choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

#Function Caller
main()
