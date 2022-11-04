from Algo import get_data
from Share import Share

path = "/Users/Henry/Desktop/gitprojects/" \
       "Open_Classroom_projects/Project-7/project/Data_set/"

data_set_1 = "/dataset_1.csv"
data_set_2 = "dataset_2.csv"

shares_dict = get_data(path + data_set_1)
print(Share.calculate_portfolio_profit(shares_dict))

