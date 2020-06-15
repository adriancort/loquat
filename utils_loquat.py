# Function that downloads Files
from datetime import datetime
from pandas_datareader import data, wb
import pandas as pd
from datetime import date
import yfinance as yf
yf.pdr_override()

start_date = '2005-01-01'
end_date = date.today()


def updateStockData(start, end):
    ASML_df = data.get_data_yahoo('ASML', start, end)
    ASML_df.to_csv('StockData/ASML.csv')

    AAPL_df = data.get_data_yahoo('AAPL', start, end)
    AAPL_df.to_csv('StockData/AAPL.csv')

    SOXL_df = data.get_data_yahoo('SOXL', start, end)
    SOXL_df.to_csv('StockData/SOXL.csv')

    WMT_df = data.get_data_yahoo('WMT', start, end)
    WMT_df.to_csv('StockData/WMT.csv')

    MA_df = data.get_data_yahoo('MA', start, end)
    MA_df.to_csv('StockData/MA.csv')

    MSFT_df = data.get_data_yahoo('MSFT', start, end)
    MSFT_df.to_csv('StockData/MSFT.csv')

    NKE_df = data.get_data_yahoo('NKE', start, end)
    NKE_df.to_csv('StockData/NKE.csv')

    INTC_df = data.get_data_yahoo('INTC', start, end)
    INTC_df.to_csv('StockData/INTC.csv')

    NKE_df = data.get_data_yahoo('NKE', start, end)
    NKE_df.to_csv('StockData/NKE.csv')

    BABA_df = data.get_data_yahoo('BABA', start, end)
    BABA_df.to_csv('StockData/BABA.csv')

    BYND_df = data.get_data_yahoo('BYND', start, end)
    BYND_df.to_csv('StockData/BYND.csv')

    BLK_df = data.get_data_yahoo('BLK', start, end)
    BLK_df.to_csv('StockData/BLK.csv')

    SKY_df = data.get_data_yahoo('SKY', start, end)
    SKY_df.to_csv('StockData/SKY.csv')

    GM_df = data.get_data_yahoo('GM', start, end)
    GM_df.to_csv('StockData/GM.csv')

    AXP_df = data.get_data_yahoo('AXP', start, end)
    AXP_df.to_csv('StockData/AXP.csv')

    ARKK_df = data.get_data_yahoo('BYND', start, end)
    ARKK_df.to_csv('StockData/BYND.csv')

    PYPL_df = data.get_data_yahoo('PYPL', start, end)
    PYPL_df.to_csv('StockData/PYPL.csv')

    RY_df = data.get_data_yahoo('RY', start, end)
    RY_df.to_csv('StockData/RY.csv')

    ENPH_df = data.get_data_yahoo('ENPH', start, end)
    ENPH_df.to_csv('StockData/ENPH.csv')

    NCLH_df = data.get_data_yahoo('NCLH', start, end)
    NCLH_df.to_csv('StockData/NCLH.csv')

    RCL_df = data.get_data_yahoo('RCL', start, end)
    RCL_df.to_csv('StockData/RCL.csv')

    OVID_df = data.get_data_yahoo('OVID', start, end)
    OVID_df.to_csv('StockData/OVID.csv')

    LK_df = data.get_data_yahoo('LK', start, end)
    LK_df.to_csv('StockData/LK.csv')

    print(' All Data Downloaded, Files Created')
