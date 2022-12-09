from Share import Share, SharePortfolio
from Algo import sort_list_of_shares
from time import time
import tracemalloc
from Share import MAXIMUM_INVESTMENT


def greedy_algorithm(shares: list[Share]) -> SharePortfolio:
    """
    :param shares: Take a list of shares
    :return: A share portfolio filled with the best shares of the list
             previously sorted. We had shares until the maximum investment
             amount is reached
    """
    share_portfolio = SharePortfolio(list_of_shares=[], benefit=0)
    sorted_shares = sort_list_of_shares(shares)
    portfolio_cost = 0
    start_time = time()
    tracemalloc.start()
    while portfolio_cost < MAXIMUM_INVESTMENT:
        try:
            next_share = sorted_shares.pop()
            new_portfolio_cost = portfolio_cost + next_share.price
            if new_portfolio_cost > MAXIMUM_INVESTMENT:
                break
            else:
                portfolio_cost = new_portfolio_cost
                share_portfolio = share_portfolio.append_share(next_share)
        except:
            pass
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print('Memory use : ' + f'{current / 10 ** 6} MB, {peak / 10 ** 6} MB ')
    print('Run time in seconds: '), print(round(time() - start_time, 3))
    return share_portfolio
