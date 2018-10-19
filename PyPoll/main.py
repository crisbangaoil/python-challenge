# import dependencies
import os
import csv

# import file
csvpath = 'election_data.csv'

#read the csv
with open(csvpath, newline='') as csvfile:

    # split the data by commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # define adding variables
    total = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    # skip the header
    next(csvreader)

    for row in csvreader:

        # count total votes
        total = total + 1

        # count votes per candidate
        if row[2] == "Khan":
            khan = khan + 1
        
        if row[2] == "Correy":
            correy = correy + 1
        
        if row[2] == "Li":
            li = li + 1

        if row[2] == "O'Tooley":
            otooley = otooley + 1

    # calculate vote percentages and round
    khanper = khan / total * 100
    khanper = str(round(khanper, 3))
    correyper = correy / total * 100
    correyper = str(round(correyper, 3))
    liper = li / total * 100
    liper = str(round(liper, 3))
    otooleyper = otooley / total *100
    otooleyper = str(round(otooleyper, 3))

    # determine the winner (does not account for ties)
    winner = ''
    
    if khan > correy:
        if khan > li:
            if khan > otooley:
                winner = "Khan"
            else:
                winner = "O'Tooley"
        else:
            if li > otooley:
                winner = "Li"
            else :
                winner = "O'Tooley"
    else:
        if correy > li:
            if correy > otooley:
                winner = "Correy"
            else:
                winner = "O'Tooley"
        else:
            if li > otooley:
                winner = "Li"
            else:
                winner = "O'Tooley"

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total}")
    print("-------------------------")
    print(f"Khan: {khanper}% ({khan})")
    print(f"Correy: {correyper}% ({correy})")
    print(f"Li: {liper}% ({li})")
    print(f"O'Tooley: {otooleyper}% ({otooley})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    txt = open("PyPoll_Results.txt","w+")
    txt.write("Election Results")
    txt.write("\n")
    txt.write("-------------------------")
    txt.write("\n")
    txt.write(f"Total Votes: {total}")
    txt.write("\n")
    txt.write("-------------------------")
    txt.write("\n")
    txt.write(f"Khan: {khanper}% ({khan})")
    txt.write("\n")
    txt.write(f"Correy: {correyper}% ({correy})")
    txt.write("\n")
    txt.write(f"Li: {liper}% ({li})")
    txt.write("\n")
    txt.write(f"O'Tooley: {otooleyper}% ({otooley})")
    txt.write("\n")
    txt.write("-------------------------")
    txt.write("\n")
    txt.write(f"Winner: {winner}")
    txt.write("\n")
    txt.write("-------------------------") 
    
