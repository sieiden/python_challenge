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
# add unique values to candidate list
unique = []
for person in candidate:
    if person not in unique:
        unique.append(person)
# Find the total number of votes each candidate won
candidate0_total= 0
candidate1_total = 0
candidate2_total = 0
candidate3_total = 0
candidate0 = unique[0]
candidate1 = unique[1]
candidate2 = unique[2]
candidate3 = unique[3]
for name in candidate:
    if name == candidate0:
         candidate0_total +=1
    elif name == candidate1:
         candidate1_total +=1
    elif name == candidate2:
         candidate2_total +=1 
    elif name == candidate3:
         candidate3_total +=1 
      
# Find the percentage of votes each candidate won
totals =[candidate0_total,candidate1_total,candidate2_total,candidate3_total]
ctotals = []
for total in totals:
    x =(total/len(voter_id))*100
    y = round(x,3)
    ctotals.append(y)

# Find the winner of the election based on popular vote.
cwinner = {unique[i]: totals[i] for i in range(len(unique))}
highest_votes = 0
for key in cwinner:
    key = key
    x = int(cwinner[key])
    if x > highest_votes:
        highest_votes = x
        y = [key,x]
    else:
        highest_votes = highest_votes

# under this comment is everything we want to print on the homework
print("```text")
print("Election Results")
print("----------------------------")
print(f'Total Votes: {len(voter_id)}')
print("----------------------------")
print(f'{unique[0]}: {ctotals[0]}% ({candidate0_total})')
print(f'{unique[1]}: {ctotals[1]}% ({candidate1_total})')
print(f'{unique[2]}: {ctotals[2]}% ({candidate2_total})')
print(f'{unique[3]}: {ctotals[3]}% ({candidate3_total})')
print("----------------------------")
print(f'Winner: {y[0]}')
print("```")

#write to txt file
my_file = os.path.join("pypoll.txt")
with open(my_file, "w") as datafile: 
    datafile.write("```text\n")
    datafile.write("Election Results\n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Votes: {len(voter_id)}\n')
    datafile.write("----------------------------\n")
    datafile.write(f'{unique[0]}: {ctotals[0]}% ({candidate0_total})\n')
    datafile.write(f'{unique[1]}: {ctotals[1]}% ({candidate1_total})\n')
    datafile.write(f'{unique[2]}: {ctotals[2]}% ({candidate2_total})\n')
    datafile.write(f'{unique[3]}: {ctotals[3]}% ({candidate3_total})\n')
    datafile.write("----------------------------\n")
    datafile.write(f'Winner: {y[0]}\n')
    datafile.write("```")
