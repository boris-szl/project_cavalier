import pandas as pd
import datetime as dt
import numpy as np

def getRisFreeRateUS():
    return 0

def getRiskFreeRateMonth():
    URL = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_long_term_rate&field_tdr_date_value_month=202202"
    table = pd.read_html(URL)
    return table[0].iloc[:,[0,3]]

def getCurrentRiskFreeRate():
    data = getRiskFreeRateMonth()
    return np.double(data.iloc[-1,[1]])/100

def getBetaData():
    URL2 = "http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html"
    beta_table = pd.read_html(URL2)
    df_beta = beta_table[0]
    df_beta = df_beta.set_axis(df_beta.iloc[0], axis="columns", inplace=False) 
    df_beta = df_beta.drop(0)
    return df_beta

def getUnleveredBeta():
    df = getBetaData().T
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

def getIndustryNames():
    return betaData()

def getUnleveredBeta(industry="Total Market", year=dt.date.today().year):
    data = getUinleveredBeta()
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
    return np.double(value[0].strip('%'))/100#

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
