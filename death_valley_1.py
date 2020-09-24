import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)
'''
print(header_row)

#enumerate shows us index and value of each item in list

for index, column_header in enumerate(header_row):
    print(index,column_header)
'''
highs = [] #for y axis
lows = []
dates = [] #for x axis

#print(x)

for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: #if anything in try fails
        print(f'Missing data for {the_date}')
    else: #if nothing fails
        highs.append(high)
        lows.append(low)
        dates.append(the_date)
#use try and except in case there are any errors in data (ex: line 50)
#f allows us to fill in data without commas

#print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
#(x, y, color, transparency)
#plot function creates line graph

plt.title("Daily High and Low Temps, 2018\nDeath Valley", fontsize = 16)
plt.xlabel("")
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", labelsize = 16)
#, which = 'major' selects benchmarks for you, went between axis and labelsize

fig.autofmt_xdate()

plt.show()