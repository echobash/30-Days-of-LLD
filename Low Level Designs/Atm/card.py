class Card:
    def __init__(self, card_no, pin, account):
        self.card_no = card_no
        self._pin = pin  # pin is private for security
        self.account = account

    def get_card_no(self):
        return self.card_no

    def validate_pin(self, input_pin):
        return input_pin == self._pin

    def set_card_pin(self, new_pin):
        self._pin = new_pin
