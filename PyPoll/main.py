#this is for PyPoll
#import the os module
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#create lists to hold values
voter_id = []
county = []
candidate = []

#read csv file
with open(csvpath, "r", encoding='utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader) # pop one row
    # Read each row of data after the header
    for row in csvreader:
        # append to value lists
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
#   under this comment is everything we want to print on the homework
print("```text")
print("Election Results")
print("----------------------------")
print(f'Total Votes: {len(voter_id)}')
print("----------------------------")
print(f'Khan:')
print(f'Correy:')
print(f'Li:)')
print(f'O\'Tooley:')
print("----------------------------")
print(f'Winner:')
print("```")