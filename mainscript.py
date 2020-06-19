# Offline Imports
from utils import oneDayDelay
from utils import oneDayDelay_plt
# Other Libraries, may require PIP installation
import statistics as st
import matplotlib.pyplot as plt
from pandas_datareader import data, wb
from datetime import datetime
import pandas as pd
import numpy as np
import datetime
from datetime import date
import yfinance as yf
yf.pdr_override()


# From CSV ticker file to list of strings, can use the nasdaq list for a larger
# list
tickersOfInterest = pd.read_csv('tickersofinterest.csv')
tickerStr = []
for number in range(0, len(tickersOfInterest)):
    tickerStr.append(tickersOfInterest.iloc[number].values[0])

# Data Import Through Yahoo Finance, 15 years worth of data
# Uses dictionary comprehension to store dataframes
start_date = '2005-01-01'
end_date = date.today()

print('\n \n********************')
print(' DOWNLOADING ...')
print('******************** \n \n')

stock_data = {}
for i in range(len(tickerStr)):
    print("Downloading: " + tickerStr[i])
    case = {tickerStr[i]: data.get_data_yahoo(
        tickerStr[i], start_date, end_date)}
    stock_data.update(case)

# Moving through all the data to find pct_changes
stock_data_returns = {}
for i in range(len(stock_data.keys())):
    case = {tickerStr[i]: stock_data[tickerStr[i]].pct_change()}
    stock_data_returns.update(case)

# Row Delay Correlation
print('\n \n********************')
print(' ALL DATA DOWNLOADED')
print('******************** \n \n')

testcols = stock_data_returns['ASML']['Close']
testdictionary = oneDayDelay(testcols)
oneDayDelay_plt(testdictionary[0], testdictionary[1])
