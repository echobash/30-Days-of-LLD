class Account:
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True

    def deposit(self, amount):
        self.balance = self.balance + amount
        return True
