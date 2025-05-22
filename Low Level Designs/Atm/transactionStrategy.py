from abc import ABC, abstractmethod


class TransactionStrategy(ABC):
    @abstractmethod
    def execute(self, atm, amount=None):
        pass
