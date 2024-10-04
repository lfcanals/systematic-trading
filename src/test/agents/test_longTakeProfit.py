import unittest
import main.agents
from main.agents.longTakeProfit import LongTakeProfit

class TestLongTakeProfit(unittest.TestCase):


    def test_open(self):
        agent = LongTakeProfit(0.1, -1)
        posIds = []
        for i in range(1,5):
            posIds.append(agent.open(i*1.1))

        for i in range(1,5):
            posIds.append(agent.open(i*1.1))


        # Checks all posId are different and incremental
        self.assertEqual(2*len(range(1,5)), len(posIds))
        setOfPosId = set() 
        for p in posIds:
            self.assertFalse(p in setOfPosId)
            setOfPosId.add(p)


    def test_prices(self):
        agent = LongTakeProfit(0.1, 0)

    def test_openAndPricesUlimitedPositions(self):
        agent = LongTakeProfit(0.1, -1)


    def test_openAndPricesThreeMaxPositions(self):
        agent = LongTakeProfit(0.1, 3)
