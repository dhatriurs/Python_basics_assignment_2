# Q11 - Pattern Printer (Alternative Version)

try:
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        # Printing numbers from 1 to current row number
        for j in range(i):
            print(i, end=" ")
        print()

except:
    print("Invalid input.")
    