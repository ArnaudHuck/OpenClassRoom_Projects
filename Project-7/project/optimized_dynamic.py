from Share import Share, SharePortfolio, MAXIMUM_INVESTMENT
from math import ceil
from time import time
import tracemalloc

path = "/Users/Henry/Desktop/gitprojects/" \
       "Open_Classroom_projects/Project-7/project/Data_set/"

data_set_1 = "/dataset_1.csv"
data_set_2 = "/dataset_2.csv"


def dynamic_algorithm(shares: list[Share],
                      c: int = MAXIMUM_INVESTMENT) \
        -> SharePortfolio:

    start_time = time()
    tracemalloc.start()

    n = len(shares)
    factor = 10
    max_cost = c * factor
    print("starting with n ", n, "and cost ", max_cost)
    empty_portfolio = SharePortfolio(list_of_shares=[], benefit=0)

    table = [[empty_portfolio for _ in range(max_cost + 1)] for _
             in
             range(n + 1)]

    for i in range(1, n + 1):

        share = shares[i - 1]
        share_price = ceil(share.price * factor)

        for j in range(max_cost + 1):
            if share_price > j:
                table[i][j] = table[i - 1][j]
            else:
                dont_buy = table[i - 1][j]
                buy = table[i - 1][j - share_price]

                if share.benefit + buy.benefit > dont_buy.benefit:
                    table[i][j] = buy.append_share(share)
                else:
                    table[i][j] = dont_buy

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print('Memory use : ' + f'{current / 10 ** 6} MB, {peak / 10 ** 6} MB ')
    print('Run time in seconds: '), print(round(time() - start_time, 3))
    return table[n][max_cost]


