# import dependencies
import os
import csv

# import file
csvpath = 'budget_data.csv'

# read the csv
with open(csvpath, newline='') as csvfile:

    # split the data by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # define variable
    count = 0   
    total = 0
    maxmonth = ''
    maxprofit = 0
    minmonth = ''
    minprofit = 1000000
    lasttotal = 0

    # Skip the header
    next(csvreader)

    for row in csvreader:
       
        # Count the Rows
        count = count + 1
        # Running Total of Profits
        total = total + int(row[1])

        # Finding the Greatest Increase in Profits
        if int(row[1]) - lasttotal > maxprofit:
            maxprofit = int(row[1]) - lasttotal
            maxmonth = row[0]

        # Finding the Greatest Decrease in Profits
        if int(row[1]) - lasttotal < minprofit:
            minprofit = int(row[1]) - lasttotal
            minmonth = row[0]

        # Store the prior row total for comparison
        lasttotal = int(row[1])

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Greatest Increase in Profits: {maxmonth} (${maxprofit})")
    print(f"Greatest Decrease in Profits: {minmonth} (${minprofit})")

    txt = open("PyBank_Results.txt","w+")
    txt.write("Financial Analysis")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write(f"Total Months: {count}")
    txt.write("\n")
    txt.write(f"Total: ${total}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: {maxmonth} (${maxprofit})")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: {minmonth} (${minprofit})")





    


