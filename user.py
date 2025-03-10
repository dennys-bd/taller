from dataclasses import dataclass
from typing import Self

from exceptions import CantHaveNegativeValueError


@dataclass
class User:
    _balance: float
    name: str
    credit_card: str

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value < 0:
            raise CantHaveNegativeValueError()
        self._balance = value

    def pay(self, value: float, user: Self) -> None:
        try:
            user.balance += value
            self.balance -= value
        except CantHaveNegativeValueError:
            print("Credit card charge issued.")
