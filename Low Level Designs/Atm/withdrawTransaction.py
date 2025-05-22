from transactionStrategy import TransactionStrategy


class WithdrawTransaction(TransactionStrategy):
    def execute(self, atm, amount=None):
        if not amount:
            print("Amount required for Withdrawal")
            return False
        if atm.current_card.account.withdraw(amount):
            print("Transaction Successful")
            atm.print_receipt(amount, "Withdrawal")
            return True
        print("Insufficient Balance")
        return False