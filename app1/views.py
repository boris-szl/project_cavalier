
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

		context = { "data" : allData}

	return render(request, 'index.html', {"data" : allData, "ticker" : ticker })


def validate2(request):

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

		context = { "data" : allData}

	return render(request, 'test.html', {"data" : allData, "ticker" : ticker })
















