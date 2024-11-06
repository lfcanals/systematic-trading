from main.agents.longTakeProfit import LongTakeProfit
import copy


def profitableDays(dailyPrices, profit, termDays, spread, fieldName = 'profitable'):
    """
        Calculates the days in which entering in the begining of the day
        will have a profit before the termDays, applying the spread
        in the entry and the exit.

        :param dailyPrices: list of dictionary of daily prices 
                with fields date,high,low,open,close.
        :param float profit: 0 to 1 prcentage of desired profit
        :param int termDays: 5 for one week, etc...
        :param termDays: maximum days to retain the position
        :param float spread: (half) spread to buy and to sell
        :return: a list of dictionaries with the 'in' and 'out' days in which
                the desired profit can be taken in less than required term
    """

    prices = copy.deepcopy(dailyPrices)

    # Of course we can improve this code!!
    # Typical example of:
    #     x = array of numbers
    #     y = array of numbers same size as x
    #     w = sliding window of 'termDays' size on y
    #     mark the elements in x such that:
    #           max(w) - x >= profit*x

    w = []
    for i in range(0,termDays): w.append(float(prices[i]['high']))
    for i in range(0,len(prices)-termDays):
        w.pop(0)
        w.append(float(prices[i+termDays]['high']))

        max_price = max(w)
        entryPrice = float(prices[i]['open'])

        if max_price - entryPrice - spread*2 >= profit*entryPrice :
            prices[i]['profitable'] = 1
        else:
            prices[i]['profitable'] = 0


    return prices

