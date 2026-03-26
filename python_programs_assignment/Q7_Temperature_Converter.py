# Q7 - Temperature Converter (Alternative Version)
# This version uses functions for each conversion.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

try:
    print("1.C to F  2.F to C  3.C to K  4.K to C")
    option = int(input("Enter option: "))
    value = float(input("Enter temperature: "))

    if option == 1:
        print("Converted value:", celsius_to_fahrenheit(value))
    elif option == 2:
        print("Converted value:", fahrenheit_to_celsius(value))
    elif option == 3:
        print("Converted value:", celsius_to_kelvin(value))
    elif option == 4:
        print("Converted value:", kelvin_to_celsius(value))
    else:
        print("Invalid option.")

except:
    print("Invalid input.")