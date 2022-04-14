import yfinance as yf
import pandas as pd
import numpy as np

class Company:
    def __init__(self, ticker_symbol):
        self.ticker = yf.Ticker(ticker_symbol)
        
        self.info = self.ticker.info

        # Company related information
        self.name = self.info['shortName']
        self.country = self.info['country']
        self.sector = self.info['sector']
        self.industry = self.info['industry']
        self.business_description = self.info['longBusinessSummary']
        
        self.actions = self.ticker.actions
        # self.news = self.ticker.news
        # Show next event (earnings, etc)
        self.event = self.ticker.calendar
        
        # Dividend and share price policy
        self.dividends = self.ticker.dividends
        self.splits = self.ticker.splits
        
        # Ownership
        self.major_holders = self.ticker.major_holders
        self.institutional_holders = self.ticker.institutional_holders
        
        # Stock price related information
        self.history = self.ticker.history
        self.fifty_two_week_high = self.info['fiftyTwoWeekHigh']
        self.fifty_two_week_low = self.info['fiftyTwoWeekLow']
        self.pre_market = self.info['preMarketPrice']
        self.price = self.info['regularMarketPrice']
        self.open = self.info['regularMarketOpen']
        self.close = self.info['regularMarketPreviousClose']
        self.market_cap = self.info['marketCap']
        
        # financials metrics
        
        # Currency
        self.currency = self.info['currency']
        
        # Financials Statements
        # Annual
        self.income_statement = self.ticker.financials
        self.balance_sheet = self.ticker.balance_sheet
        self.cash_flow = self.ticker.cashflow
        self.earnings = self.ticker.earnings
        # Quarter
        self.quarterly_is = self.ticker.quarterly_financials
        self.quarterly_bs = self.ticker.quarterly_balance_sheet
        self.quarterly_cf = self.ticker.quarterly_cashflow
        self.ltm_earnings = self.ticker.quarterly_earnings
        
        # Informations on options and derivaties
        self.option_chain = self.ticker.option_chain
        self.options_expiration = self.ticker.options
        
        # Sustainability
        self.esg = self.ticker.sustainability

        # Analysts recommendations
        self.analyst = self.ticker.recommendations
    
    def getName(self):
        return self.name

    def getSector(self):
        return self.sector

    def getIndustry(self):
        return self.industry

    def getOpeningPrice(self):
        return self.open

    def getClosingPrice(self):
        return self.close

    def getBusinessDescription(self):
        return self.business_description

    # income statement methods
    def getIncomeStatement(self):
        return self.income_statement
    
    def getOperatingIncome(self):
        return self.income_statement.loc["Operating Income"]
    
    def getEbit(self):
        return self.income_statement.loc["Ebit"]
    
    def getIncomeTaxes(self):
        return self.income_statement.loc['Income Tax Expense']
    
    # Balance Sheet Methods
    def getBalanceSheet(self):
        return self.balance_sheet
    
    def getCurrentAssets(self):
        item_name = ["Current Assets", "Total Current Assets", "current assets", "total current assets"]
        for item in item_name:
            for i, row in self.balance_sheet.iterrows():
                if i == item:
                    return self.balance_sheet.loc[i]
                else:
                    pass
                
    def getCurrentLiabilities(self):
        item_name = ["Current Liabilities", "Total Current Liabilities"]
        for item in item_name:
            for i, row in self.balance_sheet.iterrows():
                if i == item:
                    return self.balance_sheet.loc[i]
                else:
                    pass
                
    def getOtherCurrentLiabilities(self):
        item_name = ["Other current liabilities", "Total other current liabilities", "Other Current Liabilities"]
        for item in item_name:
            for i, row in self.balance_sheet.iterrows():
                if i == item:
                    return self.balance_sheet.loc[i]
                else:
                    pass
                
    def getShortTermDebt(self):
        item_name = ["Short Term Debt"]
        for item in item_name:
            for i, row in self.balance_sheet.iterrows():
                if i == item:
                    return self.balance_sheet.loc[i]
                else:
                    pass
                
    def getPPE(self):
        item_name = ["Property Plant Equipment"]
        for item in item_name:
            for i, row in self.balance_sheet.iterrows():
                if i == item:
                    return self.balance_sheet.loc[i]
                else:
                    return np.double()
                
    def getGoodwill(self):
        item_name = ["Goodwill", "Good Will"]
        for item in item_name:
            for i, row in self.balance_sheet.iterrows():
                if i == item:
                    return self.balance_sheet.loc[i]
                else:
                    return np.double()
                
    def getGoodwill2(self):
        for i, row in self.balance_sheet.iterrows():
            if i=="Goodwill":
                return self.balance_sheet.loc["Goodwill"]
            else:
                pass
        return 0
    
    # Cashflow Methods
    def getCashFlow(self):
        return self.cash_flow
    
    def getDepreciation(self):
        item_name = ["Depreciation", "Depreciation & Amortization", "D&A"]
        for item in item_name:
            for i, row in self.cash_flow.iterrows():
                if i == item:
                    return self.cash_flow.loc[i]
                else:
                    pass
                
    def getCapex(self):
        item_name = ["CAPEX", "Capex", "Capital Expenditures"]
        for item in item_name:
            for i, row in self.cash_flow.iterrows():
                if i == item:
                    return self.cash_flow.loc[i]
                else:
                    pass
    
    def getEarnings(self):
        return self.earnings
    
    def getQuarterlyIncomeStatement(self):
        return self.quarterly_is
    
    def getQuarterlyBalanceSheet(self):
        return self.quarterly_bs
    
    def getQuarterlyCashFlow(self):
        return self.quarterly_cf
    
    def getQuarterlyEarnings(self):
        return self.quarterly_earnings
    
    # create child
    def getHistory(self,timeframe='1mo'):
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # (optional, default is '1mo')
        return self.history(period=timeframe)
    
    # create child
    def getOptionChain(self,timeframe=None):
        # timeframe='YYYY-MM-DD'
        return self.option_chain()[0]
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def calculateROIC(self):
        #INCOME STATEMENT
         # for operating income
        operating_income = self.getOperatingIncome()
         # for ebit
        ebit = self.getEbit()
         # for income taxes
        income_taxes = self.getIncomeTaxes()

        
        # BALANCE SHEET
        current_assets = self.getCurrentAssets()
         # for NIBCL
        # total current liabilities
        current_liabilities = self.getCurrentLiabilities()
        # other current liabilities 
        other_current_liabilities = self.getOtherCurrentLiabilities()
        # short term debt
        short_term_debt = self.getShortTermDebt()
         # for NPP&E
        ppe = self.getPPE()
         # for Goodwill
        goodwill = self.getGoodwill()
        
        # calculate NWC
        net_work_cap = current_assets - current_liabilities

        # CASH FLOW
         # for depreciation
        depreciation = self.getDepreciation()
        # for capex
        capex = self.getCapex()

        nopat = ebit + depreciation - income_taxes
        invested_capital = net_work_cap + ppe + goodwill

        roic = ( nopat / invested_capital ) * 100
        return roic
    
    def QuarterlyROIC(self):
        return 0
