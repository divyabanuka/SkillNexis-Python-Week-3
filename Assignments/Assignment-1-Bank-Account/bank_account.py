# SkillNexis Python Programming
# Week 3 - Assignment 1
# Bank Account Class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Withdrawal successful!")

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Current Balance: ₹", self.balance)


print("================================")
print("       BANK ACCOUNT")
print("================================")

name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: ₹"))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: ₹"))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using Bank Account!")
        break

    else:
        print("Invalid choice.")