import Algo
from Share import Share, SharePortfolio
from Algo import get_all_combinations, get_csv_data,\
       create_optimized_list_of_shares, split_share_list_into_sub_lists,\
       get_all_combinations_from_several_lists_of_share


path = "/Users/Henry/Desktop/gitprojects/" \
       "Open_Classroom_projects/Project-7/project/Data_set/"

data_set_1 = "/dataset_1.csv"


shares_list: list[Share] = (get_csv_data(path + data_set_1))
optimized_share_list = Algo.create_optimized_list_of_shares(shares_list)
# print(sorted([share.price for share in optimized_share_list]))
lists_of_shares = Algo.split_share_list_into_sub_lists(optimized_share_list)
print(lists_of_shares)
# for share_list in lists_of_shares:
#    print(len(share_list))
#    print(share_list)
#    print([share.price for share in share_list])
#    print([share.calculate_performance() for share in share_list])
# print(len(optimized_portfolio_list))
# print(len(optimized_portfolio_list))
# print([portfolio.price() for portfolio in optimized_portfolio_list])
# print([portfolio for portfolio in optimized_portfolio_list])
# print(SharePortfolio.get_best_portfolio(optimized_portfolio_list))
# price_list = []
# for share in optimized_share_list:
#    price_list.append(share.price)
# print(sum(price_list))
optimized_portfolio_result = Algo.get_all_combinations_from_several_lists_of_share(lists_of_shares)
print(optimized_portfolio_result)
# print(SharePortfolio.get_best_portfolio(optimized_portfolio_result))
