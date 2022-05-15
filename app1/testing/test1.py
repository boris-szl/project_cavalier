import pandas as pd
import numpy as np
import yfinance as yf
import re
import datetime as dt
import os, sys
import requests
import json


# from company import Company
sys.path.insert(0, '..')
from modules import findata as fd
from modules import company
from modules import manipulate

def inputTicker():
	while True:
		x = input("Please enter a NASDAQ symbol.\n")
		if len(x) > 5:
			print("Invalid input. Please try again.")
			continue
		else:
			break
	return x.upper()

def to_dict(df):
    data = []
    df = setDateRows1(df)
    df = df.reset_index()
    df = df.set_axis(["Dates", "ROIC"], axis=1, inplace=False)
    dict_data = []
    for i in range(df.shape[0]):
        dict_data.append(dict(df.iloc[i]))
    return df

def toDict(df):
    dict_data = []
    for i in range(df.shape[0]):
        dict_data.append(dict(df.iloc[i]))
    return dict_data

def main():
	# x = inputTicker()
	# print(x)
	# company = cd.Company(x)
	# yearly_roic = company.calculateROIC()
	# quarterly_roic = company.QuarterlyROIC()

	# wacc = fd.calculateWacc() * 100

	# print(yearly_roic)
	# print(quarterly_roic)
	# # inaccuarate because it takes the current wacc
	# print(pd.Series([fd.calculateWacc(year=dt.date.today().year-x) for x in [0,1,2,3]]))
	# print(yearly_roic - wacc)

	# cleaning the mess up in findata modules
	# date = dt.datetime.now().year
	# print(str(date))
	# URL = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_long_term_rate&field_tdr_date_value="
	# print(URL + str(date))
	# URL2 = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_long_term_rate&field_tdr_date_value=" + str(date)
	# print(URL2)
	# print(fd.getRiskFreeRateMonth())
	# print(fd.getRiskFreeRateUs())
	# print(fd.getCurrentRiskFreeRateUs())
	# print(type(fd.getCurrentRiskFreeRateUs()))
	# print(fd.getRawBetaData())
	# print(fd.getRawBetaData().columns)
	# print(fd.getCleanedBetaData().columns)
	# print(fd.getUnleveredBeta())
	# print(fd.getUnleveredBeta().iloc[[1]])
	# print(fd.getUnleveredCleanedBeta())
	# print(fd.getRiskFreeRateForAustria())
	# print(fd.getRiskFreeRateEuroArea("DE", "EUR"))
	# print(fd.getRiskFreeRateEuroArea("AT", "EUR"))

	target = company.Company("MSFT")
	print(target)
	print(target.getNopat())
	# print(target.getInvestedCapital())
	# print(target.getNetWorkingCapital())
	print(target.getEarnings())
	print("-----------------------------")
	print("Nopat:")
	print(target.getNopat())
	print("-----------------------------")
	print("Revenue:")
	print(target.getRevenue())
	print("-----------------------------")
	print("Nopat marigin:")
	print(target.calculateNopatMargin())
	print("-----------------------------")
	print(target.calculateCapitalTurnover())
	print("-----------------------------")
	print(target.calculateRoicByMultiplication())
	print("-----------------------------")
	roic = target.calculateROIC()
	print(type(roic))
	print(target.getRevenue().reset_index()["Year"])
	list_year = list(target.getRevenue().reset_index()["Year"])
	print(pd.DataFrame(data=roic, dtype=np.float32))
	print(pd.DataFrame(roic, columns=["ROIC"]))
	print(pd.DataFrame(list_year, columns=["Dates"]))


	df_output = pd.DataFrame(data={"Dates": list_year, "ROIC": roic, "Nopat Margin" : target.calculateNopatMargin(), "Capital Turnover" : target.calculateCapitalTurnover()})
	print(df_output)
	print(toDict(df_output))

if __name__ == "__main__":
	main()

