import pandas as pd
import numpy as np
import yfinance as yf
import re
import datetime as dt
import os, sys


# from company import Company
import findata as fd
from company_test import Company
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))


def inputTicker():
	while True:
		x = input("Please enter a NASDAQ symbol.\n")
		if len(x) > 5:
			print("Invalid input. Please try again.")
			continue
		else:
			break
	return x.upper()

def main():

	x = inputTicker()
	print(x)
	company = Company(x)
	yearly_roic = company.calculateROIC()
	quarterly_roic = company.QuarterlyROIC()

	wacc = fd.calculateWacc() * 100

	print(yearly_roic)
	print(quarterly_roic)

	# inaccuarate because it takes the current wacc
	print(pd.Series([fd.calculateWacc(year=dt.date.today().year-x) for x in [0,1,2,3]]))


	# print(yearly_roic - wacc)



if __name__ == "__main__":
	main()
