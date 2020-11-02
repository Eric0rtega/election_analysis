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

# Create variable for total votes
total_votes = 0
# Declaring new list for candidate options.
candidate_options = []
# Declaring candidate votes dictionary.
candidate_votes = {}

# Winning candidate and winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Increment the total_votes value by 1.
        total_votes += 1
         # Print the candidate name from each row.
        candidate_name = row[2]
        # Check candidate list if candidate name is already added.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Track candidates vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidates count.
        candidate_votes[candidate_name] += 1

# Save results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final results to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes each candidate recieved.
    for candidate_name in candidate_votes:
        # Retrieve vote count of candidates.
        votes = candidate_votes[candidate_name]
        # Calculate the vote percentage.
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate.
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"--------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------\n")
    #print(winning_candidate_summary)
    # Print the candidate name and the percentage of votess.
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the votes.")