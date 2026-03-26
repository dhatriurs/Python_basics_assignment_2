# Q15 - Prime Checker (Alternative Version)

try:
    number = int(input("Enter number: "))
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not Prime")

except:
    print("Invalid input.")