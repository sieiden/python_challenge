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
# net_profit is a list so turn into int for sum
total = 0
for month in net_profit:
    total = total + int(month)
#   under this comment is everything we want to print on the homework
print("```text")
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: {total}')