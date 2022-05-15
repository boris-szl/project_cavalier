import pandas as pd
import datetime as dt
import numpy as np
import requests
import re as r
import json

# to do
# rename functions to conventional use

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.3"
    }

def getRiskFreeRatesForAustria():
    # returns long-term interest rate for convergence purposes - 10 years maturity, from last month to 1993
    # in pandas.DataFrame format´-ß.po
    source = "https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=229.IRS.M.AT.L.L40.CI.0000.EUR.N.Z"
    data = pd.read_html(requests.get(source, headers=headers).text)
    table = data[5].loc[2:].reset_index(drop=True)
    table = table.drop(columns=["obs. status"])
    table.columns = ["Period", "Values in %"]
    return table

def getRiskFreeRateEuroArea(country_code, currency_code):
    # def getRiskFreeRateEuroArea():
    #     # source: https://sdw.ecb.europa.eu/
    #     # ID for 10 year-treasury : 229
    #     # querly_url : https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=229
    #     # series_key = IRS.M.AT.L.L40.CI.0000.EUR.N.Z
    #     # country_code = AT
    assert isinstance(country_code, str), "Only string values"
    assert len(country_code) == 2, "Country must be two characters long"
    assert isinstance(currency_code, str), "Only string values"
    assert len(currency_code) == 3, "Currency must be three characters long"
    try:
        BASE_URL = "https://sdw.ecb.europa.eu/quickview.do?SERIES_KEY=229.IRS.M." + country_code + ".L.L40.CI.0000." + currency_code + ".N.Z"
        data = pd.read_html(requests.get(BASE_URL, headers=headers).text)
        table = data[5].loc[2:].reset_index(drop=True)
        table = table.drop(columns=["obs. status"])
        table.columns = ["Period", "Values in %"]
        return table
    except AssertionError as msg:
        print(msg)


def getSwissRiskFreeRate():
    # https://www.snb.ch/selector/en/mmr/intfeed/rss
    return 0

def getUsRiskFreeRate():
    return 0

# def getRiskFreeRateForNonEuroArea();

# def getRiskFreeRateForEuroCountry();

def getRiskFreeRateUs():
    # returns dataframe that contains the yield of
    # us treasury bonds with maturiites of close to ten years
    date = dt.datetime.now().year
    URL = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_long_term_rate&field_tdr_date_value=" + str(date)
    table = pd.read_html(URL)
    return table[0].iloc[:,[0,3]]

def getRiskFreeRateMonth():
    # returns dataframe that contains teh
    date = dt.datetime.now().year
    URL = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_long_term_rate&field_tdr_date_value=" + str(date)
    table = pd.read_html(URL)
    return table[0].iloc[:,[0,3]]

def getCurrentRiskFreeRateUs():
    # returns todays (working day) us 10-yr treasury yield
    data = getRiskFreeRateUs()
    return np.around(np.float32(data.iloc[-1,[1]])/100, 4)

def getRawBetaData():
    # parses taable data for Total Betas by Sector (for computing private company costs of equity) - US
    # from NYU Stern School Of Business Professor Aswath Damodaran
    # returns Pandas.DataFrame
    # String values for Industry Name Column contain redundant whitespaces and ununified shortings
    # please use the CleanedBetaData() method
    URL2 = "http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html"
    beta_table = pd.read_html(URL2)
    df_beta = beta_table[0]
    df_beta = df_beta.set_axis(df_beta.iloc[0], axis="columns", inplace=False) 
    df_beta = df_beta.drop(0)
    return df_beta

# either i create a new module or i merge this with
# getRawBetaData(), more likely to merge it with the function
def cleaningBetaData(dataframe):
    beta_data = dataframe
    beta_data = beta_data.set_index('Industry Name')
    # remove whitespace in index
    old_index = beta_data.index
    new_index = []
    for i in old_index:
        new_index.append(" ".join(i.split()))
    # replace value in new_index
    tuple_1 = [("Financial Svcs. (Non-bank & Insuran", "Financial Services (Non-bank  & Insurance)"),
          ("Healthcare Information and Technol","Healthcare Information and Technology"),
           ("Oil/Gas (Production and Exploratio", "Oil/Gas (Production and Exploration)"),
           ("Oilfield Svcs/Equip.", "Oilfield Services/Equipment"),
           ("R.E.I.T", "Real Estate Investment Trust"),
           ("Restaurant/Dining", "Restaurants"),
           ("Rubber& Tires", "Rubber & Tires"),
          ("Semiconductor Equip", "Semiconductor Equipment"),
          ("Software, System & Application", "Software System & Application"),
          ("Telecom (Wireless)", "Telecommunication (Wireless)"),
          ("Telecom. Equipment", "Telecommunication Equipment"),
          ("Telecom. Services", "Telecommunication Services"),
          ("Total Market (without financials)", "Total Market (excl. Financials)")]
    for i in range(len(tuple_1)):
        new_index = [w.replace(tuple_1[i][0], tuple_1[i][1]) for w in new_index]

    # df.set_index([pd.Index([1, 2, 3, 4]), 'year'])
    beta_data = beta_data.set_index([pd.Index(new_index)])
    return beta_data

