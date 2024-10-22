import csv
import sys

from main.indicators.macd import macd

periodA = int(sys.argv[1])
periodB = int(sys.argv[2])
periodSignal = int(sys.argv[3])

with open('XAUCHF1440.csv') as f:
    dailyPrices  = [{k: v for k,v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]

print(dailyPrices[1])

macdPrices = macd(dailyPrices, periodA, periodB, periodSignal)

for line in macdPrices:
    print(line)


