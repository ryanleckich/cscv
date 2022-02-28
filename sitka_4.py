import csv
from datetime import datetime


outfile = open("death_valley_2018_simple.csv", "r")
csv_file = csv.reader(outfile, delimiter=",")

header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []
lows = []

# test_date = datetime.striptime("2018-01-01"), ("%Y-%m-%d")

for row in csv_file:

    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError:
        print(f" missing data for {current_date}")

    else:

        highs.append(high)
        lows.append(low)
        dates.append(current_date)


print(highs)

import matplotlib.pyplot as plt

figure = plt.figure


plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="red")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)


plt.title("Daily low and high temperature like - 2018", fontsize=16)
plt.xlabel("Month of July 1018")
plt.ylabel("Tempertures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)


figure.autofmt_xdate()


plt.subplot(
    2,
    1,
    1,
)
plt.plot9(dates, highesply.playgorun)

plt.suptilte(" High and Lows of Stika, Alaskas 2018")
