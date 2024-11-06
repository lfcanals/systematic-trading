import unittest
from main.markers.profitableDays import profitableDays

class TestProfitableDaysMethod(unittest.TestCase):

    
    #
    # Asserts if the profit of one step forward is as properly calculated
    #
    def assertProfitOneDay(self, profitables, i, profit):
        if profitables[i+1]['high'] - profitables[i]['open'] >= profitables[i]['open']*profit:
            self.assertTrue(profitables[i]['profitable'] == 1, str(profitables[i]) + " and then " \
                    + str(profitables[i]) + " do not calculate as " + str(profit) + " profit")
        else:
            self.assertTrue(profitables[i]['profitable'] == 0, str(profitables[i]) + " and then " \
                    + str(profitables[i]) + " do not calculate as NOT profit of " + str(profit))
     
    
    #
    # Asserts if the profit of N step forward is as properly calculated
    # These two functions are different, even when one is a subset of the other
    # to code the things in two different ways. Do not simplify; this is testing code
    # one of the values is to try to find wrongly coded functions.
    #
    def assertProfitNDays(self, profitables, i, profit, steps):
        maxProf = 0
        for j in range(1, steps+1):
            maxProf = max(maxProf, profitables[i+j]['high'] - profitables[i]['open'])
            if profitables[i]['profitable'] == 1:
                self.assertTrue(maxProf >= profitables[i]['open']*profit, \
                    'Profit in two days wrongly detected for ' + str(profitables[i]))
            else:
                self.assertTrue(maxProf < profitables[i]['open']*profit, \
                    'NOT-Profit in two days wrongly detected for ' + str(profitables[i]))
    
    
    
    def setUp(self):    
        self.dailyPrices = []
        self.opens = [1,1,  1,  1,  1,  1,  1,  1,  1,1,1,1,1,1]
        self.highs = [1,1.1,1.2,1.3,1.2,1.3,1.2,1.1,1,1,1,1,1,1]
    
        for i in range(0, len(self.opens)):
            self.dailyPrices.append({'date': 'somewhen',
                        'open': self.opens[i],
                        'close': self.opens[i],
                        'high': self.highs[i],
                        'low': self.highs[i]/2,
                        'volume': 1000})
                        
    

    def test_required_profit_zero(self):
        profit=0.0000000001
        profitables = profitableDays(self.dailyPrices, profit = profit, 
                termDays=1, spread=0, fieldName='profitable')
        for i in range(0, len(profitables)-1):
            if profitables[i+1]['high'] > profitables[i]['open']:
                self.assertTrue(profitables[i]['profitable']==1)
            else:
                self.assertTrue(profitables[i]['profitable']==0)
                

    def test_one_percent_profit(self):
        profit=0.01
        profitables = profitableDays(self.dailyPrices, profit=profit,
                termDays=1, spread=0, fieldName='profitable')
        for i in range(0, len(profitables)-1):
            self.assertProfitOneDay(profitables, i, profit)
    
    
    def test_one_percent_profit_two_days(self):
        profit = 0.01
        profitables = profitableDays(self.dailyPrices, profit=profit,
                termDays=2, spread=0, fieldName='profitable')
        for i in range(0, len(profitables)-2):
            self.assertProfitNDays(profitables, i, profit, 2)
    
    
    def test_huge_spread_and_no_profit(self):
        profit = 0.1
        profitables = profitableDays(self.dailyPrices, profit=profit,
                termDays=4, spread=2, fieldName='profitable')
        for i in range(0, len(profitables)-4):
            self.assertTrue(profitables[i]['profitable'] == 0)
    
    
    
if __name__ == '__main__': unittest.main()    
