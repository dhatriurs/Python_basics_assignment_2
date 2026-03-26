# Q2 - Basic Calculator
# This version uses separate calculations instead of printing directly.

try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    power_value = first_number ** second_number

    print("\nCalculation Results")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)

    # Only perform division if denominator is not zero
    if second_number != 0:
        division = first_number / second_number
        modulus = first_number % second_number
        print("Division:", division)
        print("Modulus:", modulus)
    else:
        print("Division and modulus cannot be performed (zero denominator).")

    print("Power:", power_value)

except:
    print("Invalid input. Numbers expected.")