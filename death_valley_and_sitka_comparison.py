import csv
from datetime import datetime

dv_file = open("death_valley_2018_simple.csv", "r")
sw_file = open("sitka_weather_2018_simple.csv", "r")

csv_dv_file = csv.reader(dv_file, delimiter = ",")
csv_sw_file = csv.reader(sw_file, delimiter = ",")

dv_header_row = next(csv_dv_file)
sw_header_row = next(csv_sw_file)

dv_highs = [] #for y axis
dv_lows = []
sw_highs = []
sw_lows = []
dv_dates = [] #for x axis
sw_dates = []
'''
dv_header_row = next(csv_dv_file)

for index, column_header in enumerate(dv_header_row):
    dv_in = index
    dv_ch = column_header
    if column_header == "TMAX":
        dv_index = dv_in
        break

print(dv_index)

sw_header_row = next(csv_sw_file)

for index, column_header in enumerate(sw_header_row):
    sw_in = index
    sw_ch = column_header
'''

for row in csv_dv_file:
    try:
        dv_high = int(row[4]) #replace number with enumerate function
        dv_low = int(row[5])
        dv_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: #if anything in try fails
        print(f'Missing data for {dv_date}')
    else: #if nothing fails
        dv_highs.append(dv_high)
        dv_lows.append(dv_low)
        dv_dates.append(dv_date)

for row in csv_sw_file:
    try:
        sw_high = int(row[5])
        sw_low = int(row[6])
        sw_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: #if anything in try fails
        print(f'Missing data for {sw_date}')
    else: #if nothing fails
        sw_highs.append(sw_high)
        sw_lows.append(sw_low)
        sw_dates.append(sw_date)

import matplotlib.pyplot as plt

fig,ax = plt.subplots(2,1)

ax[0].plot(sw_dates, sw_highs, c = 'red', alpha = 0.5)
ax[0].plot(sw_dates, sw_lows, c = 'blue', alpha = 0.5)
ax[1].plot(dv_dates, dv_highs, c = 'red', alpha = 0.5)
ax[1].plot(dv_dates, dv_lows, c = 'blue', alpha = 0.5)

ax[0].set_title("Temperature comparision between Sitka Airport, AK US and Death Valley, CA US\n\nSitka Airport, AK US")
ax[1].set_title("Death Valley, CA US")
plt.xlabel("")
ax[0].fill_between(sw_dates, sw_highs, sw_lows, facecolor = 'blue', alpha = 0.1)
ax[1].fill_between(dv_dates, dv_highs, dv_lows, facecolor = 'blue', alpha = 0.1)

plt.show()
