# Q10 - ATM Simulator (Alternative Version)

def atm():
    current_balance = 10000

    while True:
        print("\n1.Check 2.Deposit 3.Withdraw 4.Exit")

        try:
            user_choice = int(input("Choose option: "))

            if user_choice == 1:
                print("Balance:", current_balance)

            elif user_choice == 2:
                amount = float(input("Deposit amount: "))
                if amount > 0:
                    current_balance += amount
                    print("Deposited successfully.")
                else:
                    print("Enter positive amount.")

            elif user_choice == 3:
                amount = float(input("Withdraw amount: "))
                if amount <= 0:
                    print("Enter valid amount.")
                elif current_balance - amount < 500:
                    print("Minimum balance of 500 required.")
                else:
                    current_balance -= amount
                    print("Withdrawal successful.")

            elif user_choice == 4:
                break
            else:
                print("Invalid option.")

        except:
            print("Invalid input.")

atm()