# Q6 - Grade Calculator (Alternative Version)
# This version separates grade logic into its own function.

def calculate_grade(percentage):
    # Determine grade based on percentage
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

try:
    subjects = 5
    total_marks = 0
    pass_status = True

    # Taking marks for fixed number of subjects
    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        total_marks += mark

        # If any subject is below 40, student fails
        if mark < 40:
            pass_status = False

    percentage = total_marks / subjects
    grade = calculate_grade(percentage)

    print("\nTotal Marks:", total_marks)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", "Pass" if pass_status else "Fail")

except:
    print("Invalid input.")