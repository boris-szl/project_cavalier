
import pandas as pd
import numpy as np
from numerize import numerize as num
import json

from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from .forms import TickerSymbol


# own modules
from app1.modules import company, findata

def renameCols(df):
	col_list = list(df.columns)
	df2 = df.set_axis([x.strftime("%m/%d/%Y") for x in col_list], axis=1, inplace=False)
	return df2

def setDateRows1(df):
	row_list = list(df.index)
	df2 = df.set_axis([x.strftime("%m/%d/%Y") for x in row_list], axis=0, inplace=False)
	return df2

def to_dict(df):
	data = []
	df = setDateRows1(df)
	df = df.reset_index()
	df = df.set_axis(["Dates", "in %"], axis=1, inplace=False)
	dict_data = []
	for i in range(df.shape[0]):
		dict_data.append(dict(df.iloc[i]))
	return dict_data


def toDict(df):
    dict_data = []
    for i in range(df.shape[0]):
        dict_data.append(dict(df.iloc[i]))
    return dict_data

def getRoicTable(target):
	list_year = list(target.getRevenue().reset_index()["Year"])
	roic = target.calculateRoicByMultiplication() * 100
	nopat_margin = target.calculateNopatMargin() * 100
	capital_turnover = target.calculateCapitalTurnover()
	return pd.DataFrame(data={"Dates": list_year, "ROIC": roic, "NopatMargin" : nopat_margin, "CapitalTurnover" : capital_turnover})

def toListDict(df):
	dict_data = []
	for i in range(df.shape[0]):
		dict_data.append(dict(df.iloc[i]))
	return dict_data

# Create your views here.

def ajax_view(request):
    ticker = "V"
    target = company.Company(ticker)
    result = getRoicTable(target).to_json(orient="records")
    test_data = {
    	"msg" : "it worked!"
    }
    return JsonResponse(json.loads(result), safe=False)

def defaultDataDisplayIndex(request):
	# default "MSFT"
	ticker = "MSFT"
	target = company.Company(ticker)

	company_name = target.getName()
	company_sector = target.getSector()
	company_industry = target.getIndustry()
	company_info = target.getBusinessDescription()
	opening_price = target.getOpeningPrice()
	closing_price = target.getClosingPrice()
	price_change = np.round(( (closing_price / opening_price ) - 1 ) * 100, 2)
	market_price = target.getMarketPrice()
	market_cap = num.numerize(target.getMarketCap(), 2)
	country = target.getCountry()

	df = getRoicTable(target)
	allData = toListDict(df)

	if request.method == "POST":
		getRoicDataIndex()

	return render(request, 'index.html', {"data" : allData, "ticker" : ticker })

# modify function for extension, improvements and testing
def getRoicDataIndex(request):

	company_name = ""
	company_sector = ""
	company_industry = ""
	opening_price = 0
	closing_price = 0
	price_change = 0
	allData = []
	ticker = ""
	company_info = ""
	market_cap = 0
	market_price = 0
	country = ""

	try:
		if request.method == 'POST':
			ticker = request.POST["ticker"]
			target = company.Company(ticker)
			list_year = list(target.getRevenue().reset_index()["Year"])
			roic = target.calculateRoicByMultiplication() * 100
			nopat_margin = target.calculateNopatMargin() * 100
			capital_turnover = target.calculateCapitalTurnover()
			df_output = pd.DataFrame(data={"Dates": list_year, "ROIC": roic, "NopatMargin" : nopat_margin, "CapitalTurnover" : capital_turnover})

			allData = toDict(df_output)
			context = { "data" : allData}

			company_name = target.getName()
			company_sector = target.getSector()
			company_industry = target.getIndustry()
			company_info = target.getBusinessDescription()
			opening_price = target.getOpeningPrice()
			closing_price = target.getClosingPrice()
			price_change = np.round(( (closing_price / opening_price ) - 1 ) * 100, 2)
			market_price = target.getMarketPrice()
			market_cap = num.numerize(target.getMarketCap(), 2)
			country = target.getCountry()

		return render(request, 'index.html',
			{"data" : allData,
			"ticker" : ticker,
			"name" : company_name,
			"sector": company_sector,
			"industry": company_industry,
			"open" : opening_price,
			"close" : closing_price,
			"change" : price_change,
			"info" : company_info,
			"market_price" : market_price,
			"market_cap": market_cap,
			"country" : country,
			})

	except KeyError:
		print("Invalid input")

		return render(request, 'error.html')

