import pandas as pd
from main.indicators.ema import ema

def macd(prices, periodA: int = 13, periodB: int = 26, periodSignal: int = 9, fieldName = 'macd'):
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

    # Calculate EMA(12) and EMA(26)
    ema_A = ema(close_prices, period=periodA)
    ema_B = ema(close_prices, period=periodB)

    # Calculate MACD line (EMA(A) - EMA(B))
    macd_line = [emaA - emaB for emaA, emaB in zip(ema_A, ema_B)]

    # Calculate Signal line (periodSignal EMA of the MACD line)
    signal_line = ema(macd_line, period=periodSignal)

    # Add MACD and Signal Line to the price data
    for i in range(len(prices)):
        prices[i]['macd-' + str(periodA) + '-' + str(periodB) + '-' + str(periodSignal)] = macd_line[i]
        prices[i]['macd_signal_line-' + str(periodA) + '-' + str(periodB) + '-' + str(periodSignal)] = signal_line[i]

    return prices
