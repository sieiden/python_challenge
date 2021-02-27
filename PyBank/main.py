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
# put the months and net_profit together into rows
budget = zip(months, net_profit)
# find total of net_profit
total = 0
for month in net_profit:
    total = total + int(month)
#find average change in net_profit (change y/change x)
change_y = int(net_profit[-1])-int(net_profit[0])
change_x = int(len(months))
print(change_y/change_x)
# find greatest increase in profits
#turn lists into a dictionary
stats_profit = {months[i]: net_profit[i] for i in range(len(months))}
greatest_increase = 0
for key in stats_profit:
    key = key
    x = int(stats_profit[key])
    if x > greatest_increase:
        greatest_increase = x
        y = [key,x]
    else:
        greatest_increase = greatest_increase
print(y)
#   under this comment is everything we want to print on the homework
print("```text")
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${total}')
print(f'Average Change: $')
print(f'Greatest Increase in Profits: ')
print(f'Greatest Decrease in Profits: ')
print("'''")