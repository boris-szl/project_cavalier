import yfinance as yf

class Company:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

        self.info = self.ticker.info

        # Company related information
        self.name = self.info['shortName']
        self.country = self.info['country']
        self.sector = self.info['sector']
        self.industry = self.info['industry']
        self.business_description = self.info['longBusinessSummary']

        self.actions = self.ticker.actions
        self.news = self.ticker.news
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
        self.prev_close = self.info['regularMarketPreviousClose']
        self.market_cap = self.info['marketCap']
        
        # financials metrics
        
        
        # Financials related information
        # Currency
        self.currency = self.info['currency']
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
        
    def getIncomeStatement(self):
        return self.income_statement
    
    def getBalanceSheet(self):
        return self.balance_sheet
    
    def getCashFlow(self):
        return self.cash_flow
    
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
    :
    def getEbit(self):
        income_state
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    
    def calculateROIC(self):
        income_statement = self.getIncomeStatement()
        cashflow = self.getCashFlow()
        balance_sheet = self.getBalanceSheet()
        
            
        #INCOME STATEMENT
         # for operating income
        operating_income = income_statement.loc['Operating Income']
         # for ebit
        ebit = income_statement.loc['Ebit']
         # for income taxes
        income_taxes = income_statement.loc['Income Tax Expense']

        # BALANCE SHEET
        curr_assets = balance_sheet.loc['Total Current Assets']
         # for NIBCL
        # total current liabilities
        total_curr_liab = balance_sheet.loc['Total Current Liabilities']
        # other current liabilities 
        other_curr_liab = balance_sheet.loc['Other Current Liab']
        # short term debt
        short_term_debt = balance_sheet.loc['Short Long Term Debt']
         # for NPP&E
        ppe = balance_sheet.loc['Property Plant Equipment']
         # for Goodwill
        goodwill = balance_sheet.loc['Good Will']
        
        # calculate NIBCL
        non_interest_bearing_curr_liab = total_curr_liab - short_term_debt
        # calculate NWC
        net_work_cap = curr_assets - total_curr_liab

        # CASH FLOW
         # for depreciation
        depreciation = cashflow.loc['Depreciation']
        # for capex
        capex = cashflow.loc['Capital Expenditures']

        nopat = ebit + depreciation - income_taxes
        invested_capital = net_work_cap + ppe + goodwill

        roic = nopat / invested_capital
        return roic * 100

    def QuarterlyROIC(self):
        income_statement = self.getQuarterlyIncomeStatement()
        cashflow = self.getQuarterlyCashFlow()
        balance_sheet = self.getQuarterlyBalanceSheet()
        #INCOME STATEMENT
         # for operating income
        operating_income = income_statement.loc['Operating Income']
         # for ebit
        ebit = income_statement.loc['Ebit']
         # for income taxes
        income_taxes = income_statement.loc['Income Tax Expense']

        # BALANCE SHEET
        curr_assets = balance_sheet.loc['Total Current Assets']
         # for NIBCL
        # total current liabilities
        total_curr_liab = balance_sheet.loc['Total Current Liabilities']
        # other current liabilities 
        other_curr_liab = balance_sheet.loc['Other Current Liab']
        # short term debt
        short_term_debt = balance_sheet.loc['Short Long Term Debt']
         # for NPP&E
        ppe = balance_sheet.loc['Property Plant Equipment']
         # for Goodwill
        goodwill = balance_sheet.loc['Good Will']
        
        # calculate NIBCL
        non_interest_bearing_curr_liab = total_curr_liab - short_term_debt
        # calculate NWC
        net_work_cap = curr_assets - total_curr_liab

        # CASH FLOW
         # for depreciation
        depreciation = cashflow.loc['Depreciation']
        # for capex
        capex = cashflow.loc['Capital Expenditures']

        nopat = ebit + depreciation - income_taxes
        invested_capital = net_work_cap + ppe + goodwill

        roic = nopat / invested_capital
        return roic * 100

