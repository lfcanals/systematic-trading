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
        agent = LongTakeProfit(0.1, -1)

        posId1 = agent.open(100.0)
        posId2 = agent.open(100.0)
        posId3 = agent.open(200.0)

        empty = agent.processPrice(99)
        self.assertTrue(len(empty) == 0)

        pos1And2 = agent.processPrice(111)
        self.assertTrue(len(pos1And2) == 2)
        self.assertTrue(
            (pos1And2[0] == posId1 and pos1And2[1] == posId2)
            or
            (pos1And2[0] == posId2 and pos1And2[1] == posId1))

        onlyPosId3 = agent.processPrice(240)
        self.assertTrue(len(onlyPosId3) == 1 and onlyPosId3[0] == posId3)



    def test_openAndPricesUlimitedPositions(self):
        agent = LongTakeProfit(0.1, -1)


    def test_openAndPricesThreeMaxPositions(self):
        agent = LongTakeProfit(0.1, 3)
