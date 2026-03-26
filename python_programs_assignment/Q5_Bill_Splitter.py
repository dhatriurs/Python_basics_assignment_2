# Q5 - Bill Splitter with Tax and Tip

try:
    bill_amount = float(input("Enter total bill: "))
    people_count = int(input("Enter number of people: "))
    tax_rate = float(input("Enter tax percentage: "))
    tip_rate = float(input("Enter tip percentage: "))

    # Adding tax to bill
    tax_value = bill_amount * tax_rate / 100
    bill_total = bill_amount + tax_value

    # Adding tip
    tip_value = bill_total * tip_rate / 100
    grand_total = bill_total + tip_value

    # Splitting equally
    share_per_person = grand_total / people_count

    print("\nFinal Bill Summary")
    print("Grand Total:", grand_total)
    print("Each person pays:", share_per_person)

except ZeroDivisionError:
    print("Number of people must be greater than zero.")
except:
    print("Invalid input.")