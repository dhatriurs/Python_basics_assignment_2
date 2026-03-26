# Q12 - Multiplication Table (Alternative Version)

try:
    num = int(input("Enter number: "))

    i = 1
    while i <= 10:
        print(num, "x", i, "=", num * i)
        i += 1

except:
    print("Invalid input.")