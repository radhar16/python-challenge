import os
import csv

# Path to collect data from the Resources folder
pyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Creating lists to read the data
date = []
profit_losses = []
profit_loss_changes = []

total_months = 0
net_profit_losses = 0
first_profit_loss = 0


# # Read in the CSV file
with open(pyBank_csv, 'r' ) as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # calculate total number of months
        total_months = total_months + 1
        date.append(row[0])

        # calculate net total amount of "Profit/Losses" over the entire period
        net_profit_losses = net_profit_losses + int(row[1])
        
        # calculate changes in "Profit/Losses" over the entire period
        final_profit_loss = int(row[1])
        change_profit_loss = final_profit_loss - first_profit_loss
        
        profit_loss_changes.append(change_profit_loss)

        first_profit_loss = final_profit_loss

    total = sum(profit_loss_changes) - profit_loss_changes[0]
    average_profit_loss = round(total/(total_months - 1), 2)

    # Calculate the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profit_loss_changes)
    greatest_increase_index = profit_loss_changes.index(greatest_increase)

    # Calculate the greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(profit_loss_changes)
    greatest_decrease_index = profit_loss_changes.index(greatest_decrease)


    # Print out the results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")        
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {date[greatest_increase_index]} (${greatest_increase})")   
print(f"Greatest Decrease in Profits: {date[greatest_decrease_index]} (${greatest_decrease})")   

output_file = os.path.join('..', "Analysis", "output_data.txt")
with open(output_file, "w") as outputfile:
    outputfile.write(f"Financial Analysis"+"\n")
    outputfile.write(f"----------------------------"+"\n")
    outputfile.write(f"Total Months: {total_months}"+"\n")
    outputfile.write(f"Total: ${net_profit_losses}"+"\n")
    outputfile.write(f"Average Change: ${average_profit_loss}"+"\n")
    outputfile.write(f"Greatest Increase in Profits: {date[greatest_increase_index]} (${greatest_increase})"+"\n")
    outputfile.write(f"Greatest Decrease in Profits: {date[greatest_decrease_index]} (${greatest_decrease})"+"\n")

    




   


        
            
