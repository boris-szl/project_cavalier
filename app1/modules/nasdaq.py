import numpy as np
import pandas as pd

nasdaq_data  = pd.read_csv("nasdaq_list.csv")
symbol_list = np.array(nasdaq_data["Symbol"])
company_names = np.array(nasdaq_data["Name"])