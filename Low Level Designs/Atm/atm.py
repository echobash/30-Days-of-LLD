from transactionStrategy import TransactionStrategy


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

    def execute_transaction(self, transaction_strategy: TransactionStrategy, amount: int = None) -> None:
        if not self.current_card:
            print("Please enter the card")
            return
        if not self.is_authenticated:
            print("Please enter the pin")
            return
        transaction_strategy.execute(self, amount)

    def print_receipt(self, amount: int, transaction_type: str) -> None:
        print()
        print("--" * 10 + "Receipt" + "--" * 10)
        print(f"Transaction : {transaction_type}")
        print(f"Amount      : {amount} ₹")
        print(f"Balance     : {self.current_card.account.get_balance()} ₹")
        print(f"Card No     : ****{str(self.current_card.get_card_no())[-4:]}")
        print("--" * 25)
        print()

    def eject_card(self):
        print("Card ejected. Thank you")
        self.is_authenticated = False
        self.current_card = None
