import uuid


class LongTakeProfit:
    """Agent that keeps open positions and close when the profit is reached"""


    def __init__(self, takeProfit, maxPositions):
        """ Constructor.

            :param float takeProfit: percentage (range 0.0 - 1.0) of desired profit
            :param int maxPositions: number of maximum positions to mantain opened (-1 for ulimited)
        """

        self.takeProfit = takeProfit
        self.maxPositions = maxPositions

        self.positions = {}



    def open(self, price):
        """ Opens a position
            Returns the identifier or None in case no more positions can be opened
        """

        if self.maxPositions<0 or len(self.positions)<self.maxPositions:
            posId = uuid.uuid4()
            self.positions[posId] = price
            return posId            
        else:
            return None



    def processPrice(self, price):
        """ Evaluates the price.
            If one of the positions (or several) has profit, returns an array with their id.
            If no position has profit, the array returned will be empty
        """
        closePos = []

        ## TODO: Optimize me. A sorted list of open prices, can find the list of positions 
        ## to close in O(logN)
        breakPrice = price / (1.0 + self.takeProfit)
        for posId in self.positions:
            if self.positions[posId] <= breakPrice:
                closePos.append(posId)

        for posId in closePos: del self.positions[posId]

        return closePos



    def closeAllPositions(self):
        """ Closes all positions
            Returns the dictionary with all closed positions and opening prices
        """
        pos = self.positions
        self.positions = {}
        return pos
