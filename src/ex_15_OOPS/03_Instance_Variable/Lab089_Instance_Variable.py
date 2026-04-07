# 🌍 Global Variable
bank_name = "State Bank of Python"

class BankAccount:
    # 🏫 Class Variable (shared by all accounts)
    bank_code = "SBP001"

    def __init__(self, account_holder, balance):
        # 🏠 Instance Variables (unique for each account)
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # 📦 Local Variable (inside method only)
        transaction_type = "Deposit"

        self.balance += amount

        print("\nTransaction Details:")
        print("Bank:", bank_name)                    # Global variable
        print("Bank Code:", BankAccount.bank_code)   # Class variable
        print("Account Holder:", self.account_holder) # Instance variable
        print("Transaction:", transaction_type)       # Local variable
        print("Updated Balance:", self.balance)


# Creating objects (accounts)
acc1 = BankAccount("Deepak", 1000)
acc2 = BankAccount("Rahul", 2000)

# Perform transactions
acc1.deposit(500)
acc2.deposit(1000)