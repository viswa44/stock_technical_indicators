# decision_making.py
def make_decision(data):
    """
    Generates BUY, SELL, or NEUTRAL decision based on moving average, Bollinger Bands, and CCI.
    """
    decisions = []
    for idx, row in data.iterrows():
        if row['Close'] > row['Upper_Band'] and row['CCI'] > 100:
            decisions.append('SELL')
        elif row['Close'] < row['Lower_Band'] and row['CCI'] < -100:
            decisions.append('BUY')
        else:
            decisions.append('NEUTRAL')
    data['Decision'] = decisions
    return data
