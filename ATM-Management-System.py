balance = 10000
pin = "1234"

def check_balance():
    print(f"\nAvailable Balance: ₹{balance}")

def deposit():
    global balance
    amount = float(input("Enter Deposit Amount: ₹"))
    if amount > 0:
        balance += amount
        print("Amount Deposited Successfully.")
        print("Available Balance: ₹", balance)
    else:
        print("Invalid Amount!")

def withdraw():
    global balance
    amount = float(input("Enter Withdrawal Amount: ₹"))
    if amount <= 0:
        print("Invalid Amount!")
    elif amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Please Collect Your Cash.")
        print("Available Balance: ₹", balance)

def change_pin():
    global pin
    old_pin = input("Enter Old PIN: ")

    if old_pin == pin:
        new_pin = input("Enter New PIN: ")
        confirm_pin = input("Confirm New PIN: ")

        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN Changed Successfully.")
        else:
            print("PIN Mismatch!")
    else:
        print("Incorrect Old PIN!")

print("========== ATM MANAGEMENT SYSTEM ==========")

login_pin = input("Enter Your 4-Digit PIN: ")

if login_pin == pin:

    while True:

        print("\n========== MENU ==========")
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            change_pin()

        elif choice == "5":
            print("Thank You For Using Our ATM.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")