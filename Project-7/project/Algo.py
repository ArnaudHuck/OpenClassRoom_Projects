import numpy as np

from Share import Share, SharePortfolio, MAXIMUM_INVESTMENT
import itertools
import csv
from numpy import array_split


def is_valid_portfolio(share_portfolio: SharePortfolio,
                       investment_amount: float) -> bool:
    is_valid = False

    try:
        if share_portfolio.price() <= investment_amount:
            is_valid = True
    except ValueError:
        pass

    return is_valid


def is_valid_share(share_price: str, share_profit: str) -> bool:
    is_valid = False

    try:
        if float(share_price) > 0 and float(share_profit) > 0:
            is_valid = True
    except ValueError:
        pass

    return is_valid


def get_csv_data(data_csv_path: str) -> list[Share]:
    """Function to get data from a CSV file"""

    # Init
    data = []

    # CSV reader
    with open(data_csv_path, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=',')
        next(data_reader)
        for share_list in data_reader:
            data.append(share_list)

    # Formatting result
    shares = [Share(action_name, float(action_cost), float(action_profit))
              for action_name, action_cost, action_profit in data
              if is_valid_share(action_cost, action_profit)]
    return shares


def get_best_share(shares: list[Share]) -> Share:

    share_performance_list = []

    for share in shares:
        share_performance_list.append(share.calculate_performance())

    best_performance = max(share_performance_list)
    best_performance_index = share_performance_list.index(best_performance)

    return shares[best_performance_index]


def create_optimized_list_of_shares(shares: list[Share]) -> list[Share]:

    new_list_of_shares: list[Share] = []

    while sum(share.price for share in new_list_of_shares) < 500:
        best_share = get_best_share(shares)
        new_list_of_shares.append(best_share)
        shares.pop(shares.index(best_share))

    return new_list_of_shares


def get_all_combinations(shares: list[Share]) -> list[SharePortfolio]:
    combination_list = []

    for n in range(len(shares) + 1):
        combination_list.extend([SharePortfolio(list(i))
                                for i in list(itertools.combinations(shares,
                                                                     n))
                                if is_valid_portfolio
                                 ((SharePortfolio(list(i))),
                                MAXIMUM_INVESTMENT)])

    return combination_list


def split_share_list_into_sub_lists(shares: list[Share]) -> list[Share]:

    array = np.array(shares)

    list_of_list = [x.tolist() for x in np.array_split(array, 10)]

    return list_of_list


def get_all_combinations_from_several_lists_of_share(lists_of_shares:
                                                     list[list[Share]])\
        -> [list[SharePortfolio]]:

    combination_list = []

    for share_list in lists_of_shares:
        combination_list.extend(get_all_combinations(share_list))

    return combination_list

