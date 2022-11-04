from typing import TYPE_CHECKING


SHARE_PURCHASE_LIMIT = 1
SHARE_FRACTION_LIMIT = 1
MAXIMUM_INVESTMENT = 500


class Share:

    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit

    def calculate_profit(self) -> float:
        return (self.price * self.profit) / 100

    @staticmethod
    def calculate_portfolio_profit(shares: list['Share']) -> list[float]:
        profit_list = []

        for share in shares:
            profit_list.append(share.calculate_profit())

        return profit_list

    def __str__(self):
        return self.name, self.price, self.profit
