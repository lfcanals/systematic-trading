from main.agents.longTakeProfit import LongTakeProfit


def daysToEnter(dailyPrices, profit, termDays, spread):
    """
        Calculates the days in which entering in the worst moment,
        an expected profit is achieved in the termDays period.

        :param dailyPrices: list of dictionary of daily prices 
                with fields date,high,low,open,close.
        :param float profit: 0 to 1 prcentage of desired profit
        :param int termDays: 5 for one week, etc...
        :param termDays: maximum days to retain the position
        :param float spread: (half) spread to buy and to sell
        :return: a list of dictionaries with the 'in' and 'out' days in which
                the desired profit can be taken in less than required term
    """

    agent = LongTakeProfit(profit, 1)
    suitableDays = []

    for i in range(2,len(dailyPrices)):
        agent.closeAllPositions()

        inDay = dailyPrices[i]
        prevInDay = dailyPrices[i-1]
        #worstEntryPrice = float(inDay['high']) + spread
        worstEntryPrice = float(inDay['open']) + spread
        posId = agent.open(worstEntryPrice)
        if posId == None:
            print("Cannot open position!!")
            break


        # Check future prices in termDays days
        #
        for j in range(i+1, min(len(dailyPrices), i+termDays+1)):
            prevOutDay = dailyPrices[i-1]
            outDay = dailyPrices[j]
            bestPrice = float(outDay['high']) - spread;
            closedPos = agent.processPrice(bestPrice)
            if len(closedPos) != 0:
                suitableDays.append({'in':inDay, 'out':outDay, 'prev-in': prevInDay, 
                        'prevOutDay': prevOutDay})
                break

    return suitableDays

