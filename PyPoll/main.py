#this is for PyPoll
#import the os module
import os

# Module for reading CSV files
import csv
csvpath = os.path.join(.., 'python_challenge','PyPoll','Resources', 'election_data.csv')

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
        votor_id.append(row[0])
        county.append(row[1])
        candidate.append(row[3])