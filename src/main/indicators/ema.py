import pandas as pd

def ema(prices, period):
    """Calculate Exponential Moving Average (EMA) for a given period."""
    prices_series = pd.Series(prices)
    return prices_series.ewm(span=period, adjust=False).mean().tolist()
