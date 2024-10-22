import pandas as pd

def ema(prices, period):
    """Calculate Exponential Moving Average (EMA) for a given period."""
    prices_series = pd.Series(prices)
    return prices_series.ewm(span=period, adjust=False).mean().tolist()


def bullBear(prices, period: int = 13, fieldName = 'bullBear'):
    """
        Calculate the Bull/Bear Power

        :param prices: list of dictionary of daily prices 
                with fields date,high,low,open,close.
        :param period: The period for calculating Bull/Bear Power (default is 13).
        :return: A list of dictionaries containing the Bull/BEar Power indicator values in the field.
    """

    df = pd.DataFrame(prices)

    # Extract closing prices for EMA calculation
    close_prices = [price['close'] for price in prices]
    
    # Calculate EMA(13)
    ema_period = ema(close_prices, period)
    
    # Add Bull and Bear Power to the price data
    for i in range(len(prices)):
        bull_power = float(prices[i]['high']) - ema_period[i]
        bear_power = float(prices[i]['low']) - ema_period[i]
        prices[i]['bull_power' + str(period)] = bull_power
        prices[i]['bear_power' + str(period)] = bear_power
    
    return prices