def defaultDataDisplayDemo(request):
	# default "MSFT"
	ticker = "MSFT"
	target = company.Company(ticker)

	company_name = target.getName()
	company_sector = target.getSector()
	company_industry = target.getIndustry()
	company_info = target.getBusinessDescription()
	opening_price = target.getOpeningPrice()
	closing_price = target.getClosingPrice()
	price_change = np.round(( (closing_price / opening_price ) - 1 ) * 100, 2)
	market_price = target.getMarketPrice()
	market_cap = num.numerize(target.getMarketCap(), 2)
	country = target.getCountry()

	df = getRoicTable(target)
	allData = toListDict(df)

	if request.method == "POST":
		getRoicDataDemo()
	else:
		return render(request, 'test.html',
		{"data" : allData,
		"ticker" : ticker,
		"name" : company_name,
		"sector": company_sector,
		"industry": company_industry,
		"open" : opening_price,
		"close" : closing_price,
		"change" : price_change,
		"info" : company_info,
		"market_price" : market_price,
		"market_cap": market_cap,
		"country" : country,
		})


def getRoicDataDemo(request):

	company_name = ""
	company_sector = ""
	company_industry = ""
	opening_price = 0
	closing_price = 0
	price_change = 0
	allData = []
	ticker = ""
	company_info = ""
	market_cap = 0
	market_price = 0
	country = ""

	try:
		if request.method == 'POST':
			ticker = request.POST["ticker"]
			target = company.Company(ticker)
			list_year = list(target.getRevenue().reset_index()["Year"])
			roic = target.calculateRoicByMultiplication() * 100
			nopat_margin = target.calculateNopatMargin() * 100
			capital_turnover = target.calculateCapitalTurnover()
			df_output = pd.DataFrame(data={"Dates": list_year, "ROIC": roic, "NopatMargin" : nopat_margin, "CapitalTurnover" : capital_turnover})

			allData = toDict(df_output)
			context = {"data" : allData}

			company_name = target.getName()
			company_sector = target.getSector()
			company_industry = target.getIndustry()
			company_info = target.getBusinessDescription()
			opening_price = target.getOpeningPrice()
			closing_price = target.getClosingPrice()
			price_change = np.round(( (closing_price / opening_price ) - 1 ) * 100, 2)
			market_price = target.getMarketPrice()
			market_cap = num.numerize(target.getMarketCap(), 2)
			country = target.getCountry()

		return render(request, 'test.html',
			{"data" : allData,
			"ticker" : ticker,
			"name" : company_name,
			"sector": company_sector,
			"industry": company_industry,
			"open" : opening_price,
			"close" : closing_price,
			"change" : price_change,
			"info" : company_info,
			"market_price" : market_price,
			"market_cap": market_cap,
			"country" : country,
			})

	except KeyError:
		print("Invalid input")

		return render(request, 'error.html')

def json_test(request):
	ticker = "V"
	target = company.Company(ticker)
	df  = getRoicTable(target)
	json_data = df.to_json()
	return render(request, "ajax.html", {"df" : json_data})


# def json_tes_two (request):
# 	ticker = "V"
# 	target = company.Company(ticker)
# 	df  = getRoicTable(target)
# 	json_data = df.to_json(orient='records')
# 	return render('ajax.html', {'df' : json_data})
