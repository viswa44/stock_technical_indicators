# technical_indicators.py
import pandas as pd

def calculate_moving_average(data, window=20):
    """
    Calculates the moving average for a specified window.
    """
    data[f'MA_{window}'] = data['Close'].rolling(window=window).mean()
    return data

def calculate_bollinger_bands(data, window=20):
    """
    Calculates Bollinger Bands for the specified window.
    """
    data = calculate_moving_average(data, window)
    data['StdDev'] = data['Close'].rolling(window=window).std()
    data['Upper_Band'] = data[f'MA_{window}'] + (data['StdDev'] * 2)
    data['Lower_Band'] = data[f'MA_{window}'] - (data['StdDev'] * 2)
    return data

def calculate_cci(data, window=20):
    """
    Calculates the Commodity Channel Index (CCI) for the specified window.
    """
    data['TP'] = (data['Close'] + data['Close'] + data['Close']) / 3
    data['SMA'] = data['TP'].rolling(window=window).mean()
    data['MAD'] = data['TP'].rolling(window=window).apply(lambda x: (x - x.mean()).abs().mean())
    data['CCI'] = (data['TP'] - data['SMA']) / (0.015 * data['MAD'])
    return data
