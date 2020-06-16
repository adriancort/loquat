# Import Modules
from utils_loquat import updateStockData
import utils_loquat
from pandas_datareader import data, wb
from datetime import datetime
import pandas as pd
import numpy as np
import datetime
from datetime import date
import yfinance as yf
yf.pdr_override()

# From CSV ticker file to list of strings
tickersOfInterest = pd.read_csv('tickersofinterest.csv')
tickerStr = []
for number in range(0, len(tickersOfInterest)):
    tickerStr.append(tickersOfInterest.iloc[number].values[0])


# Data Import Through Yahoo Finance, 15 years worth of data
# Uses dictionary Comprehension to store dataframes
start_date = '2005-01-01'
end_date = date.today()

stock_data = {}
for i in range(len(tickerStr)):
    case = {tickerStr[i]: data.get_data_yahoo(
        tickerStr[i], start_date, end_date)}
    stock_data.update(case)
stock_data.items()
