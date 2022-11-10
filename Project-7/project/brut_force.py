from Share import Share, SharePortfolio
from Algo import get_all_combinations

share_table: list[Share] = [Share("Share-1", 20, 5),
                            Share("Share-2", 30, 10),
                            Share("Share-3", 50, 15),
                            Share("Share-4", 70, 20),
                            Share("Share-5", 60, 17),
                            Share("Share-6", 80, 25),
                            Share("Share-7", 22, 7),
                            Share("Share-8", 26, 11),
                            Share("Share-9", 48, 13),
                            Share("Share-10", 34, 27),
                            Share("Share-11", 42, 17),
                            Share("Share-12", 110, 9),
                            Share("Share-13", 38, 23),
                            Share("Share-14", 14, 1),
                            Share("Share-15", 18, 3),
                            Share("Share-16", 8, 8),
                            Share("Share-17", 4,12),
                            Share("Share-18", 10, 14),
                            Share("Share-19", 24, 21),
                            Share("Share-20", 114, 18)]


portfolio_list = (get_all_combinations(share_table))
print(len(portfolio_list))
# print(SharePortfolio.get_best_portfolio(portfolio_list).benefit())

