import pandas as pd

def rsi(prices, period: int = 14, fieldName = 'rsi'):
    """
        Calculate the Relative Strength Index (RSI) for a given dataset.

        :param prices: list of dictionary of daily prices 
                with fields date,high,low,open,close.
        :param period: The period for calculating RSI (default is 14).
        :return: A pandas Series containing the RSI values.


        RSI over 70 indicates overbought : do not continue buying
        RSI under 30 indicates oversold : do not continue selling
    """

    df = pd.DataFrame(prices)

    # Calculate price changes
    df['close'] = df['close'].astype(float)
    df['delta'] = df['close'].diff().round(8)

    # Calculate gains and losses
    df['gain'] = df['delta'].where(df['delta'] > 0, 0)
    df['loss'] = -df['delta'].where(df['delta'] < 0, 0)

    # Calculate rolling average gains and losses
    avg_gain = df['gain'].rolling(window=period, min_periods=1).mean()
    avg_loss = df['loss'].rolling(window=period, min_periods=1).mean()

    # Calculate the Relative Strength (RS)
    rs = avg_gain / (avg_loss.replace(0, 1e-10))

    # Calculate the RSI
    df[fieldName + str(period)] = 100 - (100 / (1 + rs))

    # Convert the DataFrame back to list of dictionaries, including the RSI values
    result = df.to_dict(orient='records')

    return result

