# Q14 - Factorial using recursion (Alternative Version)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

try:
    number = int(input("Enter number: "))
    if number < 0:
        print("Factorial not defined for negative numbers.")
    else:
        print("Factorial:", factorial(number))

except:
    print("Invalid input.")