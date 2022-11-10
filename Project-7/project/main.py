from Algo import get_csv_data, get_all_combinations
from Share import Share, SharePortfolio

path = "/Users/Henry/Desktop/gitprojects/" \
       "Open_Classroom_projects/Project-7/project/Data_set/"


data_set_1 = "/dataset_1.csv"
data_set_2 = "/dataset_2.csv"

shares_list: list[Share] = (get_csv_data(path + data_set_1))
print(shares_list)
"""
main_portfolio = SharePortfolio(shares_list)
print(SharePortfolio.price(main_portfolio))
print(SharePortfolio.benefit(main_portfolio))
print(SharePortfolio.value_post_2years(main_portfolio))
"""

# get_all_combinations(shares_list)
