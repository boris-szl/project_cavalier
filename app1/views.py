
import pandas as pd
import numpy as np

from django.http import HttpResponseRedirect
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

# Create your views here.


# def home(request):

# 	# default is MSFT
# 	# if request.method == 'POST':
# 	# 	print(request.POST.get('ticker_symbol'))
# 	# 	form = TickerSymbol(request.POST)
# 	# 	print(form['ticker_symbol'].value())
# 	# 	print(form.data['ticker_symbol'])
# 	# 	if form.is_valid():
# 	# 		print(form.cleaned_data['ticker_symbol'])
# 	# 		print(form.isinstance.my_field)
# 	# 		form.save()
# 	# 	else:
# 	# 		form = TickerSymbol()

# 	df = pd.DataFrame(company.Company("MSFT").calculateROIC())

# 	allData = []
# 	df = setDateRows1(df)
# 	df = df.reset_index()
# 	df = df.set_axis(["Dates", "Values"], axis=1, inplace=False)
# 	for i in range(df.shape[0]):
# 		allData.append(dict(df.iloc[i]))

# 	context = { "data" : allData}

# 	return render(request, 'index.html', context)

def validate(request):

	allData = []
	ticker = None

	if request.method == 'POST':
		ticker = request.POST["ticker"]
		# context = {
		# 	'username' : username
		# }

		df = pd.DataFrame(company.Company(ticker).calculateROIC())
		df = setDateRows1(df)
		df = df.reset_index()
		df = df.set_axis(["Dates", "Values"], axis=1, inplace=False)
		for i in range(df.shape[0]):
			allData.append(dict(df.iloc[i]))

		context = {"data" : allData}

	return render(request, 'index.html', {"data" : allData, "ticker" : ticker })


# modify function for extension, improvements and testing
def validate2(request):

	company_name = ""
	company_sector = ""
	company_industry = ""
	opening_price = None
	closing_price = None
	price_change = None
	allData = []
	ticker = None

	try:
		if request.method == 'POST':
			ticker = request.POST["ticker"]
			target = company.Company(ticker)
			list_year = list(target.getRevenue().reset_index()["Year"])
			roic = target.calculateROIC()
			nopat_margin = target.calculateNopatMargin()
			capital_turnover = target.calculateCapitalTurnover()
			df_output = pd.DataFrame(data={"Dates": list_year, "ROIC": roic, "NopatMargin" : nopat_margin, "CapitalTurnover" : capital_turnover})

			allData = toDict(df_output)
			context = { "data" : allData}

			company_name = target.getName()
			company_sector = target.getSector()
			company_industry = target.getIndustry()
			opening_price = target.getOpeningPrice()
			closing_price = target.getClosingPrice()
			price_change = np.round(( (closing_price / opening_price ) - 1 ) * 100, 2)

		return render(request, 'test.html',
			{"data" : allData,
			"ticker" : ticker,
			"name" : company_name,
			"sector": company_sector,
			"industry": company_industry,
			"open" : opening_price,
			"close" : closing_price,
			"change" : price_change})

	except KeyError:
		print("Invalid input")

		return render(request, 'error.html')














