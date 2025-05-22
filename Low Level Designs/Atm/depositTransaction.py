from transactionStrategy import TransactionStrategy


class DepositTransaction(TransactionStrategy):
    def execute(self, atm, amount=None):
        if not amount:
            print("Amount required for Deposit")
            return False
        result = atm.current_card.account.deposit(amount)
        print("Transaction Successful")
        atm.print_receipt(amount, "Deposit")
        return result
