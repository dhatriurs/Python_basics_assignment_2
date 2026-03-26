# Q20 - Number Functions (Alternative Simplified Version)

try:
    number = int(input("Enter a number: "))

    # Factorial calculation
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    # Sum of digits
    digit_sum = sum(int(d) for d in str(abs(number)))

    # Reverse number
    reversed_number = int(str(number)[::-1])

    print("Factorial:", fact)
    print("Sum of digits:", digit_sum)
    print("Reversed number:", reversed_number)

except:
    print("Invalid input.")