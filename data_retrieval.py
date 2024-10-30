# data_retrieval.py
from yahoo_fin import stock_info as si
import pandas as pd

def get_currency_data(start_date, end_date):
    """
    Retrieves historical EUR/INR currency data from Yahoo Finance.
    """
    symbol = "EURINR=X"
    data = si.get_data(symbol, start_date=start_date, end_date=end_date)
    data = data[['close']]  # Only take the close price
    data.columns = ['Close']
    return data