def getCleanedBetaData():
    beta_data = getRawBetaData()
    beta_data = beta_data.set_index('Industry Name')
    # remove whitespace in index
    old_index = beta_data.index
    new_index = []
    for i in old_index:
        new_index.append(" ".join(i.split()))
    # replace value in new_index
    tuple_1 = [("Financial Svcs. (Non-bank & Insuran", "Financial Services (Non-bank  & Insurance)"),
          ("Healthcare Information and Technol","Healthcare Information and Technology"),
           ("Oil/Gas (Production and Exploratio", "Oil/Gas (Production and Exploration)"),
           ("Oilfield Svcs/Equip.", "Oilfield Services/Equipment"),
           ("R.E.I.T", "Real Estate Investment Trust"),
           ("Restaurant/Dining", "Restaurants"),
           ("Rubber& Tires", "Rubber & Tires"),
          ("Semiconductor Equip", "Semiconductor Equipment"),
          ("Software, System & Application", "Software System & Application"),
          ("Telecom (Wireless)", "Telecommunication (Wireless)"),
          ("Telecom. Equipment", "Telecommunication Equipment"),
          ("Telecom. Services", "Telecommunication Services"),
          ("Total Market (without financials)", "Total Market (excl. Financials)")]
    for i in range(len(tuple_1)):
        new_index = [w.replace(tuple_1[i][0], tuple_1[i][1]) for w in new_index]

    # df.set_index([pd.Index([1, 2, 3, 4]), 'year'])
    beta_data = beta_data.set_index([pd.Index(new_index)])
    return beta_data

def getUnleveredBeta():
    df = getRawBetaData().T
    df = df.iloc[[0,5,15,14,13,12,11]]
    df = df.T
    df = df.set_index('Industry Name')
    dates = []
    for j in range(6):
        dates.append(dt.date.today().year-j)
    df.set_axis(dates, axis="columns", inplace=True)
    df = df.rename(index={"Total  Market (without financials)":"Total Market (without financials)"})
    df = df.rename(index={"Software  (System & Application)":"Software, System & Application"})
    return df

def getUnleveredCleanedBeta():
    df = getCleanedBetaData().T
    df = df.iloc[[4,13,12,11,10]]
    df = df.T
    dates = []
    for j in range(5):
        dates.append(dt.date.today().year-j)
    df.set_axis(dates, axis="columns", inplace=True)
    return df

def getIndustryNames():
    return betaData()

def getSpecifiedUnleveredBeta(industry="Total Market", year=dt.date.today().year):
    data = getUnleveredBeta()
    return np.double(data.loc[industry,year])

def getCapitalCosts():
    URL4 = "http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html"
    coc_table = pd.read_html(URL4)
    df_coc = coc_table[0]
    df_coc = df_coc.set_axis(df_coc.iloc[0], axis="columns", inplace=False)
    df_coc = df_coc.drop(0)
    df_coc = df_coc.set_index("Industry  Name")
    return df_coc

def getCostOfEquity(industry="Total Market"):
    df = capitalCosts()
    if industry != 0:
        industry_specific_value = df['Cost of Equity'].loc[industry].strip('%')
        numerical_value = np.double(industry_specific_value)/100
        return numerical_value
    else:
        return df["Cost of Equity"]

def getMarketCostOfCapital():
    df = capitalCosts()
    return np.double(df["Cost of Capital"][-2].strip("%"))/100

def getMarketCostOfDebt():
    df = capitalCosts()
    return np.double(df.iloc[-2][5].strip('%'))/100

def getCostOfDebt(industry='Total  Market'):
    df = capitalCosts().iloc[:,[5]]
    np_array = df.loc[industry].to_numpy()
    return np.double(np_array[0].strip('%'))/100


def getImpliedRiskPremiumData():
    URL5 = "http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/histimpl.html"
    rp_table = pd.read_html(URL5)
    df_rp = rp_table[0]
    df_rp = df_rp.fillna(0)
    df_rp = df_rp.set_axis(df_rp.iloc[0], axis="columns",inplace=False)
    df_rp = df_rp.drop(0)
    return df_rp

def getImpliedERPData():
    df = getImpliedRiskPremiumData()
    df_erp = df[["Year","Implied Premium (FCFE with sustainable Payout)"]]
    df_erp = df_erp.set_index("Year")
    return df_erp

def countryRisk():
    URL6 = "http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html"
    country_risk_table = pd.read_html(URL6)
    df = country_risk_table[0]
    df = df.set_axis(df.iloc[0], axis="columns", inplace=False)
    df = df.drop(0)
    return df.iloc[:,0:5]

def getERP():
    # United States is assigned as default paramter
    df = countryRisk()
    return df.iloc[:,[0,-1]]


def getCountryERP(country='United States'):
    data = getERP().set_index("Country")
    value = data.T[country].to_numpy()
    return np.double(value[0].strip('%'))/100

def calculateEquityCost():
    # equity_cost = risk_premium * unlevered_beta + risk_free_rate
    return  0

def calculateWacc(industry='Total Market', country='United States', year=dt.date.today().year):
    # get risk free rate
    risk_free_rate = getCurrentRiskFreeRate()
    # get countries equity risk premium
    risk_premium = getCountryERP(country)
    # todays unlevered beta
    unlevered_beta = getUnleveredBeta(industry,year)
    # cost of equity
    equity_cost = risk_premium * unlevered_beta + risk_free_rate
    post_tax_debt_cost = getCostOfDebt()
    result = equity_cost + post_tax_debt_cost
    return result

def calculateWacc_2(industry='Total Market', country='United States', year=dt.date.today().year):
    return getRiskFreeRate() + getCountryERP(country) * getUnleveredBeta(industry,year) + getCostOfDebt()






