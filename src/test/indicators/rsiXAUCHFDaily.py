import csv
import sys

from main.indicators.rsi import rsi

period = int(sys.argv[1])
with open('XAUCHF1440.csv') as f:
    dailyPrices  = [{k: v for k,v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

print(dailyPrices[1])

dailyPricesRSI = rsi(dailyPrices, period)

for line in dailyPricesRSI:
    print(line)
