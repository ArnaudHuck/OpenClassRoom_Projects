from Share import Share, SharePortfolio, MAXIMUM_INVESTMENT
import itertools
import csv



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


def pop_best_share(shares: list[Share]) -> Share:

    share_benefit = [share.benefit for share in shares]
    best_benefit = max(share_benefit)
    best_benefit_index = share_benefit.index(best_benefit)
    for share in shares:
        if share.benefit == best_benefit:
            best_share = shares[best_benefit_index]
            shares.pop(best_benefit_index)

            return best_share


def create_optimized_list_of_shares(shares: list[Share]) -> list[Share]:

    new_list_of_shares: list[Share] = []

    while sum(share.price for share in new_list_of_shares) < MAXIMUM_INVESTMENT:
        best_share = pop_best_share(shares)
        new_list_of_shares.append(best_share)

    return new_list_of_shares


def get_all_combinations(shares: list[Share]) -> list[SharePortfolio]:
    combination_list = []

    for n in range(len(shares) + 1):
        combination_list.extend([SharePortfolio(list(i), sum(share.benefit for
                                                             share in i))
                                for i in list(itertools.combinations(shares,
                                                                     n))
                                if is_valid_portfolio
                                 ((SharePortfolio(list(i), sum(share.benefit for
                                                               share in i))),
                                MAXIMUM_INVESTMENT)])

    return combination_list


def sort_list_of_shares(shares):
    benefit_list = [share.benefit for share in shares]

    sorted_list = []

    new_dict = {shares[i]: benefit_list[i] for i in range(len(benefit_list))}

    s = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1],
                                 reverse=False)}

    for i in s.keys():
        sorted_list.append(i)

    return sorted_list
