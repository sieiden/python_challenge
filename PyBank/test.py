#import the os module
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#create lists to hold values
months = []
net_profit = []

#read csv file
with open(csvpath, "r", encoding='utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader) # pop one row
    # Read each row of data after the header
    for row in csvreader:
        # append to value lists
        months.append(row[0])
        net_profit.append(row[1])

profitanalysis = {months[i]:net_profit[i] for i in range(len(months))}
greatest_increase = 0
greatest_decrease = 0
for key in profitanalysis:
    key = key
    x = int(profitanalysis[key])
    if x > 0 and x > greatest_increase:
        greatest_increase = x
        y = [key,x]
    elif x < 0 and x < greatest_decrease:
        greatest_decrease = x
        z = [key,x]
    else:
        greatest_increase = greatest_increase
        greatest_decrease = greatest_decrease
print(greatest_increase)
print(greatest_decrease)