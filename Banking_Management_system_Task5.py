# Console-Based Banking Management System
# Problem Statement
# Develop a console-based Banking Management System in Python using Object-Oriented Programming (OOP).
# The system should support two types of bank accounts: Savings Account and Current Account. Users should be able to create accounts, deposit money, withdraw money, and check their account balance through a console menu.
# 1. Classes and Inheritance
# Create a parent class named BankAccount with the following attributes:
# Account holder name
# Account number
# Account balance
# Create two child classes:
# SavingsAccount
# CurrentAccount
# Both child classes must inherit common properties and methods from BankAccount.
# 2. Encapsulation
# Protect the account balance from direct modification.
# Provide a method to retrieve the current balance.
# Allow balance changes only through deposit and withdrawal methods.
# Do not allow users to deposit or withdraw zero or negative amounts.
# 3. Polymorphism
# Implement a withdraw() method in both child classes with different rules.
# Savings Account:
# A user cannot withdraw more than the available balance.
# If the requested amount exceeds the balance, display an insufficient balance message.
# Current Account:
# A user can withdraw more than the available balance.
# The account has an overdraft limit of Rs. 5,000.
# The balance must never fall below negative Rs. 5,000.
# 4. Console Menu
# Display the following menu repeatedly until the user chooses to exit:
# Create Savings Account
# Create Current Account
# Deposit Money
# Withdraw Money
# Check Balance
# Display Account Details
# Exit
# 5. Account Creation
# When creating an account, ask the user to enter:
# Account holder name
# Account number
# Initial deposit
# For a Current Account, also configure the overdraft limit to Rs. 5,000.
# For simplicity, assume each account number is unique.
# 6. Account Management
# Store created accounts so users can perform multiple transactions.
# Ask for the account number before depositing, withdrawing, or checking a balance.
# Display an appropriate message if the account does not exist.
# Validate user input and handle invalid numeric input without crashing the program.
# Prevent duplicate account numbers.
# 7. Test Cases
# Test 1: Create a Savings Account (Valid Input)
# Account type: Savings
# Name: Ali
# Account number: 101
# Initial deposit: Rs. 10,000
# Expected result: Account created successfully with a balance of Rs. 10,000.
# Test 2: Deposit Money (Valid Input)
# Starting balance: Rs. 10,000
# Account number: 101
# Deposit: Rs. 2,000
# Expected result: New balance: Rs. 12,000.
# Test 3: Successful Savings Withdrawal (Valid Input)
# Starting balance: Rs. 12,000
# Withdraw: Rs. 5,000
# Expected result: Withdrawal successful. New balance: Rs. 7,000.
# Test 4: Insufficient Savings Balance (Invalid Transaction)
# Starting balance: Rs. 7,000
# Withdraw: Rs. 8,000
# Expected result: Display Insufficient balance! Balance remains Rs. 7,000.
# Test 5: Current Account Overdraft (Valid Input)
# Starting balance: Rs. 10,000; overdraft limit: Rs. 5,000
# Withdraw: Rs. 12,000
# Expected result: Withdrawal successful. New balance: -Rs. 2,000.



# start the code here

class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
        else:
            self.__balance += amount
            print("New balance: Rs.", self.__balance)

    def _reduce(self, amount):
        self.__balance -= amount

    def show(self):
        print("Name:", self.name)
        print("Account No:", self.acc_no)
        print("Balance: Rs.", self.__balance)

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
        elif amount > self.get_balance():
            print("Insufficient balance!")
        else:
            self._reduce(amount)
            print("Withdrawal successful. New balance: Rs.", self.get_balance())

class CurrentAccount(BankAccount):
    def __init__(self, name, acc_no, balance):
        super().__init__(name, acc_no, balance)
        self.overdraft = 5000

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be greater than zero")
        elif amount > self.get_balance() + self.overdraft:
            print("Overdraft limit exceeded!")
        else:
            self._reduce(amount)
            print("Withdrawal successful. New balance: Rs.", self.get_balance())

def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Please enter a valid number")

accounts = {}

while True:
    print("\n1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Check Balance")
    print("6. Display Account Details")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == "1" or choice == "2":
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            print("Account number already exists")
        else:
            balance = get_number("Enter initial deposit: ")
            if balance < 0:
                print("Initial deposit cannot be negative")
            else:
                if choice == "1":
                    accounts[acc_no] = SavingsAccount(name, acc_no, balance)
                else:
                    accounts[acc_no] = CurrentAccount(name, acc_no, balance)
                print("Account created successfully with balance Rs.", balance)

    elif choice in ["3", "4", "5", "6"]:
        acc_no = input("Enter account number: ")
        if acc_no not in accounts:
            print("Account does not exist")
        else:
            acc = accounts[acc_no]
            if choice == "3":
                acc.deposit(get_number("Enter amount: "))
            elif choice == "4":
                acc.withdraw(get_number("Enter amount: "))
            elif choice == "5":
                print("Balance: Rs.", acc.get_balance())
            else:
                acc.show()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
    




