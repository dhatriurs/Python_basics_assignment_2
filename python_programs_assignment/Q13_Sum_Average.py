# Q13 - Sum and Average (Alternative Version)

try:
    values = list(map(float, input("Enter numbers separated by space: ").split()))

    total = 0
    for v in values:
        total += v

    avg = total / len(values)

    print("Sum:", total)
    print("Average:", avg)
    print("Max:", max(values))
    print("Min:", min(values))

except:
    print("Invalid input.")