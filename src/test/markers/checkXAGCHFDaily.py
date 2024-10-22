import csv
import sys

from main.markers.daysToEnter import daysToEnter


daysTerm = int(sys.argv[1])
profit = float(sys.argv[2])
XAGCHF_SPREAD = 0.027

with open('XAGCHF1440.csv') as f:
    dailyPrices  = [{k: v for k,v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

print(dailyPrices[1])

suitableDays = daysToEnter(dailyPrices, profit, daysTerm, XAGCHF_SPREAD)

for moments in suitableDays:
    print(moments)

