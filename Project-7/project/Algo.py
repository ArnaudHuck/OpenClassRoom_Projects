from Share import Share, SharePortfolio, MAXIMUM_INVESTMENT
import itertools
import csv


def is_valid_portfolio(share_portfolio: SharePortfolio,
                       investment_amount: float) -> bool:
    """
    :param share_portfolio: Take a share portfolio previously created
    :param investment_amount: Take an investment amount that will be a limit
    :return: A bool that validates or not if the share portfolio must be
             taken into account
    """
    is_valid = False

    try:
        if share_portfolio.price() <= investment_amount:
            is_valid = True
    except ValueError:
        pass

    return is_valid


def is_valid_share(share_price: str, share_profit: str) -> bool:
    """
    :param share_price: Take the share price of a share
    :param share_profit: Take the share profit of a share
    :return: A bool that validates if the share must be taken into account
    """
    is_valid = False

    try:
        if float(share_price) > 0 and float(share_profit) > 0:
            is_valid = True
    except ValueError:
        pass

    return is_valid


def get_csv_data(data_csv_path: str) -> list[Share]:
    """
    :param data_csv_path: Take a csv file holding the data set
    :return: A list of shares that are valid
    """

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


def get_all_combinations(shares: list[Share]) -> list[SharePortfolio]:
    """
    :param shares: Take a list of shares
    :return: A list of all the valid share portfolio that can be created by
             combination
    """
    combination_list = []

    for n in range(len(shares) + 1):
        combination_list.extend([SharePortfolio(list(i), sum(share.benefit for
                                                             share in i))
                                for i in list(itertools.combinations(shares,
                                                                     n))
                                if is_valid_portfolio
                                 ((SharePortfolio(list(i),
                                                  sum(share.benefit for
                                                      share in i))),
                                MAXIMUM_INVESTMENT)])

    return combination_list


def sort_list_of_shares(shares: list[Share]):
    """
    :param shares: Take a list of shares
    :return: The list of shares sorted by profit in absolute value
    """
    benefit_list = [share.benefit for share in shares]

    sorted_list = []

    new_dict = {shares[i]: benefit_list[i] for i in range(len(benefit_list))}

    s = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1],
                                 reverse=False)}

    for i in s.keys():
        sorted_list.append(i)

    return sorted_list
