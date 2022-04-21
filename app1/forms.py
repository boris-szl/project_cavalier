from django import forms

class TickerSymbol(forms.Form):
	ticker_symbol = forms.CharField(label = "Ticker symbol", max_length=100)