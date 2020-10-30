# Retreive Data
# Import all needed libraries, modules, and dependencies
# Total Number of votes casted
# List of all candidates who recieved votes
# Total number of votes each candidate recieved
# Percentage of votes each candidate recieved
# The winner of the election

# Add dependencies
import csv
import os
# Assign a variable to load a file from path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)