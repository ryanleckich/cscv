import csv


outfile = open(
    "/Users/ryanleckich/Desktop/School/AdvancedPython/CSV_Project-1/sitka_weather_07-2018_simple.csv",
    "r",
)
csv_file = csv.reader(outfile, delimiter=",")

header_row = next(csv_file)
# print(type(header_row))

# for index, column_header in enumerate(header_row):
# print(index, column_header)


highs = []

for i in csv_file:
    highs.append(int(i[5]))

print(highs)

import matplotlib.pyplot as plt


plt.plot(highs, c="red")

plt.title("Daily high temp, July 2008", fontsize=16)
plt.xlabel("")
plt.ylabel("Tempertures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
