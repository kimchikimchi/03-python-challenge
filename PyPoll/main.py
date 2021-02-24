#!/usr/bin/python3

import os
import csv

result = {}

# Parse the source data file
# use dirname for Windows users as gitbash messes up their path. Ugh
with open(os.path.join(os.path.dirname("__name__"), "Resources", "election_data.csv")) as csvfile:
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

# Store output into a variable to recycle both for stdout and file output
line_sep = '-------------------------'
output = (  "Election Results\n" +
            f"{line_sep}\n" +
            f"Total Votes: {total_votes}\n"
            f"{line_sep}\n"
        )

last_winning_votes = 0

for candidate, votes in result.items():
    percent = votes / total_votes * 100
    # Display up to 3 decimal points. Probably too OCD of me
    output += f"{candidate}: " + "%.3f" % round(percent, 3) + f"% ({votes})\n"
    if votes > last_winning_votes:
        last_winning_votes = votes
        winner = candidate

output += ( f"{line_sep}\n" +
            f"Winner: {winner}\n" +
            f"{line_sep}\n"
        )
print(output)

# Print the same info to a file
with open(os.path.join(os.path.dirname("__name__"), "analysis", "analysis.txt"), 'w') as outfile:
    outfile.write(output)
