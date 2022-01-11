"""
Are there differences in activity patterns between weekdays and weekends?
1.	Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a given date is a weekday or weekend day.
2.	Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all weekdays or weekend days (y-axis).

hints - date time module to determine weekday vs weekend
"""
import csv
import statistics as st
import matplotlib.pyplot as plt
import datetime as dt
import pygal

dictDateDay = {}
dictDateEnd = {}
dictIntervalDay = {}
dictIntervalEnd = {}

# File without 'NA'
file = "newActivity.csv"
with open(file,"r") as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    print(headerRow) # test 

    for row in reader:
        steps = row[0]
        # Ignore NA step values
        if steps != "NA":
            date = row[1]
            date2 = dt.datetime.strptime(date, '%Y-%m-%d')

            interval = int(row[2])

            if dt.datetime.date(date2).weekday() < 5:
                dictDateDay.setdefault(str(date), [])
                dictDateDay[str(date)].append(int(steps))
                dictIntervalDay.setdefault(interval,[])
                dictIntervalDay[interval].append(int(steps))
            else:
                dictDateEnd.setdefault(str(date), [])
                dictDateEnd[str(date)].append(int(steps))
                dictIntervalEnd.setdefault(interval,[])
                dictIntervalEnd[interval].append(int(steps))
    
    listDateDay = []   # Stores weekday
    listDateEnd = [] # Stores weekend
    listTotalDay = []  # Stores total number of steps weekday
    listTotalEnd = [] # Stores total number os steps weekend
    listAveDay = []    # Stores avg # of steps in a day
    listAveEnd = []

    for i in dictDateDay.keys():
        listDateDay.append(i)
        listTotalDay.append(sum(dictDateDay.get(i)))
        listAveDay.append(st.mean(dictDateDay.get(i)))

    for i in dictDateEnd.keys():
        listDateEnd.append(i)
        listTotalEnd.append(sum(dictDateEnd.get(i)))
        listAveEnd.append(st.mean(dictDateEnd.get(i)))
    

    hist = pygal.Bar()
    hist._title = "Average steps per day on weekdays"
    hist._x_title = "Date"
    hist._y_title = "Freq"
    hist.x_labels = listDateDay
    hist.add("Average number of steps", listAveDay)
    hist.render_to_file("stepsversionWeekday.svg")

    hist = pygal.Bar()
    hist._title = "Average steps per day on weekends"
    hist._x_title = "Date"
    hist._y_title = "Freq"
    hist.x_labels = listDateEnd
    hist.add("Average number of steps", listAveEnd)
    hist.render_to_file("stepsversionWeekend.svg")
