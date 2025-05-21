class Atm:
    def __init__(self):
        self.current_card = None
        self.is_authenticated = False

    def insert_card(self, card):
        if self.current_card:
            print("Please eject the card first")
            return
        self.current_card = card

    def validate_pin(self, input_pin):
        if self.current_card.validate_pin(input_pin):
            print("Congratulations!! Pin matched")
            self.is_authenticated = True
            return True
        print("Sorry!! Incorrect Pin entered")
        return False

    def withdraw_money(self, amount):
        if not self.is_authenticated:
            print("Enter your pin first")
            return
        status = self.current_card.account.withdraw(amount)
        if status:
            print("Withdrawal Successful")
            return
        print("Not enough Balance")
        return

    def deposit_money(self, amount):
        if not self.is_authenticated:
            print("Enter your pin first")
            return
        self.current_card.account.deposit(amount)
        print("Deposit Successful")

    def show_remaining_balance(self):
        if not self.is_authenticated:
            print("Enter your pin first")
            return
        balance = self.current_card.account.get_balance()
        print(f"Remaining Balance is - {balance}")

    def eject_card(self):
        print("Card ejected. Thank you")
        self.is_authenticated = False
        self.current_card = None

