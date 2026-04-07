bank_name = "State Bank of Python"

class BankAccount:
    bank_code = "SBP001"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    @staticmethod
    def change_bank():
        global bank_name  # 🔑 Required to modify global variable
        bank_name = "New Bank"

acc = BankAccount("Deepak", 1000)
acc.change_bank()

print(bank_name)  # New Bank

