import csv
import sys

from main.markers.daysToEnter import daysToEnter
from main.indicators.rsi import rsi


daysTerm = int(sys.argv[1])
profit = float(sys.argv[2])

XAUCHF_SPREAD = 23

with open('XAUCHF1440.csv') as f:
    dailyPrices  = [{k: v for k,v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

print("Check this first line...")
print(dailyPrices[1])
print

dailyPrices = rsi(dailyPrices, 2)
dailyPrices = rsi(dailyPrices, 5)
dailyPrices = rsi(dailyPrices, 10)
dailyPrices = rsi(dailyPrices, 15)
dailyPrices = rsi(dailyPrices, 20)

suitableDays = daysToEnter(dailyPrices, profit, daysTerm, XAUCHF_SPREAD)

for moments in suitableDays:
    print(moments)

