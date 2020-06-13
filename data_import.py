# Import Modules
from datetime import datetime
from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import yfinance as yf
yf.pdr_override()

# Data Import Through Yahoo Finance
start_date = '2006-01-01'
end_date = '2020-06-12'
BAC = data.get_data_yahoo('BAC', start_date, end_date)
print(BAC)
