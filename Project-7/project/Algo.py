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


def get_all_combinations(shares: list[Share]):
    combination_list = []

    investment = float(input("input the amount of money you wish to invest, "
                             "cannot exceed 500$ : "))

    if investment > MAXIMUM_INVESTMENT:
        print("Investment value is too high")
        return get_all_combinations(shares)
    elif investment < 0:
        print("Investment must be a positive number ")
        return get_all_combinations(shares)
    else:
        for n in range(len(shares) + 1):
            combination_list.extend([SharePortfolio(list(i))
                                    for i in list(itertools.combinations(shares,
                                                                         n))
                                    if is_valid_portfolio
                                     ((SharePortfolio(list(i))),
                                    investment)])

    return combination_list
