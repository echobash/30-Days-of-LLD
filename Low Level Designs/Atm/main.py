from account import Account
from card import Card
from atm import Atm
from withdrawTransaction import WithdrawTransaction
from depositTransaction import DepositTransaction
from getBalanceTransaction import GetBalanceTransaction


account = Account("DK23239DI")
card = Card(39823423, 8383, account)
atm = Atm()
atm.insert_card(card)
atm.validate_pin(8383)
atm.execute_transaction(GetBalanceTransaction())
atm.execute_transaction(DepositTransaction(), 2000)
atm.execute_transaction(GetBalanceTransaction())
atm.execute_transaction(WithdrawTransaction(),1000)
atm.execute_transaction(GetBalanceTransaction())
atm.execute_transaction(DepositTransaction(), 2000)
atm.execute_transaction(GetBalanceTransaction())
atm.execute_transaction(DepositTransaction(), 2000)
atm.execute_transaction(GetBalanceTransaction())
atm.execute_transaction(WithdrawTransaction(),1000)
atm.execute_transaction(WithdrawTransaction(),1000)
atm.execute_transaction(WithdrawTransaction(),1000)
atm.execute_transaction(WithdrawTransaction(),1000)
atm.execute_transaction(WithdrawTransaction(),1000)
atm.execute_transaction(WithdrawTransaction(),1000)
atm.eject_card()
