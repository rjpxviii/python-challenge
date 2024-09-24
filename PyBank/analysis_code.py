# Import necessary libraries
import csv
import os

# Define the file path
file_path = '/Users/ryanpope/python-challenge/PyBank/Resources/budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []

# Open and read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader:
        # Extract the date and profit/loss
        date = row[0]
        profit = int(row[1])
        
        # Count the total number of months
        total_months += 1
        
        # Sum the total profit/loss
        net_total += profit
        
        # Track monthly changes in profit/loss
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)
        
        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write the results to a text file
output_path = '/Users/ryanpope/python-challenge/PyBank/analysis/financial_analysis.txt'

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
