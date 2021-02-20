#!/usr/bin/python

import os
import csv

result = {}

# Parse the source data file
with open(os.path.join("Resources", "election_data.csv")) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(reader)

    '''
    # This operation would look more elegant but 
    # double memory footprint by duplicating data.
    # all_votes = list(reader)
    # total_votes = len(all_votes)
    '''
    total_votes = 0

    for row in reader:
        candidate = row[2]
        total_votes += 1

        # Using dictionary as a vote counter per each
        # candidate as key
        # Check if candidate already exists as a key.
        # If not, create one and start with count 1.
        # Otherwise, increament votes by 1
        if candidate in result:
            result[candidate] += 1
        else:
            result[candidate] = 1

line_sep = '-------------------------'
print("Election Results")
print(f"{line_sep}")
print(f"Total Votes: {total_votes}")
print(f"{line_sep}")

last_winning_votes = 0

for candidate, votes in result.items():
    percent = votes / total_votes * 100
    print(f"{candidate}: {round(percent, 2)}% ({votes})")

    if votes > last_winning_votes:
        last_winning_votes = votes
        winner = candidate

print(f"{line_sep}")
print(f"Winner: {winner}")       
print(f"{line_sep}")

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.