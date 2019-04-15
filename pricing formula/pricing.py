import csv
import statistics
from collections import defaultdict

location = input("Enter location: ")
numgallons = int(input("Enter number of gallons: "))
month = input("Enter month: ") # case sensative

columns2017 = defaultdict(list) # each value in each column is appended to a list
columns2018 = defaultdict(list) # each value in each column is appended to a list


with open('Competitors_rate-2017.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns2017[k].append(v) # append the value into the appropriate list
                                 # based on column name k

with open('Competitors_rate-2018.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns2018[k].append(v) # append the value into the appropriate list
                                 # based on column name k

monthlist1 = [float(i) for i in columns2017[month]]
monthlist2 = [float(i) for i in columns2018[month]]
transporationfee = 2
minprice = ((min(monthlist1)+min(monthlist2))/2)*numgallons
if location == "Texas":
    competitorsprice = ((statistics.mean(monthlist1)+statistics.mean(monthlist2))/2)*numgallons
else:
    competitorsprice = ((statistics.mean(monthlist1)+statistics.mean(monthlist2))/2)*numgallons + transporationfee
print(minprice)
print(round(competitorsprice, 3))

