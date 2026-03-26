# Q9 - Ticket Pricing System (Alternative Version)

try:
    age = int(input("Enter age: "))
    day_name = input("Enter day: ").lower()
    ticket_number = int(input("Number of tickets: "))

    # Set price by age category
    if age < 3:
        price = 0
    elif age <= 12:
        price = 150
    elif age <= 59:
        price = 300
    else:
        price = 200

    # Weekend discount logic
    if day_name in ["sat", "saturday", "sun", "sunday"]:
        price = price * 0.8  # 20% discount

    total_cost = price * ticket_number

    print("Price per ticket:", price)
    print("Total cost:", total_cost)

except:
    print("Invalid input.")