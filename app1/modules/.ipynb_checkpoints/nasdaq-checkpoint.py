import numpy as np
import pandas as pd
import sys, os

sys.path.insert(0, '..')

nasdaq_data  = pd.read_csv("../data/nasdaq_list.csv")
symbol_list = np.array(nasdaq_data["Symbol"])
company_names = np.array(nasdaq_data["Name"])
