# Q1 - Personal Bio Card
# This program takes user details and prints them in a simple format.

def display_bio():
    # Collecting information from user
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    course = input("Enter your course: ")
    college = input("Enter your college: ")
    email = input("Enter your email: ")

    # Printing the details
    print("\nStudent Details")
    print("---------------")
    print("Name    :", name)
    print("Age     :", age)
    print("Course  :", course)
    print("College :", college)
    print("Email   :", email)

# Calling the function
display_bio()