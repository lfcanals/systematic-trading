import pandas as pd
from main.indicators.ema import ema



def ma(prices, period: int = 13, fieldName = 'ma'):
    """
        Calculate the Bull/Bear Power

        :param prices: list of dictionary of daily prices 
                with fields date,high,low,open,close.
        :param period: The period for calculating Bull/Bear Power (default is 13).
        :return: A list of dictionaries containing the Bull/BEar Power indicator values in the field.
    """


    # Extract closing prices for EMA calculation
    close_prices = [float(price['close']) for price in prices]
    
    # Calculate Simple MA values
    sma_values = []
    for i in range(len(close_prices)):
        if i < period - 1:
            sma_values.append(None)  # Not enough data to calculate SMA
        else:
            sma_values.append(sum(close_prices[i-period+1:i+1]) / period)
    
    # Add SMA to the price data
    for i in range(len(prices)):
        prices[i]['ma' + str(period)] = sma_values[i]

    return prices
