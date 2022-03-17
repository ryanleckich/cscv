import csv
from datetime import datetime


weather = open("sitka_weather_2018_simple.csv", "r")
csv_file = csv.reader(weather, delimiter=",")


header_row = next(csv_file)


print(type(header_row))


for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []


for row in csv_file:
    highs.append(int(row[5]))

    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)
    lows.append(int(row[6]))


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


fig.autofmt_xdate()
plt.show()


plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska 2018")


plt.show()
