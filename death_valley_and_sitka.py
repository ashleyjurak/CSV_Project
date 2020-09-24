import csv
from datetime import datetime

dv_file = open("death_valley_2018_simple.csv", "r")
sw_file = open("sitka_weather_2018_simple.csv", "r")

csv_dv_file = csv.reader(dv_file, delimiter = ",")
csv_sw_file = csv.reader(sw_file, delimiter = ",")

dv_header_row = next(csv_dv_file)
sw_header_row = next(csv_sw_file)
'''
print(header_row)

#enumerate shows us index and value of each item in list

for index, column_header in enumerate(header_row):
    print(index,column_header)
'''
dv_highs = [] #for y axis
sw_highs = []
dv_dates = [] #for x axis
sw_dates = []

#print(x)

for row in csv_dv_file:
    try:
        dv_high = int(row[4])
        dv_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: #if anything in try fails
        print(f'Missing data for {dv_date}')
    else: #if nothing fails
        dv_highs.append(dv_high)
        dv_dates.append(dv_date)

for row in csv_sw_file:
    try:
        sw_high = int(row[5])
        sw_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: #if anything in try fails
        print(f'Missing data for {sw_date}')
    else: #if nothing fails
        sw_highs.append(sw_high)
        sw_dates.append(sw_date)



import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dv_dates, dv_highs, c = 'red', alpha = 0.5)
plt.plot(sw_dates, sw_highs, c = 'blue', alpha = 0.5)
#(x, y, color, transparency)
#plot function creates line graph

plt.title("Daily High Temps, 2018\nDeath Valley and Sitka", fontsize = 16)
plt.xlabel("")
#plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = "both", labelsize = 16)
#, which = 'major' selects benchmarks for you, went between axis and labelsize

fig.autofmt_xdate()

plt.show()