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
# find total of net_profit
total = 0
for month in net_profit:
    total += int(month)

#find average change in net_profit (change y/change x)
for_average = []
count = 0
for count in range(len(net_profit[:-1])):
    x = int(net_profit[count+1])
    y = int(net_profit[count])
    z = x-y
    for_average.append(z)
    count +=1
average = (sum(for_average)/len(for_average))
change=(round(average,2))

#turn lists into a dictionary
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


#   under this comment is everything we want to print on the homework
print("```text")
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${total}')
print(f'Average Change: ${change}')
print(f'Greatest Increase in Profits: {y[0]} (${y[1]})')
print(f'Greatest Decrease in Profits: {z[0]} (${z[1]})')
print("'''")

# Set variable for output txt file
my_file = os.path.join("pybank.txt")
with open(my_file, "w") as datafile: 
    datafile.write("```text\n")
    datafile.write("Financial Analysis\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Months: {len(months)}\n')
    datafile.write(f'Total: ${total}\n')
    datafile.write(f'Average Change: ${change}\n')
    datafile.write(f'Greatest Increase in Profits: {y[0]} (${y[1]})\n')
    datafile.write(f'Greatest Decrease in Profits: {z[0]} (${z[1]})\n')
    datafile.write("'''\n")
