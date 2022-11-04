from Share import Share
import csv


def get_data(file_name: str) -> list[Share]:

    data = []

    with open(file_name, "r", newline='') as f:
        dict_reader = csv.DictReader(f)
        for row_list in dict_reader:
            data.append(row_list)

        for share_dict in data:
            float_price = float(share_dict['price'])
            float_profit = float(share_dict['profit'])

    list_of_shares = [Share(name, float_price, float_profit)
                      for name, price, profit in data]

    return list_of_shares
