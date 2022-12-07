
SHARE_PURCHASE_LIMIT = 1
SHARE_FRACTION_LIMIT = 1
MAXIMUM_INVESTMENT = 500


class Share:

    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit
        self.benefit = (price * profit) / 100

    def __repr__(self):
        return f"name : {self.name}, price : {self.price}," \
               f"  profit : {self.profit}"


class SharePortfolio:

    @staticmethod
    def make(shares: list['Share']) -> 'SharePortfolio':
        benefit = sum([share.benefit for share in shares])
        return SharePortfolio(list_of_shares=shares, benefit=benefit)

    def __init__(self, list_of_shares: list['Share'], benefit: float):
        self.list_of_shares = list_of_shares
        self.benefit = benefit

    def price(self):
        return sum([share.price for share in self.list_of_shares])

    def efficiency(self) -> float:
        return (self.benefit / self.price()) * 100

    def value_post_2years(self) -> float:
        return self.price() + self.benefit

    def append_share(self, share: 'Share'):

        return SharePortfolio(list_of_shares=self.list_of_shares + [share],
                              benefit=self.benefit + share.benefit)

    def __str__(self):
        return f'{self.list_of_shares}'

    @staticmethod
    def pop_best_portfolio(portfolios_list: list['SharePortfolio'])\
            -> 'SharePortfolio':

        portfolio_benefit_list = []

        # TODO: write that in a prettier way

        for portfolio in portfolios_list:
            portfolio_benefit_list.append(portfolio.benefit)

        best_portfolio_profit = max(portfolio_benefit_list)
        best_portfolio_index = \
            portfolio_benefit_list.index(best_portfolio_profit)
        best_portfolio = portfolios_list[best_portfolio_index]
        portfolios_list.pop(best_portfolio_index)

        return best_portfolio

