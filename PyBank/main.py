#!/usr/bin/python3

import os
import csv


# Open the source data file.
# use dirname for Windows users as gitbash messes up their path
with open(os.path.join(os.path.dirname("__name__"), "Resources", "budget_data.csv")) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Use the vars as constants
    MONTH = 0
    PANDL = 1

    # Skip the header
    next(reader)

    # Cast reader object to a list so we can propagate like one.
    list_monthly_budget = list(reader)

    # The total number of months included in the dataset
    total_months = len(list_monthly_budget)
    total_pandl = 0
    cumulative_daily_pandl_change = 0
    top_profit = 0
    top_profit_month = ''
    top_loss = 0
    top_loss_month = ''

    # Only to the 2nd from the last not to go past the last row while
    # looking 'ahead'
    for i in range(0, total_months - 1):
        # We'll compare two rows at a time
        current_month = list_monthly_budget[i]
        next_month = list_monthly_budget[i + 1]

        # Replace P&L strings to numbers in the list.
        current_month[PANDL] = int(current_month[PANDL])
        next_month[PANDL] = int(next_month[PANDL])

        # Only when reading the very first row, add its P&L number
        if i == 0:
            total_pandl += current_month[PANDL]
        total_pandl += next_month[PANDL]
        pandl_change = next_month[PANDL] - current_month[PANDL]

        cumulative_daily_pandl_change += (pandl_change)

        # Check whether we can the top proffit
        if pandl_change >  top_profit:
            top_profit_month = next_month[MONTH]
            top_profit = pandl_change
        elif pandl_change < top_loss:
            top_loss_month = next_month[MONTH]
            top_loss = pandl_change

    # We are counting *between months*, not number of months.  Hence -1
    avg_pandl_change = cumulative_daily_pandl_change / (total_months - 1)

    # Pull the output into a variable so that it can be reused.
    output = ( "Financial Analysis\n" +
               "----------------------------\n" +
               f"Total Months: {total_months}\n" +
               f"Total: ${total_pandl}\n" +
               f"Average Change: ${ round(avg_pandl_change, 2) }\n" +
               f"Greatest Increase in Profits: {top_profit_month} (${top_profit})\n" +
               f"Greatest Decrease in Profits: {top_loss_month} (${top_loss})\n"
            )
    print(output)

    # Print the same info to a file
    with open(os.path.join(os.path.dirname("__name__"), "analysis", "JCha_results.txt"), 'w') as outfile:
        outfile.write(output)