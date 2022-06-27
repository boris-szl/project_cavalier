import numpy as np
import pandas as pd
import sys, os

sys.path.insert(0, '..')

# problem with this is, that it is not updated
nasdaq_data  = pd.read_csv("../data/nasdaq_list.csv")
symbol_list = np.array(nasdaq_data["Symbol"])
company_names = np.array(nasdaq_data["Name"])


# get nasdaq listed company symbols and names with
# scrapy, bs4, pandas

# json parser
# return data in json for front end
