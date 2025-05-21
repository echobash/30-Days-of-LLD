from account import Account
from card import Card
from atm import Atm


class Atm_demo:
    account = Account("DK23239DI")
    card = Card(39823423, 8383, account)
    atm = Atm()
    atm.insert_card(card)
    atm.validate_pin(8383)
    atm.show_remaining_balance()
    atm.deposit_money(2000)
    atm.show_remaining_balance()
    atm.withdraw_money(1000)
    atm.show_remaining_balance()
    atm.withdraw_money(1000)
    atm.show_remaining_balance()
    atm.withdraw_money(1000)
    atm.show_remaining_balance()
    atm.eject_card()
