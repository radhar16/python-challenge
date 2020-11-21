import os
import csv

# Path to collect data from the Resources folder
pyPoll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Creating lists to read the data
vote_counts = []
candidates = []
unique_candidates = []
percent_vote = []

total_counts = 0

# Read in the CSV file
with open(pyPoll_csv, 'r' ) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)

    for row in csvreader:
        # calculate total number of vote counts
        total_counts = total_counts + 1

        #Append canditates
        candidates.append(row[2])
    
    #set() is used to check for unique values
    for candidate in set(candidates):
        unique_candidates.append(candidate)
        
        # calcualate the total votes for each candidate.
        votes = candidates.count(candidate)
        vote_counts.append(votes)

        # calculate the percentage of votes each candidate won.
        percent = round((votes/total_counts)*100,2)
        percent_vote.append(percent)

      
    #Identifying the winner based on max vote counts by using index() function to return the winner candidate.
    winning_votes_count = max(vote_counts)
    winner = unique_candidates[vote_counts.index(winning_votes_count)]

print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_counts}") 
print(f"-----------------------------")
for i in range(len(unique_candidates)):
            print(f"{unique_candidates[i]} :  {percent_vote[i]}%   ({vote_counts[i]})")
print(f"-----------------------------")
print(f"Winner : {winner}") 
print(f"-----------------------------")


# Set variable for output file
output_file = os.path.join('..', "Analysis", "output_data.txt")

#  Open the output file
with open(output_file, "w") as datafile:
     
    datafile.write(f"Election Results"+"\n")
    datafile.write(f"-----------------------------"+"\n")
    datafile.write(f"Total Votes: {total_counts}"+"\n") 
    datafile.write(f"-----------------------------"+"\n")
    for i in range(len(unique_candidates)):
        datafile.write(f"{unique_candidates[i]} :  {percent_vote[i]}%   ({vote_counts[i]})"+"\n")
    datafile.write(f"-----------------------------"+"\n")
    datafile.write(f"Winner : {winner}"+"\n") 
    datafile.write(f"-----------------------------"+"\n")
