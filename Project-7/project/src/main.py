from Share import SharePortfolio
from brut_force import brut_force
from greedy import greedy_algorithm
from optimized_dynamic import dynamic_algorithm
from Algo import get_csv_data

path = "/Users/Henry/Desktop/gitprojects/" \
       "Open_Classroom_projects/Project-7/project/src/Data_set/"

data_set_1 = "/dataset_1.csv"
data_set_2 = "/dataset_2.csv"

shares = get_csv_data(path + data_set_1)


def display_portfolio(shareportfolio: SharePortfolio):
    """
    :param shareportfolio: Take a share portfolio
    :return: The main values of the share portfolio
    """

    for share in shareportfolio.list_of_shares:
        print(share, '\n')
    print('Total cost is: ' + f'{round(shareportfolio.price(), 2)}' + '$')
    print('Total profit is: ' + f'{round(shareportfolio.benefit, 2)}' + '$')
    print('Global portfolio efficiency : ' +
          f'{round(shareportfolio.efficiency(), 2)}')
    print('SharePortfolio value after 2 years is: ' +
          f'{round(shareportfolio.value_post_2years(), 2)}' + '$')


if __name__ == '__main__':
    choice = input('Which algorithm do you want to run ? ')
    if choice.capitalize() == 'Brut':
        display_portfolio(brut_force())
    elif choice.capitalize() == 'Greedy':
        display_portfolio(greedy_algorithm(shares))
    elif choice.capitalize() == 'Dynamic':
        display_portfolio(dynamic_algorithm(shares))
    else:
        print('You need to choose between Brut, Greedy or Optimized')
