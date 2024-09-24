import os
import csv

# Get the current directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths relative to the script's directory
csvpath = os.path.join(script_dir, 'Resources', 'election_data.csv')
output_path = os.path.join(script_dir, 'analysis', 'election_results.txt')

# Initialize variables for tracking data
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Check if the CSV file exists
if not os.path.exists(csvpath):
    print(f"Error: CSV file not found at {csvpath}")
    exit(1)

# Read the CSV file
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Store header row
    header = next(csvreader)

    # Process each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Track votes for each candidate
        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Prepare output
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

# Calculate percentages and determine the winner
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Print results to terminal
print(output)

# Write results to text file
os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure the directory exists
with open(output_path, mode='w') as file:
    file.write(output)

print(f"Results exported to {output_path}")
N