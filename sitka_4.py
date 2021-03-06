import csv
from datetime import datetime

weather = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(weather, delimiter=",")

header_row = next(csv_file)

for index, column_header in enumerate(header_row):
    print(index, column_header)


highs = []
dates = []
lows = []


for row in csv_file:

    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])

    except ValueError:

        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)


print(highs)
print(dates)


import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates, highs, c="red")

plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.3)
plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
# shows graph
fig.autofmt_xdate()
plt.show()
