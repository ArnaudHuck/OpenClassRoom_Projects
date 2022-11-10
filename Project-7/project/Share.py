
SHARE_PURCHASE_LIMIT = 1
SHARE_FRACTION_LIMIT = 1
MAXIMUM_INVESTMENT = 500


class Share:

    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit

    def calculate_benefit(self) -> float:
        return (self.price * self.profit) / 100

    def calculate_performance(self) -> float:
        return self.profit / self.price

    def __repr__(self):
        return f"name : {self.name}, price : {self.price}," \
               f"  profit : {self.profit}"


class SharePortfolio:

    def __init__(self, list_of_shares: list['Share']):
        self.list_of_shares = list_of_shares

    def price(self) -> float:
        return sum([share.price for share in self.list_of_shares])

    def benefit(self) -> float:
        return sum([(share.price * share.profit) / 100
                    for share in self.list_of_shares])

    def value_post_2years(self) -> float:
        return self.price() + self.benefit()

    @staticmethod
    def get_best_portfolio(portfolio_list: list['SharePortfolio'])\
            -> 'SharePortfolio':

        portfolio_benefit_list = []

        investment = float(input("input the amount of money you wish to invest,"
                                 "cannot exceed 500$ : "))

        if investment > MAXIMUM_INVESTMENT:
            print("Investment value is too high")
            return SharePortfolio.get_best_portfolio(portfolio_list)
        elif investment < 0:
            print("Investment must be a positive number ")
            return SharePortfolio.get_best_portfolio(portfolio_list)
        else:

            for portfolio in portfolio_list:
                portfolio_benefit_list.append(portfolio.benefit())

            best_portfolio = max(portfolio_benefit_list)
            best_portfolio_index = portfolio_benefit_list.index(best_portfolio)

        return portfolio_list[best_portfolio_index]

