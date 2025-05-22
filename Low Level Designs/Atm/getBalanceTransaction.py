from transactionStrategy import TransactionStrategy


class GetBalanceTransaction(TransactionStrategy):
    def execute(self, atm, amount=None):
        balance = atm.current_card.account.get_balance()
        print("Transaction Successful")
        print(f"Your current balance is: {balance} ₹")
        return balance
