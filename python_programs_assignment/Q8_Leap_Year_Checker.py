# Q8 - Leap Year Checker (Alternative Version)

def check_leap(year):
    # Basic leap year condition
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

try:
    year_input = int(input("Enter year: "))

    if check_leap(year_input):
        print("Leap Year")
    else:
        print("Not a Leap Year")

except:
    print("Invalid year.")